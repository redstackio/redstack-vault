---
data: >-
  curl -X POST
  "https://www.googleapis.com/compute/v1/projects/███/setCommonInstanceMetadata"
  -H "Authorization: Bearer ██████████████" -H "Content-Type: application/json"
  --data '{"items": [{"key": "0xACB", "value": "test"}]}'
tags:
  - gcp
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2d11dbf0-bb32-4370-93cd-3ace6aba4493
created_at: '2025-12-11T06:10:23.379Z'
updated_at: '2025-12-11T06:10:23.379Z'
verified: false
validated: true
submitted: true
---
# curl-set-instance-metadata

## Command

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/███/setCommonInstanceMetadata" -H "Authorization: Bearer ██████████████" -H "Content-Type: application/json" --data '{"items": [{"key": "0xACB", "value": "test"}]}'
```

## Description

Attempts to set common instance metadata in GCP to add an SSH key using a leaked token, typically fails due to permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specify POST method | Yes |
| `Authorization: Bearer ██████████████` | Authenticate with leaked token | Yes |
| `Content-Type: application/json` | Set request content type | Yes |
| `--data` | JSON payload to set metadata key-value | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/project-id/setCommonInstanceMetadata" -H "Authorization: Bearer token" -H "Content-Type: application/json" --data '{"items": [{"key": "ssh-key", "value": "test"}]}'
```

## Expected Output

Error response with 403 forbidden due to missing permissions.

## Related

- [[commands/curl-query-token-info]]
- [[procedures/Test-and-Analyze-Leaked-GCP-Tokens]]
