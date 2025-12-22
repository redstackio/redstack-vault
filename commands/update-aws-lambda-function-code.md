---
type: command
executor: bash
data: >-
  aws lambda update-function-code --function-name $_FUNCTION_NAME --zip-file
  fileb://$_ZIP_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - lambda
  - persistence
verified: true
validated: true
---

# update-aws-lambda-function-code

## Command

```bash
aws lambda update-function-code --function-name $_FUNCTION_NAME --zip-file fileb://$_ZIP_FILE
```

## Description

This command updates the deployment package (code and dependencies) of an existing AWS Lambda function using a local ZIP file. It is used in persistence scenarios to inject malicious code, replacing the original handler without changing the function's configuration or triggers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | The name or ARN of the Lambda function to update | Yes |
| --zip-file fileb://$_ZIP_FILE | Path to the local ZIP file containing the code (use fileb:// prefix for binary files) | Yes |

## Examples

### Basic Usage

```bash
aws lambda update-function-code --function-name my-persistent-function --zip-file fileb://deployment.zip
```

### Advanced Usage

```bash
aws lambda update-function-code --function-name my-persistent-function --zip-file fileb://deployment.zip --publish
```

> The --publish flag creates a new version of the function.

## Expected Output

Successful execution returns JSON like:

```json
{
  "FunctionName": "my-persistent-function",
  "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-persistent-function",
  "LastModified": "2023-10-01T12:00:00.000+0000",
  "RevisionId": "abc123",
  "CodeSha256": "def456...",
  "CodeSize": 1024,
  "Signers": []
}
```

## Related

- [[procedures/aws-lambda-backdoor-persistence]]
- [[tools/aws-cli]]
