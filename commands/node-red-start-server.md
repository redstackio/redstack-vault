---
data: node-red
tags:
  - server
  - start
  - node-red
type: command
output: >-
  Server startup message indicating listening on port 1880, e.g., 'Server now
  running at http://127.0.0.1:1880/'
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.430Z'
id: 3dac914c-b0cb-4f75-b31f-60a0c8fcc5a1
verified: false
validated: true
submitted: true
---
# node-red-start-server

## Command

```bash
node-red
```

## Description

This command starts the Node-RED runtime server, launching the web-based flow editor on port 1880 for UI access and vulnerability exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default starts server with standard config | No |

## Examples

### Basic Usage

```bash
node-red
```

### Advanced Usage

```bash
node-red --port 1881
```

## Expected Output

Console output: 'Welcome to Node-RED', followed by 'Server now running at http://127.0.0.1:1880/'. Errors if port is in use.

## Related

- [[Related Procedure|procedures/Start-Node-RED-Server]]
