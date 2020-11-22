import json
import os


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "VersionNumber": os.environ.get("VersionNumber"),
            "LastCommitId": os.environ.get("LastCommitId"),
            "ApplicationName": os.environ.get("ApplicationName"),
        }),
    }
