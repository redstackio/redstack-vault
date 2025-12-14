---
data: ./node_modules/glance/bin/glance.js --verbose --dir ./node_modules/
tags:
  - server
type: command
output: >-
  Server startup message like 'glance serving node_modules/ on port 8080'
  followed by logs of incoming requests
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.659Z'
id: c6817c91-0404-419c-b5ac-324a8a94472b
verified: false
validated: true
submitted: true
---
# glance-start-server

## Command

```bash
./node_modules/glance/bin/glance.js --verbose --dir ./node_modules/
```

## Description

Starts the Glance HTTP static file server with verbose logging, serving from the specified directory on port 8080, exposing the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--verbose` | Enables detailed request logging | No |
| `--dir` | Directory to serve files from | Yes |

## Examples

### Basic Usage

```bash
./node_modules/glance/bin/glance.js --dir ./public
```

### Advanced Usage

```bash
./node_modules/glance/bin/glance.js --verbose --dir ./node_modules/
```

## Expected Output

Startup confirmation and ongoing logs for requests, including 404s and file reads.

## Related

- [[procedures/Start-Glance-Static-File-Server]]
