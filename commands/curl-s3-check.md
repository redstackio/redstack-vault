---
id: cmd-uuid-3
data: 'curl -I https://healthyhackathon.khanacademy.org.s3.amazonaws.com'
tags:
  - http-probe
  - s3
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.823Z'
verified: false
validated: true
submitted: true
---
# curl-s3-check

## Command

```bash
 curl -I https://healthyhackathon.khanacademy.org.s3.amazonaws.com
```

## Description

Sends a HEAD request to an S3 endpoint to check for bucket existence, expecting errors for deleted buckets in takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only | Yes |
| `URL` | S3 bucket endpoint | Yes |

## Examples

### Basic Usage

```bash
 curl -I https://healthyhackathon.khanacademy.org.s3.amazonaws.com
```

### Advanced Usage

```bash
 curl -v https://hackweek.khanacademy.org.s3.amazonaws.com
```

## Expected Output

HTTP 404 with XML body containing <Code>NoSuchBucket</Code>, indicating the bucket is gone.

## Related

- [[Related Procedure: Verify-Non-Existent-S3-Buckets]]
