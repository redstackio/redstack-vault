---
id: cmd-002-s3cmd-upload-no-preserve
data: 's3cmd put file.txt s3://bucket/ --no-preserve'
tags:
  - s3
  - upload
  - mitigation
type: command
output: >-
  File 'file.txt' uploaded to 's3://bucket/file.txt' without metadata
  preservation
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.805Z'
verified: false
validated: true
submitted: true
---
# s3cmd-upload-no-preserve

## Command

```bash
s3cmd put file.txt s3://bucket/ --no-preserve
```

## Description

This command uploads a file to an S3 bucket using s3cmd while preventing the preservation of local file attributes (e.g., uname, gname, uid, gid, mode, timestamps, md5) in the object's metadata, mitigating information disclosure risks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `put` | Upload operation | Yes |
| `file.txt` | Local file to upload | Yes |
| `s3://bucket/` | Destination S3 path | Yes |
| `--no-preserve` | Avoid including local metadata in S3 object headers | Yes for mitigation |

## Examples

### Basic Usage

```bash
s3cmd put file.txt s3://mybucket/ --no-preserve
```

### Advanced Usage

```bash
s3cmd put --recursive dir/ s3://mybucket/ --no-preserve --acl-public
```

> Uploads a directory recursively without metadata and sets public ACL.

## Expected Output

Confirmation of upload without the x-amz-meta-s3cmd-attrs header containing sensitive info in subsequent HEAD requests.

## Related

- [[Related Procedure: Inspect-S3-Response-Headers-for-Metadata-Disclosure]]
