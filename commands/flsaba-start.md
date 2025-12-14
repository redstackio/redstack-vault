---
id: cmd-uuid-4
data: flsaba
tags:
  - server-start
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.335Z'
verified: false
validated: true
submitted: true
---
---

# flsaba

## Command

```bash
flsaba
```

## Description

Starts the flsaba HTTP server, serving the current directory with enabled listing on port 3000, vulnerable to XSS in name rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Defaults to port 3000 and current dir | N/A |

## Examples

### Basic Usage

```bash
flsaba
```

### Advanced Usage

```bash
PORT=3001 flsaba  # Custom port via env
```

## Expected Output

"flsaba v1.1.0 server listening on port 3000 Directory: /current/path". Server logs requests.

## Related

- [[commands/npm-install-flsaba]]
- [[procedures/Start-flsaba-Server]]

