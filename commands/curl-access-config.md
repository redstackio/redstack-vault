---
data: 'curl https://cortex-ingest.shopifycloud.com/config'
tags:
  - recon
  - config
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.347Z'
id: 6b1edb49-cf14-40ea-9068-8b6ecc627426
verified: false
validated: true
submitted: true
---
# curl-access-config

## Command

```bash
curl https://cortex-ingest.shopifycloud.com/config
```

## Description

Retrieves the server's configuration details from the exposed endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://.../config` | Config endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl https://cortex-ingest.shopifycloud.com/config
```

### Advanced Usage

```bash
curl -s https://cortex-ingest.shopifycloud.com/config | jq .  # Pretty print JSON
```

## Expected Output

{"server": {...}, "storage": {...}}

## Related

- [[Related Procedure]]
