---
id: f18affd9-0bd0-4e61-9e1d-b71afa7a4173
name: Enumerate-AWS-IAM-User-ARNS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.890520+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/ARN]]'
  - '[[tags/Cloud - AWS]]'
commands:
  - '[[commands/aws-iam-list-users]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-IAM-User-ARNS

## Summary

This procedure enumerates all IAM users in an AWS account and extracts their Amazon Resource Names (ARNs), which uniquely identify users for access control and policy enforcement. It uses the AWS CLI to query the IAM service, helping attackers map user accounts for targeted privilege escalation or credential abuse in cloud environments.

## Description

AWS Identity and Access Management (IAM) users are assigned unique ARNs in the format `arn:aws:iam::ACCOUNT_ID:user/USERNAME`, used across AWS services for permissions and resource access. Enumerating these ARNs reveals the structure of the IAM user base, including administrative or service accounts that could be exploited. This technique is useful in post-compromise scenarios where an attacker has obtained valid AWS credentials, allowing discovery of potential pivot points without alerting monitoring if permissions are limited. The procedure assumes access to the AWS CLI configured with credentials that have `iam:ListUsers` permission.

## Requirements

1. AWS CLI installed and configured with access keys or role assuming credentials that have `iam:ListUsers` permission.
2. Network access to AWS endpoints (no VPC endpoints required for IAM).
3. Basic knowledge of AWS account structure and ARN formats.

## Defense

- Enable AWS CloudTrail logging for IAM API calls and monitor for `ListUsers` actions from unexpected sources.
- Implement least-privilege access: Restrict `iam:ListUsers` to only necessary roles and audit permissions regularly.
- Use AWS Organizations with Service Control Policies (SCPs) to limit IAM enumeration across accounts.

## Objectives

1. Retrieve a list of all IAM users in the target AWS account.
2. Extract and format user ARNs for use in subsequent attacks like policy manipulation or credential targeting.
3. Identify high-value users (e.g., admins) based on names or attached policies.

## Instructions

### Step 1: Configure AWS CLI Credentials

**Context**: Ensure the AWS CLI is set up with credentials that allow IAM listing. This step verifies authentication before enumeration to avoid errors.

Use the AWS CLI to test credentials:

**Command** ([[commands/aws-configure-test]]):
```bash
aws sts get-caller-identity
```

> This command returns the current identity details. If successful, it confirms valid credentials without errors like "Unable to locate credentials."

### Step 2: List IAM Users and Extract ARNs

**Context**: Query the IAM service to retrieve all users and their ARNs. This is the core enumeration step, providing a complete inventory for further analysis.

**Command** ([[commands/aws-iam-list-users]]):
```bash
aws iam list-users --query 'Users[].{UserName:UserName,ARN:Arn}' --output table
```

> The `--query` flag filters output to usernames and ARNs only, while `--output table` formats it readably. Expected output is a table listing users like:
>
> | UserName | ARN                          |
> |----------|------------------------------|
> | admin    | arn:aws:iam::123456789012:user/admin |
> | devuser  | arn:aws:iam::123456789012:user/devuser |
>
> Success is indicated by a populated table without permission denied errors. Pipe to a file for scripting: `aws iam list-users --query 'Users[].Arn' --output text > arns.txt`.
