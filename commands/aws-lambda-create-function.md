---
id: 3b6483f0-ee83-4579-94c9-d015de3540f1
name: aws-lambda-create-function
type: command
executor: bash
data: >-
  aws lambda create-function --function-name $_FUNCTION_NAME --runtime $_RUNTIME
  --role $_ROLE_ARN --handler $_HANDLER --code file://$_CODE_FILE
output: null
created_at: '2023-04-06T03:56:09.319203+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - lambda
  - persistence
verified: true
validated: true
---

# aws-lambda-create-function

## Command

```bash
aws lambda create-function --function-name $_FUNCTION_NAME --runtime $_RUNTIME --role $_ROLE_ARN --handler $_HANDLER --code file://$_CODE_FILE
```

## Description

Creates a new Lambda function for executing custom code, potentially malicious.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | Name of the function | Yes |
| --runtime $_RUNTIME | Runtime (e.g., python3.6) | Yes |
| --role $_ROLE_ARN | IAM role ARN | Yes |
| --handler $_HANDLER | Entry point | Yes |
| --code file://$_CODE_FILE | Path to code | Yes |

## Examples

### Basic Usage

```bash
aws lambda create-function --function-name my_function --runtime python3.6 --role arn:aws:iam::account:role/lambda_role --handler lambda_function.lambda_handler --code file://code.py
```

## Expected Output

Function ARN and details.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
