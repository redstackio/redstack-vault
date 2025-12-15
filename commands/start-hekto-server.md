---
id: cmd-uuid-3
data: ./node_modules/hekto/bin/hekto.js serve
tags:
  - server
  - start
type: command
output: 'Server startup message, listening on http://127.0.0.1:3000'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.078Z'
verified: false
validated: true
submitted: true
---
# start-hekto-server

## Command

```bash
./node_modules/hekto/bin/hekto.js serve
```

## Description

Starts the hekto HTTP server to expose the current directory on port 3000, enabling the vulnerable redirection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| serve | Command to start the server | Yes |

## Examples

### Basic Usage

```bash
./node_modules/hekto/bin/hekto.js serve
```

### Advanced Usage

```bash
./node_modules/hekto/bin/hekto.js serve --port 8080
```

## Expected Output

'hekto server running at http://127.0.0.1:3000' or similar startup confirmation.

## Related

- [[Related Procedure|procedures/Start-Hekto-Server]]
