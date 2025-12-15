---
data: node server.js
tags:
  - launch
  - server
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.761Z'
id: 2c959554-e297-49b0-a487-3aec5e93a19d
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

Executes the vulnerable Fastify server script using the Node.js runtime, starting the web server on port 3000.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| server.js | Path to the server script | Yes |

## Examples

### Basic Usage

```bash
node server.js
```

### Advanced Usage

```bash
node --inspect server.js
```

## Expected Output

Server listening on http://localhost:3000; logs indicate successful startup.

## Related

- [[Related Procedure: Launch-and-Exploit-Fastify-Server-for-RCE]]
