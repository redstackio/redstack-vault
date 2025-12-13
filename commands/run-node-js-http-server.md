---
data: node server.js
tags:
  - setup
  - node-js
type: command
executor: bash
platforms:
  - Web
  - Node.js
id: aae0f48b-0c2c-4ec8-9127-c19c4fd532d3
created_at: '2025-12-13T09:01:21.559Z'
updated_at: '2025-12-13T09:01:21.559Z'
verified: false
validated: true
submitted: true
---
# Run Node.js HTTP Server

## Command

```bash
node server.js
```

## Description

Runs a simple Node.js HTTP server script for testing vulnerabilities, listening on port 8082 and handling specific routes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `port` | Specifies the listening port (8082) | Yes |

## Examples

### Basic Usage

```bash
node server.js
```

## Expected Output

Server running message and logged requests/responses.

## Related

- [[procedures/Setup-Node-js-Test-Server-for-HTTP-Smuggling]]
