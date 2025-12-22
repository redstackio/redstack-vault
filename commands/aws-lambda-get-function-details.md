---
type: command
executor: bash
data: aws lambda get-function --function-name $_FUNCTION_NAME
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - AWS
tags:
  - aws
  - lambda
  - discovery
verified: true
validated: true
---

# aws-lambda-get-function-details

## Command

```bash
aws lambda get-function --function-name $_FUNCTION_NAME
```

## Description

This command queries the AWS Lambda service to retrieve configuration and metadata for a specific function. It is used during cloud reconnaissance to understand function setup without executing code, helping identify targets for further attacks like invocation or code extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | The name of the Lambda function to query (e.g., my-app-handler) | Yes |
| --region | AWS region where the function is deployed (default: us-east-1) | No |
| --profile | AWS CLI profile name if using multiple configurations | No |
| --output json | Format for output (json, text, table; default json) | No |

## Examples

### Basic Usage

```bash
aws lambda get-function --function-name prod-webhook
```

### With Region Specification

```bash
aws lambda get-function --function-name dev-processor --region us-west-2
```

### JSON Output Parsing

```bash
aws lambda get-function --function-name test-function --output json | jq '.Code.Size'
```

## Expected Output

Successful execution returns a JSON object with sections like Configuration and Code:

```json
{
  "Configuration": {
    "FunctionName": "my-lambda-function",
    "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-lambda-function",
    "Runtime": "python3.9",
    "Role": "arn:aws:iam::123456789012:role/lambda-role",
    "Handler": "index.handler",
    "CodeSize": 12345,
    "MemorySize": 128,
    "Timeout": 30,
    "LastModified": "2023-09-01T12:00:00.000+0000"
  },
  "Code": {
    "Location": "https://...",
    "RepositoryType": "...",
    "CodeSha256": "...",
    "CodeSize": 12345,
    "LastModified": "2023-09-01T12:00:00.000+0000"
  }
}
```

Errors include "AccessDeniedException" for permission issues or "ResourceNotFoundException" if the function doesn't exist.

## Related

- [[procedures/Enumerate-AWS-Lambda-Function-Details]]
- [[tools/AWS-CLI]]
