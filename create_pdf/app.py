import logging
from datetime import datetime

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


lambda_handler({
    "type_pdf": "quote",
    "quote_id": 11,
    "data": {
        "prospect_id": 14465,
        "event_id": 2,
        "qr_url": "https://api-collect-info-cem-qr.s3.amazonaws.com/qrs/event_2/prospect_14465.png",
        "consultant": "Clemencio Seller",
        "event_name": "Expo Canadá TEST 2023",
        "request": 21,
        "created_at": datetime(2023, 9, 9, 8, 38, 30),
        "first_name": "Clemencia",
        "last_name": "Perez",
        "email": "clemencia@clemencio.com",
        "birthday": "2023-02-22",
        "address": None,
        "state": "Campeche",
        "phone": "1234567890",
        "gender": "Femenino",
        "country": "México",
        "program_name": "Business - Accounting",
        "location": "Toronto",
        "credential_type": "Undergraduate Diploma",
        "duration": "2 years",
        "start_date": "January",
        "tuition_from": "31384",
        "tuition_to": "31384",
        "logo_path": "https://api-collect-info-cem-qr.s3.amazonaws.com/logos_school/niagara+college-toronto.png",
        "notes": "This is a note",
        "signature_url": "https://api-collect-info-cem-qr.s3.amazonaws.com/signatures/event_2/request_19.png",
        "tuition_range": "From 31384 to 31384",
        "quote_number": "0000000011",
        "request_number": "0000000021",
        "date": "September 09, 2023",
    },
}, None
)