---
data: node app.js
tags:
  - node.js
  - server
type: command
executor: bash
platforms:
  - Node.js
id: 8b7a310f-da44-4bad-b3a8-c942975204e2
created_at: '2025-12-13T09:01:21.667Z'
updated_at: '2025-12-13T09:01:21.667Z'
verified: false
validated: true
submitted: true
---
# Node Run Server

## Command

```bash
node app.js
```

## Description

Runs a Node.js script to start an HTTP server, used for demonstrating vulnerabilities in the http module by processing incoming requests and logging body details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `app.js` | The filename of the Node.js script containing the HTTP server code | Yes |

## Examples

### Basic Usage

```bash
node app.js
```

### Advanced Usage

```bash
node app.js --port 5000
```

## Expected Output

Starts an HTTP server that responds with body length and content for received requests, e.g., server listening on port 5000.

## Related

- [[procedures/Set-Up-Node.js-Test-Server]]
- [[tools/node]]
