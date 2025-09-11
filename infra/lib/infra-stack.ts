import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Duration, Stack, StackProps, Tags } from 'aws-cdk-lib';
import { LambdaIntegration, LambdaRestApi, Period, RateLimitedApiKey } from 'aws-cdk-lib/aws-apigateway';
import { DockerImageCode, DockerImageFunction } from 'aws-cdk-lib/aws-lambda';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'InfraQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
    const lambdaFunction = new DockerImageFunction(this, `SeleniumLambda`, {
          code: DockerImageCode.fromImageAsset("../src"),
          timeout: Duration.seconds(40),
          functionName: `selenium-function`,
          memorySize: 512,
          logRetention: RetentionDays.ONE_WEEK
        });
  }
}
