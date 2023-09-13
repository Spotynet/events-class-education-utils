import os
import io
import boto3
import logging
from botocore.exceptions import ClientError

BUCKET_NAME = os.environ.get("BUCKET_NAME")

class S3utils:
    """S3 class for uploading files to S3 bucket"""
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def sending_pdf_to_s3(self, file: bytes, data: dict):
        pdf_stream = io.BytesIO(file)

        url = f"pdfs/event-{data['event_id']}/{data['prospect_id']}-{data['name_prospect']}/{data['date']}-{data['type_pdf']}-{data['name_prospect']}.pdf"

        try:
            self.s3_client.upload_fileobj(pdf_stream, BUCKET_NAME, url)
            self._set_object_access_policy(BUCKET_NAME, url)
        except ClientError as e:
            logging.error(e)
            return False

        pdf_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{url}"

        return pdf_url
    
    def _set_object_access_policy(self,bucket_name, object_key):
        """
        This function adds ACL policy for object in S3 bucket.
        :return: None
        """
        response = self.s3_client.put_object_acl(ACL="public-read", Bucket=bucket_name, Key=object_key)
        return response