---
data: http-file-server
tags:
  - server
  - nodejs
type: command
output: 'Server startup message, e.g., listening on http://localhost:8080'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.249Z'
id: 9363e17a-2274-45aa-b462-b32547ac7d68
verified: false
validated: true
submitted: true
---
# http-file-server-run

## Command

```bash
http-file-server
```

## Description

Starts the HTTP file server in the current directory, serving files and directory listings on port 8080, vulnerable to stored XSS in filename rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
http-file-server
```

### Advanced Usage

```bash
http-file-server --port 8081
```

## Expected Output

http-file-server listening on http://localhost:8080

## Related

- [[Related Procedure|procedures/Run-http-file-server]]
