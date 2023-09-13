#!/usr/bin/env node

const cdk = require("aws-cdk-lib");
const { CreatePdfStack } = require("../lib/stack");

const STACK_NAME = "events-class-education-utils";
const app = new cdk.App();
new CreatePdfStack(app, STACK_NAME, {
  /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */

  /* Uncomment the next line to specialize this stack for the AWS Account
   * and Region that are implied by the current CLI configuration. */
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
    env: process.env.ENV,
    stackName: STACK_NAME
  },

  /* Uncomment the next line if you know exactly what Account and Region you
   * want to deploy the stack to. */
  // env: { account: '123456789012', region: 'us-east-1' },

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});
