---
data: mdstart
tags:
  - server
  - node-js
type: command
executor: bash
platforms:
  - Node.js
  - Linux
id: 7c36bd9a-b1f1-4398-820a-fe24944f6f37
created_at: '2025-12-14T17:26:05.877Z'
updated_at: '2025-12-14T17:26:05.877Z'
verified: false
validated: true
submitted: true
---
# mdstart-server

## Command

```bash
mdstart
```

## Description

This command starts the md-fileserver HTTP server on localhost:8080, serving files from the current directory but vulnerable to path traversal due to lack of validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default startup with no options; binds to port 8080 | N/A |

## Examples

### Basic Usage

```bash
mdstart
```

### Advanced Usage

No additional flags; runs in foreground.

## Expected Output

Console output: "Server running at http://127.0.0.1:8080". Server remains active until interrupted.

## Related

- [[Related Procedure|procedures/Start-md-fileserver-Server]]
