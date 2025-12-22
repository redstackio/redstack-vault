---
id: cmd-002
data: ./node_modules/public/bin/public ./ 6060
tags:
  - server-start
  - node-js
type: command
output: 'Server startup message, e.g., listening on port 6060'
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T03:16:02.748Z'
verified: false
validated: true
submitted: true
---
# public-bin-start-server

## Command

```bash
./node_modules/public/bin/public ./ 6060
```

## Description

Starts the 'public' module's static file server, serving the current directory on port 6060 with directory indexing enabled, vulnerable to XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ./ | Directory to serve (current) | Yes |
| 6060 | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
./node_modules/public/bin/public ./ 6060
```

### Advanced Usage

```bash
./node_modules/public/bin/public /path/to/dir 8080
```

## Expected Output

"Public server running at http://0.0.0.0:6060" or similar startup confirmation.

## Related

- [[Related Procedure|procedures/Install-and-Run-Vulnerable-Public-Module]]
