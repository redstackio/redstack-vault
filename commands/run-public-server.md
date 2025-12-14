---
id: cmd-uuid-2
data: ./node_modules/public/bin/public ./ 8080
tags:
  - server
  - node-js
type: command
output: Public.js server running with './' on port 8080
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.786Z'
verified: false
validated: true
submitted: true
---
# run-public-server

## Command

```bash
./node_modules/public/bin/public ./ 8080
```

## Description

Launches the vulnerable static file server from the 'public' module, serving the current directory on port 8080.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./` | Base directory to serve | Yes |
| `8080` | Port to bind to | Yes |

## Examples

### Basic Usage

```bash
./node_modules/public/bin/public ./ 8080
```

### Advanced Usage

```bash
./node_modules/public/bin/public /path/to/dir 3000
```

## Expected Output

Server startup confirmation: 'Public.js server running with './' on port 8080'. The process remains running to handle requests.

## Related

- [[Related Procedure|procedures/Run-Vulnerable-Public-Server]]
