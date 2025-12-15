---
id: cmd-curl-verify-post-fix-redirect
data: 'curl -I http://nl.wordpress.net/.attacker.com | grep Location'
tags:
  - verification
  - web
  - redirect
type: command
output: 'Location: https://nl.wordpress.org/.attacker.com'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.157Z'
verified: false
validated: true
submitted: true
---
# curl-verify-post-fix-redirect

## Command

```bash
curl -I http://nl.wordpress.net/.attacker.com | grep Location
```

## Description

Verifies a fix for the open redirect by checking if the Location header now points within the legitimate domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request | Yes |
| `http://nl.wordpress.net/.attacker.com` | Test URL post-fix | Yes |
| `| grep Location` | Filter output to show only Location header | Yes |

## Examples

### Basic Usage

```bash
curl -I http://nl.wordpress.net/.attacker.com | grep Location
```

### Advanced Usage

```bash
curl -I -v http://nl.wordpress.net/.attacker.com | grep -i location
```

## Expected Output

Location: https://nl.wordpress.org/.attacker.com

Confirms the redirect is confined, preventing open exploitation.

## Related

- [[commands/curl-test-subdomain-vector]]
- [[procedures/Exploit-Open-Redirect-via-Malformed-Paths]]
