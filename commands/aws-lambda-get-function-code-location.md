---
id: fd8d17b7-8628-492c-afba-ff51f2f6e1c6
name: aws-lambda-get-function-code-location
type: command
executor: bash
data: >-
  aws lambda get-function --function-name "$_FUNCTION_NAME" --query
  'Code.Location' --output text --profile $_PROFILE --region $_REGION
output: null
created_at: '2023-04-06T03:56:09.663059+00:00'
updated_at: '2023-04-10T20:19:52.665195+00:00'
platforms:
  - Linux
  - AWS
tags:
  - aws
  - lambda
  - code-location
verified: true
validated: true
---

# aws-lambda-get-function-code-location

## Command

```bash
aws lambda get-function --function-name "$_FUNCTION_NAME" --query 'Code.Location' --output text --profile $_PROFILE --region $_REGION
```

## Description

This command retrieves the presigned S3 URL for the code package of a specific AWS Lambda function. It uses JMESPath querying to extract only the location, useful for scripting downloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name "$_FUNCTION_NAME" | Name of the target Lambda function | Yes |
| --query 'Code.Location' | JMESPath query to extract the code URL | Yes |
| --output text | Output as plain text (the URL) | Yes |
| --profile $_PROFILE | AWS CLI profile name | Yes |
| --region $_REGION | AWS region | No |

## Examples

### Basic Usage

```bash
aws lambda get-function --function-name "my-function" --query 'Code.Location' --output text --profile uploadcreds
```

### With Region

```bash
aws lambda get-function --function-name "my-function" --query 'Code.Location' --output text --profile uploadcreds --region us-east-1
```

## Expected Output

```
https://prod-3-east-us-1.s3.us-east-1.amazonaws.com/snapshots/uuid.zip?X-Amz-...
```
A single line with a presigned HTTPS URL to the ZIP file. Errors include "Function not found" if the name is invalid.

## Related

- [[procedures/AWS-Lambda-Function-Code-Extraction]]
- [[commands/aws-lambda-list-functions]]
