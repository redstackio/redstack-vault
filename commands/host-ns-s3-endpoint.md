---
data: host -t ns d326d3e45wj426.s3.ap-east-1.amazonaws.com
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.037Z'
id: de7e5713-2de0-4996-b032-3d532d4907d6
verified: false
validated: true
submitted: true
---
---

# host-ns-s3-endpoint

## Command

```bash
host -t ns d326d3e45wj426.s3.ap-east-1.amazonaws.com
```

## Description

Queries name server (NS) records for the specified S3 endpoint to identify aliases and authoritative name servers, revealing the bucket name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t ns | Record type: name server | Yes |
| d326d3e45wj426.s3.ap-east-1.amazonaws.com | Target S3 regional endpoint | Yes |

## Examples

### Basic Usage

```bash
host -t ns d326d3e45wj426.s3.ap-east-1.amazonaws.com
```

### Advanced Usage

```bash
host -t ns example.s3.us-east-1.amazonaws.com
```

## Expected Output

NS records: d326d3e45wj426.s3.ap-east-1.amazonaws.com is an alias for s3-r-w.ap-east-1.amazonaws.com, with AWS DNS servers listed.

## Related

- [[commands/dig-studio-redditinc-cname]]
- [[procedures/DNS-Enumeration-to-Identify-S3-Bucket]]
