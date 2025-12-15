---
id: cmd-uuid-002
data: statics-server
tags:
  - server
  - node-js
type: command
output: '服务器已经启动 访问localhost:8080'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.371Z'
verified: false
validated: true
submitted: true
---
# statics-server-start

## Command

```bash
statics-server
```

## Description

Starts the static file server in the current directory, serving on localhost:8080.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default port 8080 | No |

## Examples

### Basic Usage

```bash
statics-server
```

### Advanced Usage

```bash
statics-server --port 3000
```

## Expected Output

服务器已经启动 访问localhost:8080

## Related

- [[commands/npm-install-statics-server-global]]
- [[procedures/Run-Statics-Server-in-Directory]]
