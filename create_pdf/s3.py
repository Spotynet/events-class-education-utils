import logging
import os
from botocore.exceptions import ClientError

BUCKET_NAME = os.environ.get("BUCKET_NAME")

class S3utils:
    """S3 class for uploading files to S3 bucket"""

    def sending_pdf_to_s3(self, file: bytes, data: dict):
        temp_pdf_path = f"temp_{data['prospect_id']}.pdf"
        with open(temp_pdf_path, "wb") as f:
            f.write(file)

        url = f"pdfs/event_{data['event_id']}/{data['prospect_id']}_{data['name_prospect']}/{data['type_pdf']}_{data['quote_number']}_{data['name_prospect']}.pdf"

        try:
            S3.upload_file(temp_pdf_path, BUCKET_NAME, url)
            self._set_object_access_policy(BUCKET_NAME, url)
        except ClientError as e:
            logging.error(e)
            return False

        os.remove(temp_pdf_path)

        pdf_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{url}"

        return pdf_url
    def _set_object_access_policy(self,bucket_name, object_key):
        """
        This function adds ACL policy for object in S3 bucket.
        :return: None
        """
        response = S3.put_object_acl(ACL="public-read", Bucket=bucket_name, Key=object_key)
        return response