---
id: dfc9356f-b097-46d2-93ff-2a3b12b3318f
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/dynamic/instance-identity/document'
output: null
created_at: '2023-04-06T03:56:38.436894+00:00'
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

# curl-aws-metadata-json

## Command

```bash
curl http://169.254.169.254/latest/dynamic/instance-identity/document
```

## Description

Fetches a JSON document containing identity and metadata for the AWS EC2 instance, including account ID, instance ID, region, and more. Ideal for comprehensive reconnaissance via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses default IMDS path for identity document | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/dynamic/instance-identity/document
```

## Expected Output

{"AccountId" : "123456789012", "InstanceId" : "i-1234567890abcdef0", "Region" : "us-east-1", ...}

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
- [[commands/curl-aws-metadata-json-jq]]
