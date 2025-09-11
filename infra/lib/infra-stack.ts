import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as ecr_assets from 'aws-cdk-lib/aws-ecr-assets';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
// VPC
      const vpc = new ec2.Vpc(this, 'SeleniumVpc', {
          maxAzs: 2
      });

      // ECS Cluster
      const cluster = new ecs.Cluster(this, 'SeleniumCluster', { vpc });

      // ✅ Build Docker image from local folder (where Dockerfile is)
      const seleniumImage = new ecr_assets.DockerImageAsset(this, 'SeleniumImage', {
          directory: '../src', // <-- adjust to where your Dockerfile lives
      });

      // Task Definition
      const taskDefinition = new ecs.FargateTaskDefinition(this, 'SeleniumTaskDef', {
          memoryLimitMiB: 1024,
          cpu: 512,
      });

      taskDefinition.addContainer('SeleniumContainer', {
          image: ecs.ContainerImage.fromDockerImageAsset(seleniumImage),
          logging: ecs.LogDrivers.awsLogs({ streamPrefix: 'selenium' }),
      });

      // EventBridge Rule (every 6 hours)
      const rule = new events.Rule(this, 'SeleniumSchedule', {
          schedule: events.Schedule.cron({ minute: '0', hour: '*/6' }),
      });

      // Target: ECS Task
      rule.addTarget(new targets.EcsTask({
          cluster,
          taskDefinition,
          taskCount: 1,
          subnetSelection: { subnetType: ec2.SubnetType.PUBLIC },
      }));
  }
}
