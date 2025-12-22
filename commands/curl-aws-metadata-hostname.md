---
id: e874d097-838c-4b49-82b8-562a8c40d5a2
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/meta-data/hostname'
output: null
created_at: '2023-04-06T03:56:38.437117+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - ssrf
  - metadata
verified: true
validated: true
---

# curl-aws-metadata-hostname

## Command

```bash
curl http://169.254.169.254/latest/meta-data/hostname
```

## Description

Gets the hostname of the AWS EC2 instance. Helps in identifying the environment during SSRF reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fetches hostname from metadata | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/hostname
```

## Expected Output

ip-10-0-1-100.ec2.internal

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
