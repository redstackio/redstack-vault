---
data: node server.js
tags:
  - node-js
  - setup
type: command
executor: bash
platforms:
  - Node.js
id: 96bceac3-a45e-4465-9a89-b9ff208f69eb
created_at: '2025-12-13T09:01:17.431Z'
updated_at: '2025-12-13T09:01:17.431Z'
verified: false
validated: true
submitted: true
---
# node-start-http-server

## Command

```bash
node server.js
```

## Description

Runs a Node.js script to start a simple HTTP server for testing request parsing, used in vulnerability demonstrations like HTTP Request Smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `server.js` | The script file containing the HTTP server code | Yes |

## Examples

### Basic Usage

```bash
node server.js
```

## Expected Output

Starts the server with no direct output, but it begins listening on port 80 for incoming connections.

## Related

- [[procedures/Setup-Node-js-Testing-HTTP-Server]]
- [[tools/Node-js]]
