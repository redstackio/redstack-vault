---
id: cmd-ponse-start-001
data: node index.js
tags:
  - execution
  - server
type: command
output: Server listening on port 8080
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.633Z'
verified: false
validated: true
submitted: true
---
# start-ponse-server

## Command

```bash
node index.js
```

## Description

Executes the Node.js script to start the HTTP server using the vulnerable ponse module, listening on port 8080 and exposing the static file serving endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `index.js` | The server script file | Yes |

## Examples

### Basic Usage

```bash
node index.js
```

### Advanced Usage

```bash
node --inspect index.js
```

## Expected Output

Console log: 'Server listening on port 8080'. The process runs continuously, handling incoming requests.

## Related

- [[commands/install-ponse-module]]
- [[procedures/Start-Ponse-Server]]
