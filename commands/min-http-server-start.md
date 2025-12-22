---
id: cmd-uuid-1235
data: min-http-server
tags:
  - server
  - http
type: command
output: 'Server startup message, typically listening on a port like 8000'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.314Z'
verified: false
validated: true
submitted: true
---
# min-http-server-start

## Command

```bash
min-http-server
```

## Description

Starts the min-http-server as a zero-configuration HTTP static resource server, serving files from the current directory and exposing the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default mode starts server on port 8000 | No |

## Examples

### Basic Usage

```bash
min-http-server
```

### Advanced Usage

```bash
min-http-server --port 8080
```

## Expected Output

"min-http-server listening on http://0.0.0.0:8000". Server runs indefinitely.

## Related

- [[Related Procedure|procedures/Start-min-http-server]]
