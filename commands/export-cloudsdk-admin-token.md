---
id: cmd-23
data: export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./admin.token)
tags:
  - env
  - admin
type: command
output: Env set
executor: bash
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.484Z'
verified: false
validated: true
submitted: true
---
# export-cloudsdk-admin-token

## Command

```bash
export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./admin.token)
```

## Description

Exports the admin access token for gcloud.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `jq ...` | Parse token | Yes |
| `./admin.token` | JSON file | Yes |

## Examples

### Basic Usage

```bash
export ... $(jq ... admin.token)
```

## Expected Output

Token in env var.

## Related

- [[commands/gcloud-compute-create-miner]]
