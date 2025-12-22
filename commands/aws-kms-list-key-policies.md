---
id: c68089b0-9b03-45bd-8d67-78ab8e7bda66
name: aws-kms-list-key-policies
type: command
executor: bash
data: aws kms list-key-policies --key-id $_KEY_ID --region $_REGION
output: null
created_at: '2023-04-06T03:56:12.186324+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud-aws
  - kms
  - enumeration
  - policy
verified: true
validated: true
---

# aws-kms-list-key-policies

## Command

```bash
aws kms list-key-policies --key-id $_KEY_ID --region $_REGION
```

## Description

This command retrieves the names of policies attached to a specific KMS key, aiding in the discovery of access controls for encryption operations. Essential for identifying keys with custom or multiple policies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --key-id $_KEY_ID | KMS key ID or ARN (e.g., abc123 or arn:aws:kms:...) | Yes |
| --region $_REGION | AWS region (e.g., us-east-1) | No (defaults to config) |

## Examples

### Basic Usage

```bash
aws kms list-key-policies --key-id abc123
```

### With Region

```bash
aws kms list-key-policies --key-id arn:aws:kms:us-east-1:123456789012:key/abc123 --region us-east-1
```

## Expected Output

```json
{
    "PolicyNames": [
        "default"
    ]
}
```

Success shows a PolicyNames array with policy names like "default". Empty array means no policies (rare) or permission issues.

## Related

- [[commands/aws-kms-list-keys]]
- [[commands/aws-kms-get-key-policy]]
- [[procedures/aws-kms-enumerate-key-policies]]
