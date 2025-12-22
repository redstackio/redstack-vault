---
id: 945b6839-e0f8-4723-9e7e-bd96117573b8
name: curl-invoke-lambda-endpoint
type: command
executor: bash
data: curl "$_ENDPOINT_URL" -X GET
output: null
created_at: '2023-04-06T03:56:11.955520+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows (with curl)
tags:
  - cloud
  - aws
  - execution
verified: true
validated: true
---

# curl-invoke-lambda-endpoint

## Command

```bash
curl "$_ENDPOINT_URL" -X GET
```

## Description

This command uses curl to send an HTTP GET request to an AWS API Gateway endpoint, invoking the underlying Lambda function. It is used for remote execution in serverless environments, assuming the endpoint is publicly accessible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENDPOINT_URL | The full API Gateway URL (e.g., https://example.execute-api.region.amazonaws.com/stage/function) | Yes |
| -X GET | Specifies the HTTP method (use POST for payloads) | No (default GET) |

## Examples

### Basic Usage

```bash
curl "https://uj3948ie.execute-api.us-east-2.amazonaws.com/default/EXAMPLE" -X GET
```

### Advanced Usage with Payload

```bash
curl "https://uj3948ie.execute-api.us-east-2.amazonaws.com/default/EXAMPLE" -X POST -d '{"input":"test"}'
```

## Expected Output

A successful invocation returns the Lambda function's response, typically in JSON format, such as:

```json
{
  "statusCode": 200,
  "body": "Function executed successfully"
}
```

Errors may show 403 (unauthorized) or 502 (Lambda error).

## Related

- [[procedures/Invoke-AWS-Lambda-Function-via-API-Gateway]]
