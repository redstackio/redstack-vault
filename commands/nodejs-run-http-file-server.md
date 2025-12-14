---
data: nodejs /usr/lib/node_modules/http-file-server/http-file-server.js
tags:
  - server
  - nodejs
type: command
output: 'Server startup message, e.g., listening on http://localhost:8080'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.245Z'
id: 9c9e733a-b1e2-4fd7-8f50-9a93f58c8dff
verified: false
validated: true
submitted: true
---
# nodejs-run-http-file-server

## Command

```bash
nodejs /usr/lib/node_modules/http-file-server/http-file-server.js
```

## Description

Executes the http-file-server script directly using the Node.js runtime, alternative to global CLI, to start the vulnerable server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
nodejs /usr/lib/node_modules/http-file-server/http-file-server.js
```

### Advanced Usage

```bash
nodejs /usr/lib/node_modules/http-file-server/http-file-server.js --port 8081
```

## Expected Output

http-file-server listening on http://localhost:8080

## Related

- [[Related Procedure|procedures/Run-http-file-server]]
