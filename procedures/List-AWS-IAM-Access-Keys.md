---
id: 2eb27abd-568b-4c19-bab0-c77d94b50be9
name: List-AWS-IAM-Access-Keys
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:29.013247+00:00'
updated_at: '2023-05-25T20:04:30.747758+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
commands:
  - '[[commands/aws-iam-list-all-access-keys]]'
  - '[[commands/aws-iam-list-access-keys-for-user]]'
  - '[[commands/aws-iam-list-ssh-public-keys-for-user]]'
platforms:
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# List-AWS-IAM-Access-Keys

## Summary

This procedure enumerates IAM access keys associated with AWS accounts, including all access keys in the account, keys specific to a user, and SSH public keys for a user. It is useful during cloud reconnaissance to identify active credentials, potential credential reuse, or exposed keys that could lead to further compromise.

## Description

In AWS environments, IAM access keys provide programmatic access to services and are a common vector for unauthorized access if not properly managed. This procedure uses the AWS CLI to query IAM for access keys, revealing details like key status (Active/Inactive), creation date, and user association. It helps attackers or red teamers discover valid credentials for lateral movement or privilege escalation. The technique aligns with account discovery by listing credentials without requiring elevated privileges beyond read access to IAM. Prerequisites include configured AWS credentials with iam:ListAccessKeys permission.

## Requirements

1. AWS CLI installed and configured with access keys or role assuming iam:ListAccessKeys, iam:ListSSHPublicKeys permissions.
2. Network access to AWS API endpoints (no VPC restrictions blocking IAM calls).
3. Target AWS account with IAM users configured.

## Defense

- Enable AWS CloudTrail logging for IAM API calls to detect enumeration attempts.
- Implement least privilege: Restrict iam:ListAccessKeys to admin roles only.
- Rotate access keys regularly and monitor for inactive keys via AWS Config rules.
- Use IAM Access Analyzer to identify unused or external access.

## Objectives

1. Identify all active IAM access keys in the account to assess credential exposure.
2. Retrieve user-specific access keys for targeted enumeration.
3. List SSH public keys to discover alternative access methods like EC2 key pairs.
4. Expected outcome: JSON output listing keys with metadata for further analysis or cracking if hashes are involved.

## Instructions

### Step 1: List All Access Keys in the Account

**Context**: This step retrieves a list of all IAM access keys across the account, including their status and associated users. It provides an overview of credential distribution and helps identify potentially compromised or unused keys.

**Command** ([[commands/aws-iam-list-all-access-keys]]):
```bash
aws iam list-access-keys
```

> This command queries the IAM service for all access keys. Run it in a terminal with AWS CLI configured. If successful, it returns a JSON array of AccessKeyMetadata objects. Review the 'Status' field to identify active keys for potential exploitation.

### Step 2: List Access Keys for a Specific IAM User

**Context**: Narrow down to a specific user's access keys to check for personal credentials, which might be more easily exploitable if the user has elevated permissions. This is useful after identifying high-value users from prior enumeration.

**Command** ([[commands/aws-iam-list-access-keys-for-user]]):
```bash
aws iam list-access-keys --user-name $AWS_IAM_USER
```

> Replace $AWS_IAM_USER with the target username (e.g., 'admin-user'). This filters the query to that user. Expected output is a JSON response with the user's access keys. If no keys exist, it returns an empty list—indicating reliance on console access or roles.

### Step 3: List SSH Public Keys for a Specific User

**Context**: SSH keys provide direct server access and can be used for persistence. Listing them reveals if users have uploaded public keys for EC2 instances, potentially allowing keypair hijacking or lateral movement.

**Command** ([[commands/aws-iam-list-ssh-public-keys-for-user]]):
```bash
aws iam list-ssh-public-keys --user-name $AWS_IAM_USER
```

> Use the same $AWS_IAM_USER variable. This command lists SSH public keys uploaded to the user's IAM profile. Output includes key fingerprints and upload dates. Active keys can be retrieved separately for analysis or reuse.
