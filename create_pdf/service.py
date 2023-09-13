import os
import jinja2
import pdfkit

from s3 import S3utils

s3_utils = S3utils()


class Service:
    """
    Service to create PDFs
    """

    def create_pdfs_to_quote(self, data: dict):
        data = self._prepare_data(data)

        application_url = self._create_pdf(data, "application_template")
        quote_url = self._create_pdf(data, "quote_template")
        terms_and_conditions_url = self._create_pdf(data, "terms_and_conditions_template")

        response = {
            "application_url": application_url,
            "quote_url": quote_url,
            "terms_and_conditions_url": terms_and_conditions_url,
        }

        return response

    def create_pdfs_to_payment(self, data: dict):
        data = self._prepare_data(data)

        payment_url = self._create_pdf(data, "payment_template")

        return {
            "payment_url": payment_url,
        }

    def _prepare_data(self, data: dict):
        data["tuition_range"] = f"From {data['tuition_from']} to {data['tuition_to']}"
        data["quote_number"] = str(data["quote_id"]).zfill(10)
        data["request_number"] = str(data["request"]).zfill(10)

        return data

    def _create_pdf(self, data: dict, template_name: str):
        context = data

        template_loader = jinja2.FileSystemLoader("./")
        template_env = jinja2.Environment(loader=template_loader)

        html_template = f"./templates/{template_name}.html"
        template = template_env.get_template(html_template)
        output_text = template.render(context)

        # Encuentra la ruta completa al ejecutable wkhtmltopdf
        wkhtmltopdf_path = os.popen("which wkhtmltopdf").read().strip()
        # Configura la ruta a wkhtmltopdf usando la ruta encontrada
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        options = {
            "encoding": "utf-8",
            "page-size": "Letter",
            "footer-center": "www.classeducation.com",
            "footer-font-size": "8",
            "footer-spacing": "10",
            "margin-left": "1.18in",
            "margin-right": "1.18in",
            "margin-top": "0.78in",
            "margin-bottom": "0.78in",
        }

        pdf_content = pdfkit.from_string(output_text, configuration=config, options=options)

        if "application" in template_name:
            type_pdf = "application"
        elif "quote" in template_name:
            type_pdf = "quote"
        elif "conditions" in template_name:
            type_pdf = "terms_and_conditions"
        elif "payment" in template_name:
            type_pdf = "payment"

        url_pdf = s3_utils.sending_pdf_to_s3(
            pdf_content,
            {
                "event_id": data["event_id"],
                "prospect_id": data["prospect_id"],
                "name_prospect": data["first_name"].lower() + "-" + data["last_name"].lower(),
                "type_pdf": type_pdf,
                "date": data["created_at"].split("T")[0],
            },
        )

        return url_pdf
