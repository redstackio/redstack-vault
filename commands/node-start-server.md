---
data: node server.js
tags:
  - server-start
  - node-js
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:13.959Z'
id: ec314718-32ae-4ff8-a982-39bb71e01660
verified: false
validated: true
submitted: true
---
# node-start-server

## Command

```bash
node server.js
```

## Description

Executes the Node.js script to launch the tianma-static server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `server.js` | Script file | Yes |

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

Server starts, outputs listening message; accessible at http://localhost:3000.

## Related

- [[commands/create-server-script]]
