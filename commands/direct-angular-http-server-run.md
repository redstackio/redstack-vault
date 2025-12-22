---
id: cmd-uuid-004
data: ./node_modules/angular-http-server/angular-http-server.js --path ./
tags:
  - server
  - direct-run
type: command
output: >-
  Server startup logs including 'Path specified: ./', 'Using index.html',
  'Listening on 8080', and exploitation logs like 'Sending
  ../../../../../etc/passwd with Content-Type application/octet-stream'
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.708Z'
verified: false
validated: true
submitted: true
---
# direct-angular-http-server-run

## Command

```bash
./node_modules/angular-http-server/angular-http-server.js --path ./
```

## Description

Directly executes the angular-http-server script from node_modules with the specified path, useful for observing detailed logs during exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--path` | Directory to serve | Yes |

## Examples

### Basic Usage

```bash
./node_modules/angular-http-server/angular-http-server.js --path ./
```

### Advanced Usage

```bash
node ./node_modules/angular-http-server/angular-http-server.js --path /dir
```

## Expected Output

Startup logs and file access details, e.g., 'Sending [path] with Content-Type application/octet-stream'.

## Related

- [[Related Procedure|procedures/Setup-and-Run-angular-http-server]]
