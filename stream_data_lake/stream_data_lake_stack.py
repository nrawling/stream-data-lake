from aws_cdk import (
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
    aws_rds as rds,
    aws_ec2 as ec2,
    aws_iam as iam,
    core
)

class StreamDataLakeStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # IAM Roles
        # TBD

	# First, we want to create a VPC for the Aurora DB
        self.vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           cidr="10.0.0.0/24",
                           nat_gateways=1,
                           )
        core.CfnOutput(self, "Output",
                       value=self.vpc.vpc_id)

        # Create Aurora Serverless instance to maintain current snapshot of data
        cluster = rds.ServerlessCluster(self, 'AnotherCluster',
                                        engine=rds.DatabaseClusterEngine.aurora_postgres(version=rds.AuroraPostgresEngineVersion.VER_11_7),
#                                        parameterGroup=rds.ParameterGroup.fromParameterGroupName(self, 'ParameterGroup', 'default.aurora-postgresql10'),
                                        vpc=self.vpc,
                                        scaling=rds.ServerlessScalingOptions(
                                            auto_pause=core.Duration.minutes(10),
                                            min_capacity=rds.AuroraCapacityUnit.ACU_1,
                                            max_capacity=rds.AuroraCapacityUnit.ACU_2,
                                        ))

        # Create Dynamo Source table
        dynamo = dynamodb.Table(self, "ss-nrawling-testtable-780856337633",
                                      partition_key=dynamodb.Attribute(name='PK', type=dynamodb.AttributeType.STRING))

        # S3 bucket will store stream output                                       
        bucket = s3.Bucket(self, "ss-nrawling-testbucket-780856337633",
                                 versioned=False, 
                                 removal_policy=core.RemovalPolicy.DESTROY,
                                 bucket_name="ss-nrawling-testbucket-780856337633")

        # Lambda function to process Dynamo Stream
	# TBD

        # Kinesis Stream
        # TBD
