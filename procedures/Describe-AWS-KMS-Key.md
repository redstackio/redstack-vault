---
id: 9d4daff2-4a8f-4354-b022-99ecbe54e898
name: Describe-AWS-KMS-Key
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.166856+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/KMS]]'
commands:
  - '[[commands/aws-kms-describe-key]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Describe-AWS-KMS-Key

## Summary

This procedure uses the AWS CLI to describe a specific AWS Key Management Service (KMS) customer master key (CMK), retrieving detailed information such as its ARN, state, creation date, description, key usage, and policy. It is useful in red team engagements for enumerating cloud resources to identify keys potentially protecting sensitive data, enabling further targeting of encryption configurations.

## Description

In an AWS environment, KMS keys are used to encrypt and decrypt data across services like S3, EBS, and RDS. An attacker with compromised credentials or IAM role can use this procedure to gather metadata about a specific KMS key without decrypting data directly. This discovery step helps assess the key's role in the infrastructure, such as whether it is enabled, its origin (AWS-managed or customer-managed), and associated policies that might reveal access patterns. The procedure requires AWS CLI access with kms:DescribeKey permissions and is typically part of broader cloud enumeration to map encryption dependencies. Success provides JSON output that can be parsed for key details, aiding in planning attacks like key policy manipulation or data exfiltration attempts.

## Requirements

1. AWS CLI installed and configured with credentials having kms:DescribeKey permission on the target key.
2. Valid AWS access key ID and secret access key (or assumed role) for the target account.
3. Network access to AWS endpoints (no VPC endpoints required for standard usage).
4. Knowledge of the target KMS key ID or ARN.

## Defense

- Implement least-privilege IAM policies to restrict kms:DescribeKey actions to necessary roles only.
- Enable AWS CloudTrail logging for KMS API calls and monitor for anomalous DescribeKey requests from unexpected IPs or users.
- Use AWS Config rules to audit KMS key policies and alert on changes or excessive permissions.
- Rotate KMS keys periodically and disable unused ones to limit enumeration value.

## Objectives

1. Retrieve detailed metadata about a specific AWS KMS key to understand its configuration and usage.
2. Identify the key's state, origin, and policy to assess potential attack vectors in the cloud environment.
3. Support broader discovery of encryption dependencies for targeted post-exploitation.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials that have access to the target KMS key. This step confirms authentication before executing the describe command, preventing permission errors.

If not already configured, use `aws configure` to set your access key, secret key, region, and output format. Test with a simple command like `aws sts get-caller-identity` to verify permissions.

**Expected Output**: JSON response showing your AWS account details and role.

### Step 2: Describe the Target KMS Key

**Context**: Execute the AWS KMS describe-key command to fetch information about the specified CMK. This reveals critical details like the key's state (e.g., Enabled or Disabled), creation date, usage (ENCRYPT_DECRYPT or SIGN_VERIFY), and ARN, which can indicate if the key protects sensitive resources.

**Command** ([[commands/aws-kms-describe-key]]):
```bash
aws kms describe-key --key-id $_KEY_ID
```

> Replace $_KEY_ID with the actual key ID (e.g., 1234abcd-12ab-34cd-56ef-1234567890ab) or full ARN (e.g., arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab). The command outputs a JSON structure with KeyMetadata including KeyId, KeyState, CreationDate, KeyUsage, and more. If the key does not exist or permissions are insufficient, it returns an error like AccessDeniedException or NotFoundException.

**Expected Output**: JSON object with key details, for example:
```json
{
  "KeyMetadata": {
    "AWSAccountId": "123456789012",
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "Description": "My key",
    "KeyManager": "aws",
    "KeyState": "Enabled",
    "CreationDate": "2023-01-01T00:00:00.000Z",
    "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
    "Origin": "AWS_KMS",
    "KeyUsage": "ENCRYPT_DECRYPT",
    "Arn": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  }
}
```

### Step 3: Parse and Analyze Output

**Context**: Review the JSON output to extract actionable intelligence, such as checking if the key is enabled and its usage type. This step involves manual inspection or piping to jq for filtering, helping decide next actions like attempting to list key policies or grants.

Use jq to filter specific fields:
```bash
aws kms describe-key --key-id $_KEY_ID | jq '.KeyMetadata.KeyState'
```

**Expected Output**: Filtered value, e.g., "Enabled". If the key is disabled or pending deletion, it may indicate recent administrative changes worth investigating further.
