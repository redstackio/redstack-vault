---
id: bb6c440e-3dec-48ee-96e5-e58d17fa101c
name: Enumerate-AWS-Managed-Policies-for-IAM-User
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.648345+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - aws-iam-policy-enumeration
  - cloud-aws
  - discovery
  - persistence
commands:
  - '[[commands/aws-iam-list-attached-user-policies]]'
platforms:
  - AWS
tools: []
validated: true
---

# Enumerate-AWS-Managed-Policies-for-IAM-User

## Summary

This procedure enumerates all managed policies attached to a specific IAM user in an AWS environment, helping identify overly permissive policies that could enable privilege escalation or persistence. It uses the AWS CLI to query attached policies, revealing potential excessive privileges such as AdministratorAccess, which attackers can exploit after initial access to an AWS account.

## Description

In AWS Identity and Access Management (IAM), managed policies define permissions for users, groups, or roles. Attackers with valid credentials to an AWS account often enumerate these policies to discover hidden privileges, such as access to S3 buckets, EC2 instances, or other resources. This technique is part of post-compromise discovery, allowing escalation by assuming roles or using discovered permissions. The procedure assumes the attacker has AWS CLI configured with credentials (e.g., via access keys or assumed role) and focuses on AWS-managed policies, though it also lists customer-managed ones. Success reveals policy ARNs and names, which can be further inspected for exploitation opportunities like lateral movement or data exfiltration.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., access key ID and secret access key) that have at least iam:ListAttachedUserPolicies permission.
2. Network access to AWS APIs (no VPC endpoints required unless in a private subnet).
3. Knowledge of the target IAM user name.
4. Bash-compatible shell environment (Linux, macOS, or Windows with Git Bash).

## Defense

- Implement least privilege principle: Assign only necessary policies to IAM users and regularly audit attachments using AWS IAM Access Analyzer.
- Enable AWS CloudTrail logging for IAM API calls to detect enumeration attempts (look for ListAttachedUserPolicies events).
- Use IAM policy conditions to restrict actions based on source IP or MFA, and monitor for anomalous credential usage via AWS GuardDuty.
- Rotate credentials frequently and enforce MFA for all IAM users with console access.

## Objectives

1. List all managed and customer policies attached to a target IAM user.
2. Identify permissive policies (e.g., those granting full administrative access) for potential exploitation.
3. Support persistence by documenting privileges for future reference in a compromise scenario.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS credentials are active and have the required permissions to avoid authentication errors during enumeration.

Run `aws sts get-caller-identity` to confirm your identity and permissions.

**Expected Output**: JSON response showing Account, UserId, and Arn if successful.

### Step 2: Enumerate Attached Policies

**Context**: Query AWS IAM for policies attached to the target user, capturing both AWS-managed and customer-managed policies to assess privilege levels.

**Command** ([[commands/aws-iam-list-attached-user-policies]]):
```bash
aws iam list-attached-user-policies --user-name $_TARGET_USER
```

This command retrieves a list of policy attachments. Review the output for policy names like "AdministratorAccess" or "ReadOnlyAccess", which indicate potential escalation paths. If no policies are attached, the response will be an empty list.

**Expected Output**:
```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        },
        {
            "PolicyName": "AmazonS3ReadOnlyAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
        }
    ]
}
```

### Step 3: Analyze Policy Details

**Context**: For each discovered policy, fetch its document to understand exact permissions, helping decide on next actions like resource access or role assumption.

Use `aws iam get-policy-version` for each PolicyArn from Step 2.

**Command** (follow-up, not a separate command doc):
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id v1
```

**Expected Output**: JSON policy document detailing allowed actions (e.g., "s3:*" for full S3 access), which can be parsed for exploitable permissions.

**Success Indicators**:
- Policies listed without permission denied errors.
- Identification of high-privilege policies like full admin access.
