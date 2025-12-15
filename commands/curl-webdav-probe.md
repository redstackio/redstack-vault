---
id: cmd-curl-webdav-probe-001
data: >-
  for i in {1..50}; do curl -i -X PROPFIND -u invalid:invalid
  https://target.com/remote.php/dav/files/ 2>/dev/null | head -1; done
tags:
  - recon
  - webdav
  - brute-force
type: command
output: HTTP/1.1 401 Unauthorized (repeated 50 times without variation)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.726Z'
verified: false
validated: true
submitted: true
---
# curl-webdav-probe

## Command

```bash
for i in {1..50}; do curl -i -X PROPFIND -u invalid:invalid https://target.com/remote.php/dav/files/ 2>/dev/null | head -1; done
```

## Description

This bash loop uses curl to send 50 consecutive PROPFIND requests with invalid credentials to a Nextcloud WebDAV endpoint, probing for rate limiting by checking if responses remain consistent without bans or delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers in output | Yes |
| `-X PROPFIND` | Specify WebDAV PROPFIND method | Yes |
| `-u invalid:invalid` | Provide invalid username:password for auth | Yes |
| `https://target.com/remote.php/dav/files/` | Target WebDAV URL | Yes |
| `{1..50}` | Loop count for repeated attempts | No (adjustable) |
| `2>/dev/null | head -1` | Suppress errors and show only first line | No |

## Examples

### Basic Usage

```bash
for i in {1..10}; do curl -i -X PROPFIND -u invalid:invalid https://target.com/remote.php/dav/files/ | head -1; done
```

### Advanced Usage

```bash
for i in {1..100}; do curl -i -k -X PROPFIND -u invalid:invalid https://target.com/remote.php/dav/files/ -H "Depth: 0" 2>/dev/null | head -1; sleep 0.1; done
```

## Expected Output

Repeated lines like "HTTP/1.1 401 Unauthorized" without interruptions, IP blocks, or changing response times, confirming no rate limiting.

## Related

- [[Related Procedure|procedures/Exploit-WebDAV-Authentication-Bypass]]
