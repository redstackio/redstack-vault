---
id: 239bd5a7-e0d9-4978-a867-86a54c68bb94
name: curl-ec2-basic-metadata
type: command
executor: bash
data: 'curl "http://169.254.169.254/latest/meta-data/"'
output: null
created_at: '2023-04-06T03:55:53.744763+00:00'
updated_at: '2023-04-06T03:55:53.763748+00:00'
platforms:
  - AWS
  - Linux
tags:
  - ssrf
  - metadata
verified: true
validated: true
---

# curl-ec2-basic-metadata

## Command

```bash
curl "http://169.254.169.254/latest/meta-data/"
```

## Description

This command fetches the root EC2 instance metadata endpoint, listing available metadata categories. Use it via SSRF payloads to enumerate internal instance details without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses default HTTP GET to the metadata IP | Yes |

## Examples

### Basic Usage

```bash
curl "http://169.254.169.254/latest/meta-data/"
```

### With Output to File

```bash
curl "http://169.254.169.254/latest/meta-data/" > metadata_list.txt
```

## Expected Output

Plain text list of paths:

```
ami-id
ami-launch-index
ami-manifest-deregistration-term
block-device-mapping/
...
iam/security-credentials/
instance-id
...
```

## Related

- [[procedures/Exfiltrate-AWS-S3-Data-via-EC2-SSRF]]
- [[commands/curl-ec2-iam-credentials]]
