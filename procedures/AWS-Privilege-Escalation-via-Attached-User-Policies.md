---
id: dd09db1a-6e60-4497-b8ba-cfb77685c6b4
name: AWS-Privilege-Escalation-via-Attached-User-Policies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.459044+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/Study Case]]'
  - aws
  - iam
  - discovery
commands:
  - '[[commands/aws-iam-list-attached-user-policies]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# AWS-Privilege-Escalation-via-Attached-User-Policies

## Summary

This procedure exploits misconfigured AWS IAM policies attached to users by first discovering them through API calls, identifying overly permissive attachments, and then modifying them to escalate privileges. It allows attackers with initial AWS credentials to gain broader access to resources like S3 buckets or other services, enabling data exfiltration or further compromise.

## Description

In AWS environments, IAM policies define permissions for users, groups, or roles. If an attacker has compromised credentials with limited permissions, they can use the IAM API to list attached user policies and identify misconfigurations, such as policies granting excessive rights (e.g., full S3 access). With permissions to update policies (often via attached admin-like policies), the attacker can then attach or modify these policies to their own user or role, escalating privileges. This technique targets environments where least privilege is not enforced, common in cloud setups with shared credentials. The process assumes the attacker has AWS CLI access and valid keys, and it maps to discovery of cloud infrastructure followed by privilege manipulation.

## Requirements

1. Valid AWS access key ID and secret access key for a user with IAM read permissions (e.g., iam:ListAttachedUserPolicies).
2. AWS CLI installed and configured with the credentials (via ~/.aws/credentials or environment variables).
3. Network access to AWS APIs (no VPC endpoints blocking IAM calls).
4. Optional: Named profile for multi-account management.

## Defense

Defensive measures and detection strategies:

- Enforce least privilege by scoping IAM policies tightly to required resources and actions.
- Monitor IAM API calls (e.g., ListAttachedUserPolicies, AttachUserPolicy) using AWS CloudTrail and set alerts for unusual policy modifications.
- Enable MFA for all IAM users and use roles instead of long-lived access keys.
- Regularly audit attached policies with tools like IAM Access Analyzer to detect overly permissive configurations.

## Objectives

1. Identify attached IAM policies on target users to uncover potential privilege escalation paths.
2. Modify or attach discovered policies to escalate access to sensitive AWS resources.
3. Gain unauthorized control over services like S3, EC2, or RDS for data access or lateral movement.

## Instructions

### Step 1: Configure AWS CLI with Compromised Credentials

**Context**: Before querying IAM, ensure the AWS CLI is set up with the compromised access keys. This step authenticates your session to the target AWS account. If using a named profile, create or update the ~/.aws/credentials file.

**Why**: Proper configuration prevents authentication errors and allows seamless API calls.

Instructions: Run the following to set credentials (replace placeholders with actual values). Note: This is manual setup; in automated scenarios, use environment variables like AWS_ACCESS_KEY_ID.

```bash
aws configure set aws_access_key_id $_ACCESS_KEY_ID --profile $_PROFILE_NAME
aws configure set aws_secret_access_key $_SECRET_ACCESS_KEY --profile $_PROFILE_NAME
aws configure set default.region $_REGION --profile $_PROFILE_NAME
```

**Expected Output**: No output if successful; verify with `aws sts get-caller-identity --profile $_PROFILE_NAME` which should return the user ARN and account ID.

**Success Indicators**:
- `get-caller-identity` returns the expected user and account without errors.
- No credential validation failures.

### Step 2: List Attached Policies for Target User

**Context**: Use the IAM API to enumerate policies attached directly to a specific user. This reveals permissions that could be exploited if the user has update rights.

**Command** ([[commands/aws-iam-list-attached-user-policies]]):

```bash
aws iam list-attached-user-policies --user-name $_USER_NAME --profile $_PROFILE_NAME
```

**Why**: This discovers managed policies (AWS or customer-managed) attached to the user, highlighting misconfigurations like admin access. Review the output for policies with broad actions (e.g., "*" on S3).

**Expected Output**:

```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "example-policy",
            "PolicyArn": "arn:aws:iam::aws:policy/example-policy"
        }
    ]
}
```
A list of policy ARNs; empty array if no policies attached.

**Success Indicators**:
- JSON response with AttachedPolicies array populated.
- Policy ARNs visible for further inspection (e.g., via `aws iam get-policy --policy-arn $_ARN`).

### Step 3: Analyze and Modify Policy for Escalation

**Context**: Inspect the listed policies for exploitable permissions. If the current user has iam:AttachUserPolicy or iam:UpdateUserPolicy permissions (often via an existing policy), modify or reattach to escalate.

**Why**: Direct modification grants additional rights, such as s3:* for data access. This step assumes partial write access; if not, chain with other escalation vectors.

Instructions: First, retrieve policy details:

```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id v1 --profile $_PROFILE_NAME
```

Then, if permitted, attach to your user (replace $_TARGET_USER with attacker's user):

```bash
aws iam attach-user-policy --user-name $_TARGET_USER --policy-arn $_POLICY_ARN --profile $_PROFILE_NAME
```

For inline policies, use update commands (requires knowing the policy document).

**Expected Output**: For attach: No output on success; error if insufficient perms. For get-policy-version: JSON with Statement array showing permissions.

**Success Indicators**:
- Policy details show broad permissions (e.g., Allow on s3:*).
- Attach succeeds without AccessDenied errors.
- Verify escalation with `aws sts get-caller-identity` and test new actions (e.g., `aws s3 ls`).

### Step 4: Verify Escalated Access

**Context**: Test the new permissions to confirm escalation, such as listing S3 buckets or other resources.

**Why**: Validates the attack's success and identifies further opportunities.

Instructions: Attempt a privileged action based on the policy, e.g.,

```bash
aws s3 ls --profile $_PROFILE_NAME
```

**Expected Output**: List of S3 buckets if escalated; previously denied actions now succeed.

**Success Indicators**:
- Access to previously restricted resources.
- No permission errors on test commands.
