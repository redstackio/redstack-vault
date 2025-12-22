---
id: 9847cc82-eda3-43f2-b815-bfadc9d7daad
type: command
executor: bash
data: 'curl http://169.254.169.254/latest/dynamic/instance-identity/document | jq'
output: null
created_at: '2023-04-06T03:56:38.437350+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - ssrf
  - metadata
  - json
verified: true
validated: true
---

# curl-aws-metadata-json-jq

## Command

```bash
curl http://169.254.169.254/latest/dynamic/instance-identity/document | jq
```

## Description

Retrieves and pretty-prints the AWS EC2 instance identity JSON using jq for easier parsing. Requires jq installed on the instance; useful in SSRF scenarios where response needs formatting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Pipes curl output to jq for formatting | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/dynamic/instance-identity/document | jq
```

## Expected Output

{
  "AccountId": "123456789012",
  "InstanceId": "i-1234567890abcdef0",
  "Region": "us-east-1"
}

## Related

- [[procedures/Exploit-SSRF-to-Access-Cloud-Metadata]]
- [[commands/curl-aws-metadata-json]]
