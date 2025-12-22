---
id: cmd-nodejs-run-001
data: nodejs index.js
tags:
  - execution
  - server
type: command
output: 'Server listening on port 3006, ready to handle requests'
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.510Z'
verified: false
validated: true
submitted: true
---
# nodejs-run-server

## Command

```bash
nodejs index.js
```

## Description

Executes the Node.js script index.js to start an HTTP server using the hangersteak module on port 3006. This exposes the vulnerability for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `index.js` | Script file containing server setup | Yes |

## Examples

### Basic Usage

```bash
nodejs index.js
```

### Advanced Usage

```bash
nodejs --inspect index.js
```

## Expected Output

Console output: "Server running on port 3006". The process listens indefinitely.

## Related

- [[Related Procedure|procedures/Start-Hangersteak-Server]]
