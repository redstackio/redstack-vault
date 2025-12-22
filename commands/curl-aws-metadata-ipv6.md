---
id: 8fad935e-3660-4e75-8d0d-e497cf6aa612
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/meta-data/public-ipv6'
output: null
created_at: '2023-04-06T03:56:38.437266+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - ssrf
  - metadata
  - ipv6
verified: true
validated: true
---

# curl-aws-metadata-ipv6

## Command

```bash
curl http://169.254.169.254/latest/meta-data/public-ipv6
```

## Description

Fetches the public IPv6 address of the AWS EC2 instance if IPv6 is enabled. Aids in network mapping via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Retrieves public IPv6 | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/public-ipv6
```

## Expected Output

2001:db8::1

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
