import json
import boto3
import os
import base64
from urllib.parse import unquote, unquote_to_bytes

AWS_REGION = os.environ.get('REGION')
AWS_ACCOUNT = os.environ.get('ACCOUNT')
WORKER_LAMBDA_NAME = os.environ.get('WORKER_LAMBDA')
BONUS_LAMBDA_NAME = os.environ.get('BONUS_LAMBDA')
REQUEST_LAMBDA_NAME = os.environ.get('REQUEST_LAMBDA')

FUNCTION_ARN = f'arn:aws:lambda:{AWS_REGION}:{AWS_ACCOUNT}:function:'


def base64_encoder(body):
    decoded_data = base64.b64decode(body)
    decoded_data = unquote_to_bytes(decoded_data).decode(encoding='utf-8', errors='replace')

    if decoded_data.startswith('token'):
        items_list = list()
        for item in decoded_data.split('&'):
            item = tuple(item.split('='))
            items_list.append(item)
        body = dict(items_list)

        return body

    elif decoded_data.startswith('payload'):
        body = json.loads(decoded_data.split('=', 1)[1])

        return body


def resolve_function_name(lambda_to_invoke):
    if lambda_to_invoke == 'worker':
        lambda_name = WORKER_LAMBDA_NAME
    elif lambda_to_invoke == 'request':
        lambda_name = REQUEST_LAMBDA_NAME
    else:
        lambda_name = BONUS_LAMBDA_NAME

    function_name = FUNCTION_ARN + lambda_name

    return function_name


def invoke_lambda(function_name, data):
    client = boto3.client('lambda')

    client.invoke(
        FunctionName=function_name,
        InvocationType='Event',
        Payload=json.dumps(data)
    )


def invoke_request_response_lambda(function_name, data):
    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(data)
    )

    return response
