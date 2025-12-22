---
id: 14f1f348-2f9a-46e6-a165-85ebff0b7e34
name: aws-kms-describe-key
type: command
executor: bash
data: aws kms describe-key --key-id $_KEY_ID
output: null
created_at: '2023-04-06T03:56:12.162938+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - kms
verified: true
validated: true
---

# aws-kms-describe-key

## Command

```bash
aws kms describe-key --key-id $_KEY_ID
```

## Description

This command retrieves detailed metadata about a specific AWS KMS customer master key (CMK) using the AWS CLI. It is used during cloud discovery to enumerate key properties without performing encryption or decryption operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --key-id | The unique identifier or ARN of the KMS key to describe (e.g., key ID like 1234abcd-12ab-34cd-56ef-1234567890ab or full ARN) | Yes |
| --region | AWS region where the key resides (e.g., us-east-1); defaults to configured region | No |
| --output | Output format (json, text, table); defaults to json | No |

## Examples

### Basic Usage

Describe a key by ID:
```bash
aws kms describe-key --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
```

### Advanced Usage

Describe a key with text output in a specific region:
```bash
aws kms describe-key --key-id arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab --region us-west-2 --output text
```

## Expected Output

Successful execution returns a JSON object containing the KeyMetadata. Example:
```json
{
  "KeyMetadata": {
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "Description": "Example key",
    "KeyManager": "aws",
    "KeyState": "Enabled",
    "CreationDate": "2023-01-01T12:00:00+00:00",
    "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
    "Origin": "AWS_KMS",
    "KeyUsage": "ENCRYPT_DECRYPT",
    "Arn": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  }
}
```
Errors include InvalidKeyIdException if the key doesn't exist or AccessDeniedException if permissions are lacking.

## Related

- [[procedures/Describe-AWS-KMS-Key]] (procedure that uses this command)
- [[tools/aws-cli]] (tool)
