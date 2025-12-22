---
type: command
executor: bash
data: nslookup $_IP_ADDRESS
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - dns
  - reconnaissance
verified: true
validated: true
---

# nslookup-reverse-dns-s3-ip

## Command

```bash
nslookup $_IP_ADDRESS
```

## Description

Conducts a reverse DNS lookup on an S3 bucket's IP address to determine the AWS region from the endpoint hostname, essential for targeting region-specific S3 operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IP_ADDRESS | The IP address of the S3 endpoint (e.g., 52.218.192.11) | Yes |

## Examples

### Basic Usage

```bash
nslookup 52.218.192.11
```

### Advanced Usage

```bash
nslookup -type=PTR $_IP_ADDRESS  # Explicit PTR query
```

## Expected Output

```
Non-authoritative answer:
11.192.218.52.in-addr.arpa name = s3-website-us-west-2.amazonaws.com.
```

The hostname reveals the region (e.g., us-west-2); parse it for use in AWS CLI.

## Related

- [[procedures/List-Files-in-S3-Bucket]]
- [[commands/dig-dns-lookup-s3-bucket-name]]
