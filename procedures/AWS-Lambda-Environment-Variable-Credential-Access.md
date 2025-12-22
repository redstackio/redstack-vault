---
id: b0393ab5-a3e2-4544-89f7-ed59ade44058
name: AWS-Lambda-Environment-Variable-Credential-Access
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.603944+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
tags:
  - cloud-aws
  - credential-access
  - lambda
  - environment-variables
commands:
  - '[[commands/aws-lambda-list-functions]]'
  - '[[commands/aws-lambda-get-function-configuration]]'
  - '[[commands/jq-select-environment-variables]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
  - '[[tools/jq]]'
validated: true
---

# AWS-Lambda-Environment-Variable-Credential-Access

## Summary

This procedure retrieves the configuration of an AWS Lambda function, including its environment variables, using the AWS CLI. Environment variables in Lambda functions may contain sensitive credentials or API keys, allowing an attacker with sufficient IAM permissions to extract them for further privilege escalation or lateral movement in the AWS environment.

## Description

AWS Lambda is a serverless computing service where functions execute in response to events without managing underlying infrastructure. Each Lambda function has an execution role with IAM permissions and can include environment variables for configuration. If these variables store secrets (e.g., database credentials, API tokens), an attacker who has compromised an AWS account with read access to Lambda (via lambda:GetFunction permission) can query the function's configuration to dump these variables. This technique is useful in cloud penetration testing to identify misconfigurations where secrets are not rotated or stored securely, such as in AWS Secrets Manager. The procedure assumes the attacker has AWS CLI access with appropriate credentials and focuses on the us-east-1 region by default, but it can be adapted.

## Requirements

1. AWS CLI installed and configured with access keys or role assuming lambda:GetFunction and lambda:ListFunctions permissions.
2. Knowledge of the AWS region where the Lambda function is deployed (default: us-east-1).
3. Target Lambda function name; if unknown, listing permissions are needed.
4. jq installed for parsing JSON output.

## Defense

- Avoid storing sensitive data in Lambda environment variables; use AWS Secrets Manager, Systems Manager Parameter Store, or IAM roles instead.
- Implement least-privilege IAM policies: restrict lambda:GetFunction to trusted roles only.
- Enable AWS CloudTrail for API logging to monitor Lambda configuration queries.
- Regularly audit and rotate any unavoidable secrets in environment variables.
- Use AWS Config rules to detect functions with sensitive env vars.

## Objectives

1. Identify target Lambda functions in the account.
2. Retrieve the detailed configuration, including environment variables.
3. Extract and review variables for sensitive credentials.
4. Use discovered credentials to access other AWS resources if applicable.

## Instructions

### Step 1: List Available Lambda Functions

**Context**: If the target function name is unknown, enumerate all Lambda functions in the region to identify potential targets. This step discovers the attack surface by listing functions that may contain sensitive configurations.

**Command** ([[commands/aws-lambda-list-functions]]):
```bash
aws lambda list-functions --region $_REGION
```

> This command queries the AWS Lambda service for a list of functions. Review the output JSON for FunctionName fields to select a target. If no functions appear, verify permissions or try a different region.

### Step 2: Retrieve Function Configuration

**Context**: Once a function is identified, fetch its configuration details, which include environment variables, runtime, handler, and role ARN. This is the core step for accessing potential credentials stored in env vars.

**Command** ([[commands/aws-lambda-get-function-configuration]]):
```bash
aws lambda get-function-configuration --function-name $_FUNCTION_NAME --region $_REGION
```

> The output is a JSON object with a Configuration section. Look for the Environment key, which maps variable names to values. Success is indicated by a 200 OK response and presence of the Environment object; if access denied, escalate IAM reconnaissance.

### Step 3: Extract Environment Variables

**Context**: Parse the JSON output from Step 2 to isolate the environment variables, making it easier to scan for secrets like API keys (e.g., patterns matching AWS_ACCESS_KEY_ID or custom tokens). This step verifies if sensitive data is exposed.

**Command** ([[commands/jq-select-environment-variables]]):
```bash
echo '$_JSON_OUTPUT' | jq '."Environment"."Variables"'
```

> Pipe the JSON from the previous command into jq. If Environment.Variables exists, it outputs a key-value object; if absent or null, no env vars are set. Manually inspect values for base64-encoded or plain-text secrets, and test them with tools like aws sts get-caller-identity.
