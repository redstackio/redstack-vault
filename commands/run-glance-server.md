---
id: cmd-uuid-2
data: ./node_modules/glance/bin/glance.js --verbose --dir ./
tags:
  - server
  - http
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.951Z'
verified: false
validated: true
submitted: true
---
# run-glance-server

## Command

```bash
./node_modules/glance/bin/glance.js --verbose --dir ./
```

## Description

Starts the Glance HTTP server to serve static files from the current directory, exposing directory listings vulnerable to Stored XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--verbose` | Enables detailed logging | No |
| `--dir ./` | Specifies the root directory to serve | Yes |

## Examples

### Basic Usage

```bash
./node_modules/glance/bin/glance.js --dir ./
```

### Advanced Usage

```bash
./node_modules/glance/bin/glance.js --verbose --dir ./
```

## Expected Output

"Glance server listening on port 3000" followed by request logs.

## Related

- [[commands/npm-install-glance]]
- [[procedures/Run-Glance-Server]]
