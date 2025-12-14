---
data: seeftl
tags:
  - server
  - xss
type: command
output: 'Running at http://127.0.0.1:8000/'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.682Z'
id: f5db07e2-b8bd-4cb0-b76c-60984640dde6
verified: false
validated: true
submitted: true
---
# seeftl-start-server

## Command

```bash
seeftl
```

## Description

Starts the seeftl static file server in the current directory, exposing directory listings vulnerable to stored XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default port 8000, localhost bind | No |

## Examples

### Basic Usage

```bash
seeftl
```

### Advanced Usage

```bash
seeftl --port 8080
```

## Expected Output

"Running at http://127.0.0.1:8000/" followed by server logs.

## Related

- [[commands/npm-install-seeftl-global]]
