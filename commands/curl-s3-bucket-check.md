---
id: cmd-uuid-curl-s3-check
data: 'curl https://bucket-name.s3.amazonaws.com'
tags:
  - http
  - cloud
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.824Z'
verified: false
validated: true
submitted: true
---
# curl-s3-bucket-check

## Command

```bash
curl https://bucket-name.s3.amazonaws.com
```

## Description

Probes an AWS S3 bucket endpoint to check for usage or vulnerability status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://bucket-name.s3.amazonaws.com` | S3 bucket URL | Yes |

## Examples

### Basic Usage

```bash
curl https://dangling-bucket.s3.amazonaws.com
```

### Advanced Usage

```bash
curl -v https://bucket.s3.amazonaws.com/test
```

## Expected Output

XML error: '<Error><Code>NoSuchBucket</Code></Error>' for vulnerable buckets.

## Related

- [[Related Procedure]]
