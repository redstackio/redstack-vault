---
id: f66c317d-6c2a-4663-ad83-3c6d08321cea
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/meta-data/'
output: null
created_at: '2023-04-06T03:56:38.436941+00:00'
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

# curl-aws-metadata-root

## Command

```bash
curl http://169.254.169.254/latest/meta-data/
```

## Description

Lists all available metadata categories at the root of the AWS IMDS. Use this to enumerate endpoints before targeting specific data in SSRF attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Queries the root metadata path | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/
```

## Expected Output

ami-id
ami-launch-index
ami-manifest-deregistration-term
...

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
- [[commands/curl-aws-metadata-id]]
