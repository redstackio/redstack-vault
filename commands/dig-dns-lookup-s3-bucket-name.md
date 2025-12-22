---
type: command
executor: bash
data: dig $_BUCKET_NAME
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - dns
  - reconnaissance
verified: true
validated: true
---

# dig-dns-lookup-s3-bucket-name

## Command

```bash
dig $_BUCKET_NAME
```

## Description

Performs a DNS A record lookup for an S3 bucket name to resolve its IP address, which is the first step in identifying the bucket's AWS region during cloud reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BUCKET_NAME | The name of the S3 bucket to resolve (e.g., flaws.cloud) | Yes |

## Examples

### Basic Usage

```bash
dig flaws.cloud
```

### Advanced Usage

```bash
dig +short flaws.cloud  # Short output, just IP
```

## Expected Output

```
;; ANSWER SECTION:
flaws.cloud.    5    IN    A    52.218.192.11
```

An IP address indicates the bucket endpoint; no answer suggests it doesn't exist or is not public.

## Related

- [[procedures/List-Files-in-S3-Bucket]]
- [[commands/nslookup-reverse-dns-s3-ip]]
