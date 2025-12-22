---
type: command
executor: bash
data: >-
  aws kms decrypt --ciphertext-blob fileb://$_CIPHERTEXT_FILE --output text
  --query Plaintext
output: null
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tags:
  - kms
  - decrypt
  - aws-cli
verified: true
validated: true
---

# aws-kms-decrypt-ciphertext-blob

## Command

```bash
aws kms decrypt --ciphertext-blob fileb://$_CIPHERTEXT_FILE --output text --query Plaintext
```

## Description

This command uses the AWS CLI to decrypt a ciphertext blob stored in a file using AWS KMS. It requires IAM permissions for kms:Decrypt and outputs the plaintext in base64 format, suitable for exfiltrating sensitive data like credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --ciphertext-blob fileb://$_CIPHERTEXT_FILE | Path to the binary file containing the encrypted ciphertext blob | Yes |
| --output text | Formats the output as plain text (JSON by default) | No |
| --query Plaintext | JMESPath query to extract only the plaintext field from the response | No |

## Examples

### Basic Usage

```bash
aws kms decrypt --ciphertext-blob fileb://encrypted-secret.bin --output text --query Plaintext
```

### Piped to Decode

```bash
aws kms decrypt --ciphertext-blob fileb://encrypted-secret.bin --output text --query Plaintext | base64 -d > secret.txt
```

## Expected Output

A base64-encoded string representing the decrypted plaintext:
```
AQIDBAUGBwgJCgsMDQ4PEA== (example base64)
```
If successful, no errors; failures include AccessDeniedException if permissions are insufficient.

## Related

- [[procedures/AWS-KMS-Decrypt-Exfiltration]]
- [[commands/aws-sts-get-caller-identity]] (for permission checks)
