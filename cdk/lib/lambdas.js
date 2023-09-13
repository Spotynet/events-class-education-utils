const { Duration } = require('aws-cdk-lib');
const { Construct } = require('constructs');

const lambda = require('aws-cdk-lib/aws-lambda');
const path = require('path');
const { RetentionDays } = require('aws-cdk-lib/aws-logs');

class Lambdas extends Construct {
    constructor(scope, id, props, roles) {
        super(scope, id, props);

        this.createPdf = new lambda.DockerImageFunction(scope, 'CreatePdf', {
            description: "Function that creates a PDF from a HTML template and a JSON payload, then uploads it to S3 and return the URL.",
            functionName: `${props.env.stackName}-create-pdf-${props.env.env}`,
            code: lambda.DockerImageCode.fromImageAsset(path.join(__dirname, '../../create_pdf')),
            timeout: Duration.minutes(15),
            memorySize: 1024,
            logRetention: RetentionDays.ONE_MONTH,
            role: roles.lambdaRole,
        });
        }
}

module.exports = { Lambdas }
