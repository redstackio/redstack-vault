---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - aws
  - lambda
  - policy-listing
  - discovery
  - cloud
commands:
  - '[[commands/aws-lambda-get-policy]]'
platforms:
  - AWS
tools: []
verified: true
validated: true
---

# List-AWS-Lambda-Function-Policy

## Summary

This procedure retrieves the resource-based policy attached to a specific AWS Lambda function using the AWS CLI. It allows attackers with sufficient permissions to inspect the function's execution role and resource policies, revealing granted permissions that can inform privilege escalation, lateral movement, or persistence strategies within an AWS environment.

## Description

In AWS, Lambda functions can have resource-based policies that define who or what can invoke the function and under what conditions. Listing these policies provides insight into the function's access rights, such as permissions to other AWS services (e.g., S3, DynamoDB). An attacker who has compromised credentials with lambda:GetPolicy permission can use this to map out the attack surface in a cloud environment. This is particularly useful after initial access via misconfigured IAM roles or during reconnaissance of serverless architectures. The procedure assumes AWS CLI v2 is installed and configured with appropriate credentials. Success reveals the policy in JSON format, including statements with actions, resources, and principals.

## Requirements

1. AWS CLI installed and accessible (version 2 recommended).
2. Valid AWS credentials with lambda:GetPolicy permission on the target function.
3. Knowledge of the Lambda function name, AWS region, and optional CLI profile.
4. Network access to AWS APIs (no direct VPC restrictions assumed).

## Defense

- Implement least privilege: Restrict lambda:GetPolicy to only necessary roles and monitor its usage via CloudTrail.
- Enable AWS CloudTrail logging for Lambda API calls and alert on anomalous policy retrievals from unexpected IPs or roles.
- Use IAM Access Analyzer to review and audit resource-based policies regularly for over-permissions.
- Rotate credentials frequently and use temporary credentials with short lifespans.

## Objectives

1. Retrieve the JSON policy document for a specified Lambda function.
2. Identify permissions granted to the function for potential exploitation paths.
3. Map out IAM principals and actions allowed on the function to support further attacks.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials that have access to the target Lambda function. This step confirms authentication and avoids errors during policy retrieval.

Run the AWS CLI configure list command to check your current profile and region settings.

**Command** ([[commands/aws-configure-list]]):
```bash
aws configure list
```

> This command displays the current configuration without making API calls. Expected output includes your default profile, region, and credential source. If credentials are missing or invalid, use `aws configure` to set them up. Why: Proper configuration prevents authentication failures in subsequent steps.

### Step 2: Retrieve the Lambda Function Policy

**Context**: Execute the core command to fetch the policy. Provide the function name, region, and profile as needed. This step directly accomplishes the objective by querying the AWS Lambda API.

**Command** ([[commands/aws-lambda-get-policy]]):
```bash
aws lambda get-policy --function-name $_FUNCTION_NAME --profile $_PROFILE --region $_REGION
```

> Replace placeholders with actual values (e.g., --function-name my-function --region us-east-1). The command sends a GET request to the Lambda service and returns the policy if accessible. Why: This reveals the policy statements, allowing analysis of permissions like invoke rights or cross-service access. If the function has no policy, it returns an empty or error response—verify the function exists first with `aws lambda get-function --function-name $_FUNCTION_NAME`.

### Step 3: Parse and Analyze the Output

**Context**: Review the JSON response for actionable insights, such as allowed actions (e.g., s3:GetObject) or principal ARNs. This step verifies success and extracts value for next attack phases.

Use jq (if installed) to format and filter the JSON output for easier reading.

**Command** ([[commands/jq-parse-json]]):
```bash
aws lambda get-policy --function-name $_FUNCTION_NAME --profile $_PROFILE --region $_REGION | jq ' .Policy '
```

> Expected: Formatted JSON showing the policy document with Statement arrays. Why: Parsing helps identify exploitable permissions quickly. If no jq, pipe to a file and open in a JSON viewer. Success criteria: Policy document contains Sid, Effect, Action, and Principal fields without access denied errors.
