---
data: dy-server2 -p 8888
tags:
  - server
  - http
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.459Z'
id: 384c3270-fd69-484c-80be-06ed8089fecc
verified: false
validated: true
submitted: true
---
# dy-server2-start-server

## Command

```bash
dy-server2 -p 8888
```

## Description

This command starts the dy-server2 HTTP server on port 8888, serving the current directory's files and folders without sanitization, exposing XSS risks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Port to listen on | Yes |
| `8888` | Specific port number | Yes |

## Examples

### Basic Usage

```bash
dy-server2 -p 8888
```

### Advanced Usage

```bash
dy-server2 -p 3000
```

## Expected Output

'Server is listening on http://localhost:8888' or equivalent startup message.

## Related

- [[Related Procedure|procedures/Start-dy-server2-Server]]
