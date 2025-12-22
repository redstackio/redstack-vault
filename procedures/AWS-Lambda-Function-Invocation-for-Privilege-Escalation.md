---
id: e78ebd3f-414a-40d4-9d54-e211a43eebed
name: AWS-Lambda-Function-Invocation-for-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.033250+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Invoke a lambda function]]'
  - '[[tags/Privilege Escalation]]'
commands:
  - '[[commands/aws-lambda-invoke-function]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-Lambda-Function-Invocation-for-Privilege-Escalation

## Summary

This procedure outlines how to invoke an AWS Lambda function using the AWS CLI to execute serverless code, potentially leading to privilege escalation if the function runs under a role with broader permissions than the invoker's IAM user or role. This technique exploits the trust in Lambda execution environments to perform unauthorized actions, such as accessing sensitive resources or data exfiltration.

## Description

AWS Lambda is a serverless compute service that allows code execution in response to events without managing servers. Attackers with limited permissions can invoke Lambda functions if they have the lambda:InvokeFunction permission, and if the function's execution role has elevated privileges (e.g., access to S3 buckets, EC2 instances, or other services), this can enable lateral movement or escalation. For example, an attacker might invoke a function that queries metadata services or performs API calls on behalf of the more privileged role. This procedure assumes the target environment is an AWS account where the attacker has initial foothold via compromised credentials. Success depends on the function's code and role permissions; always verify post-invocation effects like log entries in CloudWatch or changes in resources.

## Requirements

1. AWS CLI installed and configured with access keys or role assuming credentials that include lambda:InvokeFunction permission.
2. Knowledge of the target Lambda function name, ARN, or alias, and the AWS region where it is deployed.
3. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).
4. Optional: Payload data if the function expects input (e.g., JSON file for custom parameters).

## Defense

Defensive measures and detection strategies:

- Implement least privilege for IAM roles: Ensure Lambda execution roles have minimal permissions and monitor cross-service access.
- Enable AWS CloudTrail logging for Lambda invocations and review for anomalous calls (e.g., from unusual IPs or with unexpected payloads).
- Use AWS Config rules to alert on functions with overly permissive roles and implement resource policies to restrict invocation sources.
- Monitor CloudWatch Logs for Lambda executions, looking for suspicious code behavior or error patterns indicating abuse.

## Objectives

1. Successfully invoke a target Lambda function to execute its code.
2. Leverage the function's execution role for privilege escalation or unauthorized resource access.
3. Verify the invocation results and any resulting privilege gains (e.g., new API access).

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure your AWS CLI is properly set up and you have the necessary permissions to interact with Lambda services. This prevents errors during invocation and confirms your access level.

**Command** ([[commands/aws-configure-list]]):
```bash
aws configure list
```

> This command displays your current AWS configuration, including access key, secret key (masked), default region, and output format. If not configured, run `aws configure` to set credentials. Expected output includes active profile details without errors.

Next, test Lambda permissions by listing functions.

**Command** ([[commands/aws-lambda-list-functions]]):
```bash
aws lambda list-functions --region $_REGION
```

> Replace $_REGION with the target region (e.g., us-west-2). This lists available Lambda functions, confirming you have lambda:ListFunctions permission. If denied, escalation may require other paths. Expected output: JSON array of functions with names and ARNs.

### Step 2: Identify Target Lambda Function

**Context**: Select a Lambda function likely to provide escalation, such as one with an execution role permitting access to sensitive services (e.g., S3 read, EC2 describe). Use the list output to choose.

Review function details for role information.

**Command** ([[commands/aws-lambda-get-function]]):
```bash
aws lambda get-function --function-name $_FUNCTION_NAME --region $_REGION
```

> $_FUNCTION_NAME is the target function (e.g., myEscalationFunction). This retrieves configuration, including the execution role ARN. Expected output: JSON with Role field showing the IAM role; cross-reference in IAM to assess privileges.

### Step 3: Prepare Invocation Payload (If Needed)

**Context**: Some functions require input data. Prepare a JSON payload file if the function processes parameters, which could influence escalation (e.g., specifying a resource to access).

Create a sample payload file.

**Command** (using echo or editor):
```bash
echo '{"key": "value"}' > payload.json
```

> This creates a basic JSON file. Customize based on function expectations (e.g., for data exfiltration targets). Expected output: A valid JSON file verifiable with `cat payload.json`.

### Step 4: Invoke the Lambda Function

**Context**: Execute the function to run its code under the elevated role, potentially achieving escalation by performing actions the invoker couldn't directly.

**Command** ([[commands/aws-lambda-invoke-function]]):
```bash
aws lambda invoke --function-name $_FUNCTION_NAME --payload file://payload.json $_OUTPUT_FILE --region $_REGION
```

> $_FUNCTION_NAME is the function name, payload.json is optional input, $_OUTPUT_FILE is the response file (e.g., response.json), $_REGION is the AWS region. This synchronously invokes the function and saves the response. Expected output: The CLI returns the request ID; check $_OUTPUT_FILE for execution results (e.g., JSON with statusCode 200 and body).

### Step 5: Verify Escalation and Results

**Context**: Analyze the invocation response and check for privilege gains, such as new resource access or logs indicating successful unauthorized actions.

Review the output file and CloudWatch logs.

**Command** ([[commands/aws-lambda-get-log-events]]):
```bash
aws logs get-log-events --log-group-name /aws/lambda/$_FUNCTION_NAME --log-stream-name $_STREAM_NAME --region $_REGION
```

> $_STREAM_NAME from recent logs (use describe-log-streams first if needed). Expected output: Log events showing function execution details; look for evidence of escalated actions (e.g., S3 access logs).

If escalation succeeded, test new permissions (e.g., aws s3 ls s3://sensitive-bucket).
