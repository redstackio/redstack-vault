---
id: 02811cc5-7880-4a15-8f54-e453e67e8862
type: command
executor: bash
data: aws lambda get-function --function-name $_FUNCTION_NAME
output: null
created_at: '2023-04-06T03:56:11.202142+00:00'
updated_at: '2023-04-10T20:20:12.620714+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - aws-cli
verified: true
validated: true
---

# aws-lambda-get-function

## Command

```bash
aws lambda get-function --function-name $_FUNCTION_NAME
```

## Description

This command retrieves the configuration and code details for a specific AWS Lambda function via the AWS CLI. It is used during cloud enumeration to gather metadata that can reveal misconfigurations or attack paths, such as execution roles or runtime environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | The name of the Lambda function to query (e.g., my-lambda-function). Must match exactly, case-sensitive. | Yes |
| --region (optional) | AWS region where the function is deployed (defaults to default region in config). | No |
| --profile (optional) | AWS profile to use if multiple configurations exist. | No |

## Examples

### Basic Usage

```bash
aws lambda get-function --function-name my-example-function
```

### Advanced Usage

```bash
aws lambda get-function --function-name my-example-function --region us-east-1 --profile attacker-profile
```

## Expected Output

A JSON object containing the function's details:

```json
{
  "Configuration": {
    "FunctionName": "my-example-function",
    "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-example-function",
    "Runtime": "python3.9",
    "Role": "arn:aws:iam::123456789012:role/lambda-execution-role",
    "Handler": "lambda_function.lambda_handler",
    "CodeSize": 1234,
    "Description": "Sample Lambda function",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2023-04-01T12:00:00.000+0000",
    "CodeSha256": "abc123...",
    "Version": "$LATEST",
    "Environment": {
      "Variables": {
        "KEY": "value"
      }
    },
    "VpcConfig": null
  },
  "Code": {
    "Location": "https://...",
    "RepositoryType": "..."
  }
}
```

Success is indicated by a 200 OK response with valid JSON; errors include ResourceNotFoundException if the function doesn't exist or AccessDeniedException if permissions are insufficient.

## Related

- [[procedures/AWS-Lambda-Function-Enumeration]]
