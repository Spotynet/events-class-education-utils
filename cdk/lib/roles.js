const { Construct } = require("constructs");
const iam = require("aws-cdk-lib/aws-iam");

class Roles extends Construct {
  constructor(scope, id, props) {
    super(scope, id);

    this.lambdaRole = iam.Role.fromRoleArn(
      scope,
      "LambdaRole",
      `arn:aws:iam::346463309815:role/S3PutObjectRole`,
      { mutable: false }
    );
  }
}

module.exports = Roles;