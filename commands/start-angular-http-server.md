---
data: ./node_modules/angular-http-server/angular-http-server.js -p 6060
tags:
  - server
  - node.js
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.706Z'
id: 41addece-c1ce-4d17-8a1c-cd9a6d0612ec
verified: false
validated: true
submitted: true
---
# start-angular-http-server

## Command

```bash
./node_modules/angular-http-server/angular-http-server.js -p 6060
```

## Description

Starts the vulnerable HTTP server on port 6060 using the installed module's script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Port flag | Yes |
| `6060` | Port number | Yes |

## Examples

### Basic Usage

```bash
./node_modules/angular-http-server/angular-http-server.js -p 6060
```

### Advanced Usage

```bash
node ./node_modules/angular-http-server/angular-http-server.js -p 6060 -s
```

## Expected Output

"Server running at http://127.0.0.1:6060" or similar startup message.

## Related

- [[Related Procedure]]
