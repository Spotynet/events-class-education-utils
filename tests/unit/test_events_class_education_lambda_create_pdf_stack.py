import aws_cdk as core
import aws_cdk.assertions as assertions

from events_class_education_lambda_create_pdf.events_class_education_lambda_create_pdf_stack import EventsClassEducationLambdaCreatePdfStack

# example tests. To run these tests, uncomment this file along with the example
# resource in events_class_education_lambda_create_pdf/events_class_education_lambda_create_pdf_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EventsClassEducationLambdaCreatePdfStack(app, "events-class-education-lambda-create-pdf")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
