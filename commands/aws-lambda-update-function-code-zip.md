---
id: 6e6dc58f-ec8f-4bb5-b083-1b59d05eff31
name: aws-lambda-update-function-code-zip
type: command
executor: bash
data: >-
  aws lambda update-function-code --function-name $_FUNCTION_NAME --zip-file
  fileb://$_ZIP_FILE
output: null
created_at: '2023-04-06T03:56:09.318915+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - lambda
verified: true
validated: true
---

# aws-lambda-update-function-code-zip

## Command

```bash
aws lambda update-function-code --function-name $_FUNCTION_NAME --zip-file fileb://$_ZIP_FILE
```

## Description

Updates a Lambda function's code from a ZIP file for injecting malicious payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | Target function | Yes |
| --zip-file fileb://$_ZIP_FILE | Path to ZIP (base64 encoded) | Yes |

## Examples

### Basic Usage

```bash
aws lambda update-function-code --function-name target_function --zip-file fileb://code.zip
```

## Expected Output

Function update confirmation.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
