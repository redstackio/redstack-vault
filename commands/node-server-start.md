---
data: node ./server.js
tags:
  - server
  - start
type: command
output: Server listening on port 8000
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.215Z'
id: b7145fae-27a6-48b9-8782-54fb13e263d2
verified: false
validated: true
submitted: true
---
# node-server-start

## Command

```bash
node ./server.js
```

## Description

Executes the vulnerable Express server script to start listening on port 8000 for webhook triggers that generate multipart boundaries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./server.js` | Path to the server script | Yes |

## Examples

### Basic Usage

```bash
node ./server.js
```

### Advanced Usage

```bash
node --inspect ./server.js
```

## Expected Output

Server listening on port 8000

## Related

- [[commands/node-exploit-run]]
