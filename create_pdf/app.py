import logging

from service import Service

logger = logging.getLogger()
logger.setLevel(logging.INFO)

service = Service()

def lambda_handler(event, _):
    logger.info({"event": event})

    data = event["data"]
    data["quote_id"] = event["quote_id"]

    if event["type_pdf"] == "quote":
        response = service.create_pdfs_to_quote(data)
    elif event["type_pdf"] == "payment":
        response = service.create_pdfs_to_payment(data)
    
    logger.info({"response": response})

    return response