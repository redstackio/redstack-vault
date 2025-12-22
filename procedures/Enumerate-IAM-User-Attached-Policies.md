---
id: 4f97ebd4-9e5c-4546-b210-e4885b850a41
name: Enumerate-IAM-User-Attached-Policies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.062479+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - iam-enumeration
  - aws-cloud
  - user-policies
commands:
  - '[[commands/aws-iam-list-attached-user-policies]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-IAM-User-Attached-Policies

## Summary

This procedure uses the AWS CLI to enumerate the managed policies attached to a specific IAM user, providing insights into the user's permissions and access levels within the AWS environment. It is useful during reconnaissance to map out privilege structures and identify high-value targets with excessive permissions.

## Description

In AWS Identity and Access Management (IAM), users can have inline policies or attached managed policies that define their access to resources. Enumerating attached managed policies reveals the scope of permissions granted to a user, such as read/write access to S3 buckets, EC2 instances, or other services. This technique is commonly employed in cloud penetration testing or red team engagements to discover over-privileged accounts. The procedure relies on the `aws iam list-attached-user-policies` command, which queries the IAM service and returns a JSON list of attached policies, including ARNs and policy names. Success depends on having sufficient IAM permissions (e.g., iam:ListAttachedUserPolicies) for the target user. This maps to MITRE ATT&CK's Cloud Service Discovery tactic, as it involves probing cloud configurations to understand the environment.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least `iam:ListAttachedUserPolicies` permission for the target user.
2. AWS CLI installed and configured with the appropriate profile (e.g., via `aws configure`).
3. Network access to AWS endpoints (no VPC restrictions blocking IAM API calls).
4. Knowledge of the target IAM username.

## Defense

- Implement the principle of least privilege by regularly auditing and minimizing attached policies to only necessary permissions.
- Enable AWS CloudTrail logging for IAM actions to detect unauthorized enumeration attempts.
- Use IAM Access Analyzer to identify and alert on unexpected access patterns or permissions.
- Restrict IAM list permissions to administrative roles only and monitor for anomalous API calls via AWS GuardDuty.

## Objectives

1. Retrieve a list of managed policies attached to the specified IAM user.
2. Analyze the policies to determine the user's effective permissions and potential attack paths.
3. Identify users with broad access for further targeting in reconnaissance.

## Instructions

### Step 1: List Attached Policies for the Target User

**Context**: This step queries the AWS IAM service to fetch all managed policies attached to the specified user. The command returns a JSON response detailing policy ARNs, names, and attachment status, allowing you to assess the user's access scope. Ensure your AWS CLI is authenticated with credentials that can perform this action; if the user has no attached policies, the response will be an empty list.

**Command** ([[commands/aws-iam-list-attached-user-policies]]):
```bash
aws iam list-attached-user-policies --user-name $_USERNAME
```

> Replace `$_USERNAME` with the target IAM username (e.g., `john.doe`). The command authenticates via your current AWS profile and sends an API request to IAM. If successful, it outputs JSON with policy details. Parse the output using `jq` for easier reading, such as `| jq '.AttachedPolicies[].PolicyName'`. If you lack permissions, you'll receive an AccessDenied error.

### Step 2: Verify and Analyze Output

**Context**: Review the returned policies to understand access levels. For each policy, note the ARN to fetch further details if needed (e.g., via `aws iam get-policy-version`). This helps chain to other discovery techniques, like listing group policies or role assumptions.

**Command** ([[commands/aws-iam-list-attached-user-policies]]):
```bash
aws iam list-attached-user-policies --user-name $_USERNAME | jq '.AttachedPolicies[] | {PolicyName: .PolicyName, PolicyArn: .PolicyArn}'
```

> This enhanced invocation uses `jq` to filter key fields. Expected to show policy names and ARNs, indicating permissions like `AdministratorAccess` (high risk) or custom policies (analyze further).
