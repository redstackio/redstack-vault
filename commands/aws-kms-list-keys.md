---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: aws-kms-list-keys
type: command
executor: bash
data: aws kms list-keys --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - cloud-aws
  - kms
  - enumeration
verified: true
validated: true
---

# aws-kms-list-keys

## Command

```bash
aws kms list-keys --region $_REGION
```

## Description

This command lists all customer-managed KMS keys in the specified AWS region, providing KeyIds needed for further enumeration like policy listing. Use it during initial discovery of encryption resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_REGION | AWS region (e.g., us-east-1) | No (defaults to config) |

## Examples

### Basic Usage

```bash
aws kms list-keys
```

### With Specific Region

```bash
aws kms list-keys --region us-west-2
```

## Expected Output

```json
{
    "Keys": [
        {
            "KeyArn": "arn:aws:kms:us-east-1:123456789012:key/abc123",
            "KeyId": "abc123"
        }
    ]
}
```

A successful run returns a Keys array with ARNs and IDs. Empty array indicates no keys or insufficient permissions (e.g., AccessDenied).

## Related

- [[commands/aws-kms-list-key-policies]]
- [[procedures/aws-kms-enumerate-key-policies]]
