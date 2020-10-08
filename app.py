#!/usr/bin/env python3

from aws_cdk.core import App, Stack, Tags

from stream_data_lake.stream_data_lake_stack import StreamDataLakeStack

app = App()
stack = StreamDataLakeStack(app, "stream-data-lake")

# Tag all 
Tags.of(stack).add("EnvName", "nrawling")
Tags.of(stack).add("EnvType", "dev")
Tags.of(stack).add("OwnerContact", "nathan.rawling@hobsons.com")
Tags.of(stack).add("MaintenanceContact", "nathan.rawling@hobsons.com")
Tags.of(stack).add("ProductLine", "None")
Tags.of(stack).add("ProductComponent", "StreamDataLake")
Tags.of(stack).add("Provisioner", "aws-cdk")

app.synth()
