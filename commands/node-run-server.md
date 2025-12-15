---
id: cmd-uuid-1
data: node server.js
tags:
  - setup
  - server
type: command
output: Server listening on port 3000
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.672Z'
verified: false
validated: true
submitted: true
---
# node-run-server

## Command

```bash
node server.js
```

## Description

Executes a Node.js script to start an HTTP/2 server for vulnerability testing. Use this to initialize the target environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `server.js` | Path to the server script file | Yes |

## Examples

### Basic Usage

```bash
node server.js
```

### Advanced Usage

```bash
node --max-old-space-size=4096 server.js
```

## Expected Output

Server startup message like "Server running at http://localhost:3000/" and HTTP/2 enabled confirmation.

## Related

- [[procedures/Start-Node-js-HTTP2-Server]]
