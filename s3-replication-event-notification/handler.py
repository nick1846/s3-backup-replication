import json


def s3ReplicationEvent(event, context):
    raise Exception("Received event: " + json.dumps(event, indent=2))
    