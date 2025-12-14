---
data: ./node_modules/626/index.js
tags:
  - server
  - execution
type: command
output: 'Server startup message: ''Listening on 8080'''
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.186Z'
id: d65d8454-11b0-47d0-aba6-3443c459dfa7
verified: false
validated: true
submitted: true
---
# start-626-server

## Command

```bash
./node_modules/626/index.js
```

## Description

Executes the vulnerable index.js script from the 626 module to start an HTTP server on port 8080, exposing the path traversal flaw.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs default server | N/A |

## Examples

### Basic Usage

```bash
./node_modules/626/index.js
```

### Advanced Usage

Run in background: ```bash
nohup ./node_modules/626/index.js &
```

## Expected Output

Listening on 8080
(Server remains running until interrupted)

## Related

- [[Related Procedure|procedures/Start-626-HTTP-Server]]
