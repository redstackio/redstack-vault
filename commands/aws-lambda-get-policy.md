---
type: command
executor: bash
data: >-
  aws lambda get-policy --function-name $_FUNCTION_NAME --profile $_PROFILE
  --region $_REGION
tags:
  - aws
  - lambda
  - policy
  - discovery
platforms:
  - AWS
verified: true
validated: true
---

# aws-lambda-get-policy

## Command

```bash
aws lambda get-policy --function-name $_FUNCTION_NAME --profile $_PROFILE --region $_REGION
```

## Description

This command retrieves the resource-based IAM policy attached to a specific AWS Lambda function. It is used during cloud reconnaissance to inspect permissions that could enable further exploitation, such as identifying invocable functions or cross-account access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --function-name $_FUNCTION_NAME | The name of the Lambda function (e.g., my-lambda-function) | Yes |
| --profile $_PROFILE | AWS CLI profile name containing credentials (e.g., default or custom-profile) | No (uses default if omitted) |
| --region $_REGION | AWS region where the function is deployed (e.g., us-east-1) | No (uses default if omitted) |

## Examples

### Basic Usage

```bash
aws lambda get-policy --function-name my-function --region us-east-1
```

### Advanced Usage

```bash
aws lambda get-policy --function-name prod-processor --profile attacker-profile --region eu-west-1 --qualifier $LATEST
```

> The --qualifier option (optional) specifies a version or alias; omit for $LATEST.

## Expected Output

Successful execution returns a JSON response with the policy details:

```json
{
  "Policy": "{\"Version\":\"2012-10-17\",\"Id\":\"default\",\"Statement\":[{\"Sid\":\"\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"lambda.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-1:123456789012:function:my-function\"}]}",
  "RevisionId": "abc123"
}
```

The Policy field is a JSON string containing IAM statements. Errors include AccessDeniedException if permissions are insufficient.

## Related

- [[procedures/List-AWS-Lambda-Function-Policy]] (procedure using this command)
- [[aws-lambda-list-functions]] (related command for enumerating functions)
