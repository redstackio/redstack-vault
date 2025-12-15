---
id: cmd-start-http-server
data: ./http-file-server.js --path=/tmp/ --host=* --port=1234
tags:
  - server
  - startup
  - http
type: command
output: Server startup message indicating it's listening on port 1234
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.571Z'
verified: false
validated: true
submitted: true
---
# start-http-file-server-with-tmp-root

## Command

```bash
./http-file-server.js --path=/tmp/ --host=* --port=1234
```

## Description

Starts the http-file-server script, setting the root directory to /tmp/, binding to all host interfaces, and listening on port 1234 for HTTP requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--path=/tmp/` | Sets the web root directory to /tmp/ | Yes |
| `--host=*` | Binds the server to all available network interfaces | Yes |
| `--port=1234` | Specifies the listening port | Yes |

## Examples

### Basic Usage

```bash
./http-file-server.js --path=/tmp/ --host=* --port=1234
```

### Advanced Usage

```bash
./http-file-server.js --path=/tmp/ --host=0.0.0.0 --port=1234 --log-level=debug
```

## Expected Output

"http-file-server v0.2.6 started, serving /tmp/ on *:1234". The process remains running, serving files via HTTP.

## Related

- [[commands/npm-install-global-http-file-server]]
- [[procedures/Start-http-file-server-with-Tmp-Root]]
