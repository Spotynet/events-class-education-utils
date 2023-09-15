#!/usr/bin/env node
const cdk = require("aws-cdk-lib");
const { CreatePdfStack } = require("../lib/stack");

const STACK_NAME = "events-class-education-utils";
const app = new cdk.App();

// Development stage
const STACK_NAME_DEV = `${STACK_NAME}-dev`;
new CreatePdfStack(app, STACK_NAME_DEV, {
  env: {
    account: '346463309815',
    region: 'us-west-1',
    env: 'dev',
    stackName: STACK_NAME
  },
  imageTag: '1.0.0',
  containerCount: 1,
});

// Production stage with two environments
const STACK_NAME_PROD = `${STACK_NAME}-prod`;
new CreatePdfStack(app, STACK_NAME_PROD, {
  env: {
    account: '346463309815',
    region: 'us-east-1',
    env: 'prod',
    stackName: STACK_NAME
  },
  imageTag: '1.0.0',
  containerCount: 2,
});