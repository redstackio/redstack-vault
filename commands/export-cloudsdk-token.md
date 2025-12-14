---
id: cmd-7
data: export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./default.token)
tags:
  - env
  - token
type: command
output: Environment set
executor: bash
platforms:
  - GCP
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.537Z'
verified: false
validated: true
submitted: true
---
# export-cloudsdk-token

## Command

```bash
export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./default.token)
```

## Description

Extracts and exports the access_token from a GCP metadata JSON for gcloud use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `jq .access_token -r` | Parse raw token | Yes |
| `./default.token` | Input JSON | Yes |

## Examples

### Basic Usage

```bash
export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r token.json)
```

### Advanced Usage

```bash
export GOOGLE_OAUTH2_TOKEN=$(jq ...)
```

## Expected Output

No output; verify with 'echo $CLOUDSDK_AUTH_ACCESS_TOKEN'.

## Related

- [[commands/gcloud-auth-revoke]]
