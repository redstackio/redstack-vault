---
id: cmd-simplehttpserver
data: simplehttpserver ./
tags:
  - http-server
  - vulnerable
type: command
output: Serving ./ on port 8000
executor: bash
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.613Z'
verified: false
validated: true
submitted: true
---
# simplehttpserver-start

## Command

```bash
simplehttpserver ./
```

## Description

Starts the simplehttpserver serving the current directory ('./') as web root on port 8000, vulnerable to path traversal via symlinks due to unvalidated URL path handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./` | Web root directory (current working directory) | Yes |

## Examples

### Basic Usage

```bash
simplehttpserver ./
```

### Advanced Usage

```bash
simplehttpserver /path/to/dir  # Serve specific directory
```

## Expected Output

'Serving ./ on port 8000' followed by request logs. Server runs until Ctrl+C; accessible at http://localhost:8000.

## Related

- [[Related Procedure: Start simplehttpserver with Current Directory]]
