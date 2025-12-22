---
id: cmd-uuid-3
data: 'aws s3 rb s3://affirm-prod-www-cms█████████ --force'
tags:
  - cleanup
  - s3
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.708Z'
verified: false
validated: true
submitted: true
---
# aws-s3-rb-force

## Command

```bash
aws s3 rb s3://affirm-prod-www-cms█████████ --force
```

## Description

Recursively deletes the S3 bucket and all its contents forcefully after vulnerability demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rb | Remove bucket | Yes |
| --force | Forces deletion without confirmation | Yes |
| s3://bucket | Bucket URI | Yes |

## Examples

### Basic Usage

```bash
aws s3 rb s3://affirm-prod-www-cms█████████ --force
```

### Advanced Usage

```bash
aws s3 rb s3://affirm-prod-www-cms█████████ --force --region us-east-1
```

## Expected Output

delete: s3://affirm-prod-www-cms█████████/index.html
remove_bucket: affirm-prod-www-cms█████████

## Related

- [[Related Procedure|procedures/Claim-Dangling-S3-Bucket]]
