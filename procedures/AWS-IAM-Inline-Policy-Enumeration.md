---
id: 3d42b32c-c309-471c-be8b-3ad37c796910
name: AWS-IAM-Inline-Policy-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.568791+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Listing inline policies of our user]]'
  - aws
  - iam
  - discovery
commands:
  - '[[commands/aws-iam-list-user-policies]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-IAM-Inline-Policy-Enumeration

## Summary

This procedure enumerates all inline policies attached to a specific IAM user in an AWS account using the AWS CLI. It helps identify permissions granted directly to the user, which may reveal over-privileged configurations exploitable for privilege escalation or lateral movement in cloud environments.

## Description

Inline policies in AWS IAM are policies embedded directly into a user, group, or role, unlike managed policies that can be reused. This procedure queries the AWS IAM API to list these inline policies for a given user, providing insight into the user's effective permissions without needing to retrieve the full policy documents. It is useful during reconnaissance phases of red team engagements or audits to map access rights and spot misconfigurations, such as unintended administrative privileges. The technique relies on the `iam:ListUserPolicies` permission, which is often granted to users with read access to IAM. Execution requires configured AWS credentials with sufficient permissions and targets a specific IAM user by name.

## Requirements

1. Valid AWS access keys or IAM role with `iam:ListUserPolicies` permission.
2. AWS CLI installed and configured with credentials (via `aws configure` or environment variables).
3. Network access to AWS APIs (typically over HTTPS on port 443).
4. Knowledge of the target IAM user name.

## Defense

- Implement least privilege access by regularly auditing and removing unnecessary inline policies.
- Enable AWS CloudTrail logging for IAM API calls to detect enumeration attempts.
- Use IAM Access Analyzer to identify and alert on anomalous permission grants.
- Restrict `iam:ListUserPolicies` to administrative roles only and monitor its usage via AWS Config.

## Objectives

1. List all inline policies attached to the target IAM user.
2. Assess the scope of permissions to identify potential exploitation paths.
3. Validate user access levels for privilege escalation opportunities.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure AWS credentials are set up and test connectivity to avoid errors during enumeration.

Run `aws sts get-caller-identity` to confirm your identity and permissions.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> This command returns your AWS account, user ARN, and session details. If it fails with permission errors, update credentials.

### Step 2: Enumerate Inline Policies for the IAM User

**Context**: Query the IAM service to retrieve the list of inline policy names attached to the specified user. This reveals direct policy attachments without fetching policy details.

Execute the command with the target user name.

**Command** ([[commands/aws-iam-list-user-policies]]):
```bash
aws iam list-user-policies --user-name example_user
```

> Replace `example_user` with the actual IAM user name. The output is a JSON list of policy names. If no policies exist, it returns an empty list. Success is indicated by HTTP 200 response and policy names in the `PolicyNames` array.
