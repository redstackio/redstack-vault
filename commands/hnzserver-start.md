---
id: 123e4567-e89b-12d3-a456-426614174005
name: hnzserver-start
type: command
executor: bash
data: hnzserver
output: 'server running is :http://localhost:8888'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.458Z'
platforms:
  - Linux
tags:
  - server
  - node-js
verified: false
validated: true
submitted: true
---

# hnzserver-start

## Command

```bash
hnzserver
```

## Description

This command starts the hnzserver static file server in the current directory, listening on port 8888 for HTTP requests. It serves files without path sanitization, enabling path traversal exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Runs with defaults: serves from current dir on port 8888 | N/A |

## Examples

### Basic Usage

```bash
hnzserver
```

### Advanced Usage

```bash
cd ~/Desktop && hnzserver
```

## Expected Output

The console outputs "server running is :http://localhost:8888" and keeps the process running. Requests to the URL will serve directory files.

## Related

- [[commands/npm-install-hnzserver]]
- [[procedures/Start-hnzserver-Static-Server]]
