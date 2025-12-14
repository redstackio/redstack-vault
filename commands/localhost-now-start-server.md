---
data: localhost 5432
tags:
  - server
  - start
type: command
output: null
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.641Z'
id: 550aa035-83ee-406d-bb76-9b78968c96a9
verified: false
validated: true
submitted: true
---
# localhost-now-start-server

## Command

```bash
localhost 5432
```

## Description

Starts the localhost-now web server on port 5432, serving files from the current directory and exposing the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `5432` | Port number to bind the server | Yes |

## Examples

### Basic Usage

```bash
localhost 5432
```

### Advanced Usage

```bash
localhost 8080
```

## Expected Output

"Web Server started on localhost:5432". Server runs until interrupted.

## Related

- [[Related Procedure|procedures/Start-localhost-now-Server]]
