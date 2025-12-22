---
id: 17a46eb3-f11b-46cf-b301-24edb5f5134d
name: AWS-IAM-Attach-Inline-Policy-to-User
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.544455+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Account Manipulation/User|T1098.001 - Account Manipulation:
    User]]
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - cloud-aws
  - iam-policy-attachment
  - privilege-escalation
commands:
  - '[[commands/aws-iam-put-user-policy]]'
  - '[[commands/aws-iam-list-user-policies]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-IAM-Attach-Inline-Policy-to-User

## Summary

This procedure demonstrates how to attach an inline policy to an existing AWS IAM user using the AWS CLI, allowing an attacker with initial access to escalate privileges by granting additional permissions such as full administrative access. This technique is commonly used for persistence and further lateral movement in compromised AWS environments, enabling actions like resource creation or data exfiltration without relying on existing roles.

## Description

In an AWS environment, IAM users can have inline policies attached directly to them via the AWS API or CLI, bypassing some role-based restrictions. An attacker who has obtained credentials for an IAM user with 'iam:PutUserPolicy' permissions can craft a malicious policy document (e.g., granting 'AdministratorAccess') and attach it inline. This grants the user elevated permissions immediately, which can persist even if the original credentials are rotated, as long as the policy remains attached. The technique targets AWS IAM services and requires authenticated API access. It is effective in scenarios where the attacker has low-privileged console or CLI access and aims to expand their foothold. Detection relies on CloudTrail logging of IAM policy changes, and mitigation involves monitoring for unexpected policy attachments.

## Requirements

1. Valid AWS credentials with 'iam:PutUserPolicy' permission (obtained via initial access like compromised keys or SSO).
2. AWS CLI installed and configured with the target account's access keys.
3. A prepared JSON policy document file granting desired permissions (e.g., full admin access).
4. Network access to AWS API endpoints (no specific ports beyond standard HTTPS/443).

## Defense

- Enable AWS CloudTrail for IAM API calls and monitor for 'PutUserPolicy' events using CloudWatch or SIEM tools.
- Implement least-privilege principles: Restrict 'iam:PutUserPolicy' to trusted admin roles only.
- Use IAM Access Analyzer to detect anomalous policy attachments and enable MFA for all IAM users.
- Regularly audit attached policies with 'iam:ListUserPolicies' and automate alerts for high-privilege grants.

## Objectives

1. Escalate privileges for the targeted IAM user to perform restricted actions.
2. Establish persistence by embedding elevated permissions directly in the user profile.
3. Enable further exploitation, such as creating backdoor users or accessing sensitive resources.

## Instructions

### Step 1: Prepare the Inline Policy Document

**Context**: Create a JSON file defining the malicious policy, such as granting full AdministratorAccess. This step ensures the policy grants the necessary permissions without relying on managed policies.

Use a text editor or echo command to create the file. For example, here's a sample admin policy:

[[codes/AWS-IAM-Administrator-Access-Policy-JSON]]

Save it as `AdminPolicy.json` in your working directory.

**Expected Output**: A valid JSON file with policy statements, verifiable by opening the file or using `cat AdminPolicy.json`.

> If the JSON is invalid, the subsequent attachment will fail with a parsing error.

### Step 2: Attach the Inline Policy to the IAM User

**Context**: Use the AWS CLI to attach the prepared policy to the target IAM user. This grants the permissions defined in the JSON immediately upon successful execution.

**Command** ([[commands/aws-iam-put-user-policy]]):
```bash
aws iam put-user-policy --user-name $_USER_NAME --policy-name $_POLICY_NAME --policy-document file://$_POLICY_DOCUMENT_PATH
```

Replace placeholders: `$_USER_NAME` with the target user (e.g., 'compromised-user'), `$_POLICY_NAME` with a non-suspicious name (e.g., 'CustomReadOnlyPolicy'), and `$_POLICY_DOCUMENT_PATH` with the path to your JSON (e.g., 'AdminPolicy.json').

**Expected Output**: A JSON response indicating success, such as:
```json
{
    "PolicyName": "CustomReadOnlyPolicy"
}
```
No errors like 'AccessDenied' or 'NoSuchEntity'.

> This command updates the user's permissions inline; test by attempting a privileged action post-attachment.

### Step 3: Verify the Policy Attachment

**Context**: Confirm the policy was attached correctly by listing the user's inline policies. This validates success and allows checking for any issues before proceeding to exploitation.

**Command** ([[commands/aws-iam-list-user-policies]]):
```bash
aws iam list-user-policies --user-name $_USER_NAME
```

Replace `$_USER_NAME` with the target user name.

**Expected Output**: A JSON list including your attached policy:
```json
{
    "PolicyNames": [
        "CustomReadOnlyPolicy"
    ]
}
```
If empty or missing, re-run Step 2.

> Decision point: If the policy isn't listed, check credentials or permissions; otherwise, proceed to use the elevated access for further actions like [[procedures/AWS-Create-Backdoor-User]].
