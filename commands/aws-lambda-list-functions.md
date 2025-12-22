---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: aws-lambda-list-functions
type: command
executor: bash
data: aws lambda list-functions --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud-aws
  - discovery
  - lambda
verified: true
validated: true
---

# aws-lambda-list-functions

## Command

```bash
aws lambda list-functions --region $_REGION
```

## Description

This command lists all AWS Lambda functions in the specified region, providing an overview of deployed serverless functions for discovery purposes in cloud assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_REGION | AWS region to query (e.g., us-east-1) | No (defaults to default region) |

## Examples

### Basic Usage

```bash
aws lambda list-functions --region us-east-1
```

### Advanced Usage

```bash
aws lambda list-functions --region us-east-1 --query 'Functions[].FunctionName' --output table
```

## Expected Output

```
{
    "Functions": [
        {
            "FunctionName": "my-lambda-function",
            "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-lambda-function",
            "Runtime": "python3.9",
            "Role": "arn:aws:iam::123456789012:role/lambda-execution-role",
            "Handler": "lambda_function.lambda_handler"
        }
    ]
}
```

## Related

- [[procedures/AWS-Lambda-Environment-Variable-Credential-Access]]
- [[commands/aws-lambda-get-function-configuration]]
