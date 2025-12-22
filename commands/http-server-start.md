---
data: http_server
tags:
  - server
  - http
type: command
output: 'server running is :http://localhost:8888'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:49.783Z'
id: 5f6eb593-148c-4fd9-bb60-a288ac8af737
verified: false
validated: true
submitted: true
---
# http-server-start

## Command

```bash
http_server
```

## Description

Starts a static HTTP server in the current directory, serving files on port 8888 by default, vulnerable to unsanitized directory listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses defaults: port 8888, current dir | No |

## Examples

### Basic Usage

```bash
http_server
```

### Advanced Usage

```bash
http_server 3000
```

## Expected Output

"server running is :http://localhost:8888" with the server listening.

## Related

- [[commands/npm-install-global-http-server]]
