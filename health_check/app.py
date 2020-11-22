import json

# import requests


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "All systems are go",
            # "location": ip.text.replace("\n", "")
        }),
    }
