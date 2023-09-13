const { Stack } = require('aws-cdk-lib');
const { Lambdas } = require('./lambdas');
const Roles = require('./roles');

class CreatePdfStack extends Stack {
  /**
   *
   * @param {Construct} scope
   * @param {string} id
   * @param {StackProps=} props
   */
  constructor(scope, id, props) {
    super(scope, id, props);

    const roles = new Roles(this, 'Roles', props);
    new Lambdas(this, 'Lambdas', props, roles)
  }
}

module.exports = { CreatePdfStack }
