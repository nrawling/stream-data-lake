from aws_cdk import (
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
    core
)

class StreamDataLakeStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dynamo = dynamodb.Table(self, "ss-nrawling-testtable-780856337633",
                                      partition_key=dynamodb.Attribute(name='PK', type=dynamodb.AttributeType.STRING))
                                       
        bucket = s3.Bucket(self, "ss-nrawling-testbucket-780856337633",
                                 versioned=False, 
                                 removal_policy=core.RemovalPolicy.DESTROY,
                                 bucket_name="ss-nrawling-testbucket-780856337633")
