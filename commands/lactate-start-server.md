---
id: cmd-lactate-start-001
name: lactate-start-server
type: command
executor: bash
data: lactate -p 8081
output: Server startup message indicating it's listening on port 8081
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.988Z'
platforms:
  - Linux
tags:
  - server
  - web
verified: false
validated: true
submitted: true
---

# lactate-start-server

## Command

```bash
lactate -p 8081
```

## Description

Starts the lactate static web server on port 8081, serving files from the current directory and exposing the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Specifies the port to listen on | Yes |
| `8081` | Port number | Yes |

## Examples

### Basic Usage

```bash
lactate -p 8081
```

### Advanced Usage

```bash
lactate -p 8081 --dir /root
```

## Expected Output

"lactate server running at http://localhost:8081" or similar startup log.

## Related

- [[commands/curl-path-traversal]]
- [[procedures/Start-Vulnerable-Lactate-Server]]
