---
id: cmd-uuid-3
data: 'curl -o downloaded.txt "https://bucket.s3.amazonaws.com/key"'
tags:
  - http
  - get
  - s3
type: command
output: Downloaded file content
executor: bash
platforms:
  - Cloud (AWS)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.029Z'
verified: false
validated: true
submitted: true
---
# curl-download-from-s3

## Command

```bash
curl -o downloaded.txt "https://bucket.s3.amazonaws.com/key"
```

## Description

Downloads an object from S3 to verify upload success and size.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o downloaded.txt` | Output file | Yes |
| URL | S3 object URL | Yes |

## Examples

### Basic Usage

```bash
curl -o file.txt "https://s3.../key"
```

### Advanced Usage

```bash
curl -o output.bin "https://bucket.s3.amazonaws.com/key?signed-get-params"
ls -lh output.bin
```

## Expected Output

File saved; use ls -lh to check size > limit.

## Related

- [[Related Procedure]]
