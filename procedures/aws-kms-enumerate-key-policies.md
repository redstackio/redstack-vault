---
id: cbec736a-0a71-4e33-9b40-cb0aca2b4193
name: aws-kms-enumerate-key-policies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.190393+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/KMS]]'
  - '[[tags/Policy Enumeration]]'
commands:
  - '[[commands/aws-kms-list-keys]]'
  - '[[commands/aws-kms-list-key-policies]]'
  - '[[commands/aws-kms-get-key-policy]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# aws-kms-enumerate-key-policies

## Summary

This procedure enumerates the key policies attached to AWS KMS (Key Management Service) keys within a target AWS account. By listing available keys, retrieving policy names, and fetching the full policy documents, attackers can identify misconfigurations such as overly permissive access controls that allow unauthorized use of encryption keys for data protection bypass or privilege escalation. Defenders can use this to audit and remediate policy weaknesses.

## Description

AWS KMS keys are used to encrypt and decrypt data across AWS services. Each key has an associated policy that defines who can use it and for what operations. This procedure leverages AWS CLI commands to discover these policies, revealing potential attack vectors like keys granting broad permissions to external principals or roles. It requires credentials with kms:ListKeys, kms:ListKeyPolicies, and kms:GetKeyPolicy permissions. In an offensive scenario, this helps map the encryption landscape; defensively, it supports compliance audits under frameworks like NIST or CIS AWS benchmarks. The process assumes the AWS CLI is configured with access to the target account via IAM roles, assumed roles, or direct credentials.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., via `aws configure` or environment variables) that have kms:ListKeys, kms:ListKeyPolicies, and kms:GetKeyPolicy permissions.
2. Network access to the AWS API endpoints for the target region (default: us-east-1).
3. Knowledge of the target AWS account or ability to assume a role with the required permissions.

## Defense

- Implement principle of least privilege by scoping KMS key policies to specific IAM users/roles and avoiding wildcard permissions like "*".
- Enable AWS CloudTrail logging for KMS API calls (e.g., ListKeyPolicies, GetKeyPolicy) and monitor for anomalous access patterns using Amazon GuardDuty or SIEM tools.
- Regularly audit KMS keys and policies using AWS Config rules or tools like Prowler to detect and alert on permissive configurations.
- Rotate credentials and use temporary security tokens via STS to limit exposure.

## Objectives

1. Identify all customer-managed KMS keys in the account.
2. List policy names attached to a specific key to understand access controls.
3. Retrieve and analyze full policy documents for misconfigurations like excessive permissions.
4. Gather intelligence on the target's encryption usage for further attacks like key compromise or data exfiltration.

## Instructions

### Step 1: List All KMS Keys

**Context**: Begin by enumerating all customer-managed KMS keys to identify targets for policy enumeration. This step provides the KeyId (ARN or alias) needed for subsequent commands. Without this, you cannot specify a key for policy listing.

**Command** ([[commands/aws-kms-list-keys]]):
```bash
aws kms list-keys --region $_REGION
```

> Run this in the target region to output a JSON list of keys. If no region is specified, it defaults to us-east-1. Review the KeyList array for KeyIds like "arn:aws:kms:us-east-1:123456789012:key/abc123". If the output is empty, no customer keys exist or permissions are insufficient.

### Step 2: List Policies Attached to a Specific Key

**Context**: Using a KeyId from Step 1, list the names of policies attached to that key. This reveals how many policies exist and their names (typically "default" for the primary policy), helping pinpoint keys with multiple or custom policies that may indicate misconfigurations.

**Command** ([[commands/aws-kms-list-key-policies]]):
```bash
aws kms list-key-policies --key-id $_KEY_ID --region $_REGION
```

> The command returns a JSON object with a PolicyNames array (e.g., ["default"]). If PolicyNames is empty, the key has no attached policies (unlikely for managed keys). Use jq for parsing: `aws kms list-key-policies ... | jq '.PolicyNames'`. Decision point: If multiple policies, prioritize "default" as it controls core access.

### Step 3: Retrieve Full Policy Details

**Context**: For each policy name from Step 2, fetch the complete policy document to inspect permissions. This JSON policy can be analyzed for statements allowing actions like kms:Decrypt or kms:GenerateDataKey to unauthorized principals, enabling attacks like data access or malware persistence.

**Command** ([[commands/aws-kms-get-key-policy]]):
```bash
aws kms get-key-policy --key-id $_KEY_ID --policy-name $_POLICY_NAME --region $_REGION
```

> Outputs JSON with the Policy field containing the IAM policy document. Look for loose conditions (e.g., no IP restrictions) or broad principals (e.g., "*"). Pipe to jq for readability: `... | jq '.Policy'`. If the policy grants excessive rights, note for escalation (e.g., if it allows admin roles). Success if policy is retrieved without AccessDenied errors.
