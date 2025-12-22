---
id: 0afef758-6950-4090-bd40-5c60b3aa0d10
name: AWS-KMS-Key-Policy-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.212170+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Getting full information about a policy]]'
commands:
  - '[[commands/aws-kms-get-key-policy]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-KMS-Key-Policy-Enumeration

## Summary

The AWS KMS Key Policy Enumeration procedure retrieves the resource-based policy document attached to a customer managed AWS Key Management Service (KMS) key. This allows identification of permissions, principals, and conditions in the policy, which can reveal misconfigurations such as overly permissive access to external accounts or services, aiding in further discovery of AWS resources and potential privilege escalation paths.

## Description

In an AWS environment, KMS keys are used to encrypt and decrypt data across services like S3, RDS, and EBS. The key policy is a JSON document that defines who can use the key and under what conditions. Enumerating this policy is a discovery technique that helps attackers map access controls, identify weak permissions (e.g., allowing root access or cross-account usage), and discover related resources. This procedure assumes the attacker has valid AWS credentials with kms:GetKeyPolicy permission and uses the AWS CLI to query the policy. It is typically performed after initial access to an AWS account, such as via compromised IAM credentials, to assess encryption key management security.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_DEFAULT_REGION) with at least kms:GetKeyPolicy permission on the target key.
2. AWS CLI installed and accessible (version 2 recommended for full feature support).
3. Knowledge of the target KMS key ID or ARN (can be obtained via prior enumeration like aws kms list-keys).
4. Network access to AWS APIs (no direct VPC restrictions assumed).

## Defense

Defensive measures and detection strategies:

- Implement least privilege: Restrict kms:GetKeyPolicy to only necessary roles and monitor for anomalous calls via AWS CloudTrail.
- Enable AWS Config rules to alert on overly permissive KMS policies (e.g., allowing external principals).
- Use AWS KMS key policies that deny actions from untrusted accounts and require MFA for administrative changes.
- Monitor CloudTrail logs for GetKeyPolicy API calls from unexpected IPs or users, and integrate with SIEM for anomaly detection.

## Objectives

1. Retrieve the complete JSON policy document for a specified KMS key.
2. Analyze the policy for weaknesses, such as broad Allow statements or discoverable resource dependencies.
3. Support broader cloud resource discovery by identifying encrypted services tied to the key.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Before retrieving the policy, ensure your AWS CLI is properly configured with credentials that have the necessary permissions. This step prevents authentication errors and confirms access to the KMS service.

If not already configured, set up credentials using environment variables or the aws configure command. Test basic access with a simple KMS list-keys call to verify permissions.

**Command** ([[commands/aws-kms-list-keys]]):
```bash
aws kms list-keys --region $_AWS_REGION
```

> This command lists available KMS keys in the account. If it succeeds without permission errors, proceed. Expected output is a JSON array of key metadata, confirming kms:ListKeys permission (a prerequisite for targeting specific keys).

If you encounter AccessDenied, adjust your IAM policy to include kms:GetKeyPolicy on the target key.

### Step 2: Identify the Target KMS Key ID

**Context**: You need the key ID or ARN of the KMS key to enumerate its policy. If unknown, use a discovery command to list keys and select one (e.g., a customer-managed key used for sensitive data).

Use the list-keys command from Step 1 to obtain the KeyId (e.g., '1234abcd-12ab-34cd-56ef-1234567890ab'). Note customer-managed keys (not AWS-managed) as they support custom policies.

Decision point: If no keys are listed or access is denied, this procedure cannot proceed—escalate privileges or target another account.

### Step 3: Retrieve the KMS Key Policy

**Context**: Execute the core command to fetch the policy document. The default policy name for KMS keys is 'default', but custom names can be used if applicable. This reveals the full policy JSON, including statements, principals, and actions.

**Command** ([[commands/aws-kms-get-key-policy]]):
```bash
aws kms get-key-policy --key-id $_KEY_ID --policy-name $_POLICY_NAME --region $_AWS_REGION
```

> Replace $_KEY_ID with the key ID from Step 2 (e.g., '1234abcd-12ab-34cd-56ef-1234567890ab') and $_POLICY_NAME with 'default' for the primary key policy. The --region flag ensures the correct AWS region is queried. Expected output is a JSON object with a 'Policy' field containing the base64-encoded policy string; decode it (e.g., via base64 -d or jq) to view the readable JSON policy document showing permissions like "Effect": "Allow", "Principal", and "Action": "kms:*".

### Step 4: Analyze the Retrieved Policy

**Context**: Parse and review the policy for actionable insights. Look for misconfigurations like allowing * principals or references to other ARNs.

Save the output to a file for analysis:
```bash
echo '$_POLICY_STRING' | base64 -d > key_policy.json
```

Use jq to query: jq '.Policy' key_policy.json | base64 -d | jq '.' to pretty-print. Identify weaknesses such as cross-account access or missing Deny statements.

Decision point: If the policy is empty or defaults to strict AWS-managed, target another key; otherwise, use findings for further attacks like key rotation bypass or data decryption.
