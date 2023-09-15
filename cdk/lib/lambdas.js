const { Duration } = require('aws-cdk-lib');
const { Construct } = require('constructs');
const { RetentionDays } = require('aws-cdk-lib/aws-logs');
const lambda = require('aws-cdk-lib/aws-lambda');
const path = require('path');
const config = require('../config/config.json');

class Lambdas extends Construct {
    constructor(scope, id, props, roles) {
        super(scope, id, props);

        const { env } = props.env;

        const layerWkHtmlToPdf = lambda.LayerVersion.fromLayerVersionArn(this, "wkhtmltopdf", `${config.environment[env].layerWhtmlToPdfArn}`);

        this.createPdf = new lambda.Function(this, "CreatePdf", {
            description: "Function that creates a PDF from a HTML template and a JSON payload, then uploads it to S3 and return the URL.",
            functionName: `${props.env.stackName}-create-pdf-${props.env.env}`,
            code: lambda.Code.fromAsset(path.join(__dirname, '../../create_pdf'), {
                bundling: {
                    image: lambda.Runtime.PYTHON_3_9.bundlingImage,
                    command: [
                        'bash',
                        '-c',
                        'pip install -r requirements.txt -t /asset-output && cp -au . /asset-output',
                    ],
                },
            }),
            runtime: lambda.Runtime.PYTHON_3_9,
            handler: "app.lambda_handler",
            timeout: Duration.minutes(15),
            memorySize: 1024,
            logRetention: RetentionDays.ONE_MONTH,
            environment: {
                BUCKET_NAME: `events-class-education-utils-storage-${props.env.env}`
            },
            role: roles.lambdaRole,
            layers: [layerWkHtmlToPdf],
        });

    }
}

module.exports = { Lambdas }
