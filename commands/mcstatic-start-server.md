---
data: ./node_modules/mcstatic/bin/mcstatic --port 6060
tags:
  - server
  - node-js
type: command
executor: bash
platforms:
  - Node.js
id: e0d3f2be-0c82-4415-b722-3598b8ca1f3a
created_at: '2025-12-14T17:26:16.781Z'
updated_at: '2025-12-14T17:26:16.781Z'
verified: false
validated: true
submitted: true
---
# mcstatic-start-server

## Command

```bash
./node_modules/mcstatic/bin/mcstatic --port 6060
```

## Description

Starts the mcstatic static HTTP server on port 6060, exposing the directory traversal vulnerability in path handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--port` | Specifies the port for the server to listen on (6060) | Yes |

## Examples

### Basic Usage

```bash
./node_modules/mcstatic/bin/mcstatic --port 6060
```

### Advanced Usage

```bash
./node_modules/mcstatic/bin/mcstatic --port 6060 --dir ./public
```

## Expected Output

Console output indicating "Server listening on http://0.0.0.0:6060" or similar startup confirmation.

## Related

- [[Related Procedure|procedures/Start-mcstatic-Server]]
