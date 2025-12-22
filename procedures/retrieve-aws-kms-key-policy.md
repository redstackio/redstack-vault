---
id: b9484f0f-dfd6-499d-9b52-508f9cbe869f
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.433405+00:00'
updated_at: '2023-04-10T20:20:53.399175+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/KMS]]'
  - '[[tags/Policy Listing]]'
  - '[[tags/Discovery]]'
commands:
  - '[[commands/aws-kms-get-key-policy]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Retrieve AWS KMS Key Policy

## Summary

This procedure retrieves the full policy document for an AWS Key Management Service (KMS) key, revealing the permissions and principals (users, roles, or services) granted access to the key. It is useful in cloud environments for discovering encryption key access patterns, which can inform privilege escalation paths or identify opportunities for data exfiltration using compromised credentials.

## Description

AWS KMS manages encryption keys for securing data across AWS services. Key policies define who can use the keys for cryptographic operations like encrypt, decrypt, or sign. An attacker with limited AWS credentials (e.g., read access to KMS) can enumerate these policies to map out access controls, identify over-privileged principals, or find keys used in sensitive services like S3 or RDS. This technique is particularly valuable in lateral movement within AWS accounts, as it exposes the attack surface without requiring administrative privileges. The procedure uses the AWS CLI to query the policy in JSON format, allowing parsing for specific statements like Allow or Deny rules targeting IAM users, roles, or external accounts.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) with at least kms:GetKeyPolicy permission on the target key.
2. AWS CLI installed and accessible (version 2 recommended for full feature support).
3. Knowledge of the target KMS key ID or ARN (can be obtained via prior enumeration like aws kms list-keys).
4. Network access to AWS endpoints (no VPC-specific restrictions assumed).

## Defense

- Apply the principle of least privilege: Restrict kms:GetKeyPolicy to only necessary roles and monitor usage via AWS CloudTrail.
- Enable AWS Config rules to alert on changes to KMS key policies and implement guardrails to prevent overly permissive policies.
- Use AWS Organizations SCPs to limit KMS access across accounts and integrate with SIEM for anomaly detection in key policy queries.

## Objectives

1. Retrieve the complete JSON policy document for a specified KMS key.
2. Analyze the policy to identify principals with decrypt or manage permissions.
3. Uncover potential escalation vectors, such as keys accessible by service roles in other AWS services.

## Instructions

### Step 1: Identify the Target KMS Key

**Context**: Before retrieving the policy, ensure you have the key ID or ARN. If not known, enumerate available keys using aws kms list-keys (requires kms:ListKeys permission).

**Command** ([[commands/aws-kms-list-keys]]):
```bash
aws kms list-keys --region us-east-1
```

> This lists key IDs in the specified region. Select a key ID from the output (e.g., 1234abcd-12ab-34cd-56ef-1234567890ab) for the next step. Expected output is a JSON array of KeyList entries with KeyId and KeyArn.

### Step 2: Retrieve the Key Policy

**Context**: Use the AWS CLI to fetch the policy for the specific key. The default policy name is 'default', but custom names can be specified if applicable. This step requires kms:GetKeyPolicy permission and returns the policy as a JSON string that can be piped to jq for parsing.

**Command** ([[commands/aws-kms-get-key-policy]]):
```bash
aws kms get-key-policy --key-id $_KEY_ID --policy-name default --region $_REGION --output json | jq '.Policy'
```

> Replace $_KEY_ID with the actual key ID (e.g., 1234abcd-12ab-34cd-56ef-1234567890ab) and $_REGION with the AWS region (e.g., us-east-1). The command outputs the policy JSON, which includes Statement arrays detailing principals, actions (e.g., kms:Decrypt), and conditions. If successful, you'll see the full policy; errors indicate insufficient permissions or invalid key ID.
