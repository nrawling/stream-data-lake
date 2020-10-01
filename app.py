#!/usr/bin/env python3

from aws_cdk import core

from stream_data_lake.stream_data_lake_stack import StreamDataLakeStack

app = core.App()

StreamDataLakeStack(app, "stream-data-lake")

app.synth()
