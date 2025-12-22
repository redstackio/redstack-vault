---
id: b2bf6e88-9993-45bd-b689-722f24f867fb
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/meta-data/placement/region'
output: null
created_at: '2023-04-06T03:56:38.437199+00:00'
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

# curl-aws-metadata-region

## Command

```bash
curl http://169.254.169.254/latest/meta-data/placement/region
```

## Description

Retrieves the AWS region where the EC2 instance is running. Useful for targeting region-specific resources in SSRF attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Queries placement region | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/placement/region
```

## Expected Output

us-east-1

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
