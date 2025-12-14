---
id: cmd-check-headers-xframe
name: check-http-headers-for-x-frame-options
type: command
executor: bash
data: 'curl -I https://www.goodhire.com/api'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.697Z'
platforms:
  - Linux
  - macOS
  - Windows (with curl)
tags:
  - headers
  - web-recon
verified: false
validated: true
submitted: true
---

# check-http-headers-for-x-frame-options

## Command

```bash
curl -I https://www.goodhire.com/api
```

## Description

This command uses curl to perform a HEAD request on the specified API endpoint, retrieving HTTP response headers to check for security headers like X-Frame-Options. It is useful for initial reconnaissance of web vulnerabilities such as clickjacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I, --head` | Fetch headers only (no body) | Yes |
| `URL` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://www.goodhire.com/api
```

### Advanced Usage

```bash
curl -I -s https://www.goodhire.com/api | grep -i x-frame-options
```
(Add -s for silent mode and grep to filter for the specific header.)

## Expected Output

Description of what output to expect when the command runs successfully.

HTTP/2 200 
date: Mon, 01 Oct 2023 12:00:00 GMT
server: nginx
content-type: application/json
... (no X-Frame-Options line)

If X-Frame-Options is present, it would show as "X-Frame-Options: DENY".

## Related

- [[Related Procedure: Test API for Clickjacking Protections]]
