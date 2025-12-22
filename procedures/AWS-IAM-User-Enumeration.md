---
id: f851d96b-db3f-4ee9-9633-20e7d9d75824
name: AWS-IAM-User-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.012455+00:00'
updated_at: '2023-04-10T20:20:23.921365+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/1. Enumerating IAM users]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Listing IAM Users]]'
  - aws
  - iam
  - enumeration
  - discovery
commands:
  - '[[commands/aws-iam-list-users]]'
platforms:
  - AWS
  - Cloud
tools: []
validated: true
---

# AWS-IAM-User-Enumeration

## Summary

This procedure enumerates all IAM users in an AWS account using the AWS CLI, providing details such as usernames, user IDs, and ARNs. It is useful for discovering user accounts during reconnaissance to identify potential targets for further attacks like password spraying or phishing.

## Description

AWS Identity and Access Management (IAM) controls access to AWS resources by managing users, groups, roles, and permissions. Enumerating IAM users reveals the structure of identities in the account, including active users who may have elevated privileges or access to sensitive resources like S3 buckets or EC2 instances. This technique is typically performed after obtaining valid AWS credentials with read access to IAM (e.g., via IAM:ListUsers permission). Attackers can use this information to map the environment, prioritize high-value targets, or prepare for lateral movement. The procedure relies on the AWS CLI for automation and can be extended with output parsing for larger-scale operations. Note that excessive API calls may trigger CloudTrail logging and alerts if monitoring is enabled.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with IAM permissions to list users (e.g., IAM:ListUsers policy).
2. AWS CLI installed and configured on the attacker's machine (version 2 recommended for better JSON handling).
3. Network access to AWS endpoints (no VPC restrictions blocking CLI traffic).
4. Optional: jq or similar tool for parsing JSON output if automating further.

## Defense

- Enable multi-factor authentication (MFA) for all IAM users and monitor for unauthorized access attempts.
- Use AWS CloudTrail to log IAM API calls and set up Amazon GuardDuty or CloudWatch alarms for suspicious ListUsers activity.
- Implement least-privilege policies: Restrict IAM:ListUsers to only necessary roles and regularly audit user permissions with IAM Access Analyzer.
- Rotate credentials frequently and use temporary credentials via STS for short-lived access.

## Objectives

1. Identify all IAM users in the target AWS account to map the identity landscape.
2. Gather user details (usernames, ARNs) for targeting in subsequent attacks like credential abuse or social engineering.
3. Verify the presence of privileged users (e.g., admins) to prioritize exploitation paths.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Before enumerating users, ensure your AWS CLI is properly configured with credentials that have the necessary IAM permissions. This step prevents authentication errors during execution.

Run `aws sts get-caller-identity` to confirm your identity and permissions.

> If the command succeeds and returns your account details without errors, proceed. If it fails with AccessDenied, update your credentials or attach the required policy.

### Step 2: Enumerate IAM Users

**Context**: Use the AWS CLI to query the IAM service for a list of all users. This retrieves essential metadata without requiring additional permissions beyond listing.

**Command** ([[commands/aws-iam-list-users]]):
```bash
aws iam list-users
```

> This command sends an API request to the IAM service and returns a JSON array of user objects. Each user includes fields like UserName, UserId, Arn, CreateDate, and Path. Success is indicated by a 200 OK response and a non-empty Users array. If no users exist or permissions are insufficient, it returns an empty list or error.

### Step 3: Parse and Review Output

**Context**: The raw JSON output can be large; parse it to extract actionable information like usernames for further reconnaissance.

Use jq to filter usernames:
```bash
aws iam list-users | jq '.Users[].UserName'
```

> Expected output is a list of usernames, e.g., ["admin", "developer", "service-account"]. Export to a file for scripting: `aws iam list-users --output text --query 'Users[].[UserName,Arn]' > iam_users.txt`. Review for patterns like admin or root-like names to identify high-value targets.
