---
id: cmd-398285-serve
data: serve
tags:
  - web-server
type: command
output: |-
  │                                                 │
  │   Serving!                                      │
  │                                                 │
  │   - Local:            http://localhost:5000     │
  │   - On Your Network:  http://192.168.x.x:5000   │
  │                                                 │
  │   Copied local address to clipboard!            │
executor: bash
platforms:
  - Web
  - Node.js
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.895Z'
verified: false
validated: true
submitted: true
---
# serve-start

## Command

```bash
serve
```

## Description

Starts the serve HTTP server in the current directory on port 5000, enabling static file serving and directory listings vulnerable to XSS via unsanitized filenames.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Defaults to current dir and port 5000 | N/A |

## Examples

### Basic Usage

```bash
serve
```

### Advanced Usage

```bash
serve -p 3000
```

## Expected Output

Server acceptance message with local URL; listens for connections until stopped.

## Related

- [[procedures/Start-Serve-Server-for-Directory-Hosting]]
