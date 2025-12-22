---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.146895+00:00'
updated_at: '2023-04-10T20:19:49.153467+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing keys in KMS]]'
commands:
  - '[[commands/aws-kms-list-keys]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-KMS-Key-Enumeration

## Summary

This procedure uses the AWS CLI to enumerate and list all customer managed keys in AWS Key Management Service (KMS), revealing encryption keys that protect sensitive data across AWS services. It is useful in cloud penetration testing or red team operations to identify potential targets for further decryption or privilege escalation attacks.

## Description

AWS KMS is a managed service for creating and controlling encryption keys used to secure data in services like S3, EBS, and RDS. Enumerating KMS keys allows an attacker with compromised credentials to discover which keys exist, their IDs, creation dates, and descriptions, potentially exposing encrypted resources. This technique maps to MITRE ATT&CK's Cloud Service Discovery, as it involves querying cloud infrastructure to map the environment. In an attack scenario, this is often performed after initial credential compromise to assess the scope of accessible encrypted data. The procedure assumes the attacker has AWS credentials with at least kms:ListKeys permission and relies on the AWS CLI for interaction. Expected outcomes include a JSON list of keys, which can be parsed to identify high-value targets like keys protecting production databases.

## Requirements

1. Valid AWS credentials (access key and secret key) with kms:ListKeys permission or equivalent IAM policy allowing KMS key listing.
2. AWS CLI installed and configured with the credentials via `aws configure` or environment variables.
3. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).
4. Optional: Specify a region if targeting non-default (e.g., us-east-1).

## Defense

- Implement least privilege access: Restrict kms:ListKeys to only necessary roles and monitor usage via AWS CloudTrail.
- Enable AWS Config rules to alert on unauthorized KMS access attempts.
- Use AWS Organizations SCPs to deny listing actions in sensitive accounts.
- Monitor for anomalous API calls using Amazon GuardDuty or SIEM integration with CloudTrail logs.

## Objectives

1. Retrieve a complete list of KMS keys in the target AWS account.
2. Identify key metadata (ID, ARN, creation date, description) for potential follow-on decryption attacks.
3. Assess the encryption posture to discover sensitive data protected by these keys.

## Instructions

### Step 1: Configure AWS CLI if Needed

**Context**: Ensure the AWS CLI is set up with the compromised credentials to authenticate API calls. This step verifies connectivity and permissions before enumeration.

Run the configuration command if not already set:

**Command** ([[commands/aws-configure-credentials]]):
```bash
aws configure
```

> Enter the access key, secret key, default region, and output format (json) when prompted. Expected output: No errors, and subsequent `aws sts get-caller-identity` should return account details confirming valid credentials.

If credentials are set via environment variables, verify with:

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> Expected output: JSON with UserId, Account, and Arn confirming authenticated session.

### Step 2: Enumerate KMS Keys

**Context**: Directly query the KMS service to list all customer managed keys. This reveals the encryption infrastructure without needing additional tools.

**Command** ([[commands/aws-kms-list-keys]]):
```bash
aws kms list-keys --region $_REGION
```

> This command queries the KMS API and returns a JSON array of keys. Use --region to target specific regions if multi-region enumeration is needed. If successful, parse the output for KeyId and KeyArn to map keys to resources. Decision point: If no keys are returned, check permissions or try other regions; if permission denied, escalate privileges.
