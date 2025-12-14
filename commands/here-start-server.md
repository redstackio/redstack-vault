---
data: here -p 8081
tags:
  - server
  - web-server
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.881Z'
id: 50b532b5-ade2-4f4d-9f0f-311d09b4c80c
verified: false
validated: true
submitted: true
---
# here-start-server

## Command

```bash
here -p 8081
```

## Description

Starts the serve-here static file server from the current directory, binding to the specified port to expose files for HTTP access, vulnerable to path traversal in version 3.2.0.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Port to bind the server to | Yes |
| `8081` | Specific port number | Yes |

## Examples

### Basic Usage

```bash
here -p 8081
```

### Advanced Usage

```bash
here -p 8081 --cors
```

(Enables CORS if supported)

## Expected Output

Server startup message: "Serving /current/dir on port 8081". The process listens indefinitely until interrupted.

## Related

- [[commands/npm-install-serve-here]]
- [[procedures/Start-serve-here-Server]]
