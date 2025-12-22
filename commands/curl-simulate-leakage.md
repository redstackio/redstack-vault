---
data: >-
  curl -H "Referer:
  https://hackerone.com/users/password/edit?reset_password_token=HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN"
  -A "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0"
  -e
  "https://hackerone.com/users/password/edit?reset_password_token=HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN"
  http://xkcd.com/936/
tags:
  - http-request
  - referer-simulation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.900Z'
id: fb97d935-9682-4cad-9c86-97fb42d6f957
verified: false
validated: true
submitted: true
---
# curl-simulate-leakage

## Command

```bash
curl -H "Referer: https://hackerone.com/users/password/edit?reset_password_token=HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN" -A "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0" -e "https://hackerone.com/users/password/edit?reset_password_token=HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN" http://xkcd.com/936/
```

## Description

This curl command simulates a browser's HTTP GET request to an external site, explicitly setting the Referer header to include a leaked password reset URL with token, mimicking the cross-domain leakage from a vulnerable reset page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Referer: ..."` | Sets the custom referer header with the sensitive URL | Yes |
| `-A "..."` | Sets the User-Agent to match a common browser | Yes |
| `-e "..."` | Alternative way to set referer (for compatibility) | No |
| `http://xkcd.com/936/` | Target external URL to request | Yes |

## Examples

### Basic Usage

```bash
curl -H "Referer: https://example.com/reset?token=ABC123" http://external-site.com/
```

### Advanced Usage

```bash
curl -H "Referer: https://hackerone.com/users/password/edit?reset_password_token=TOKEN" -A "Mozilla/5.0 ..." --verbose http://xkcd.com/936/
```

## Expected Output

HTTP response body from the external site (e.g., HTML from xkcd comic), with the referer header sent to the server for logging. Use --verbose to see headers in output.

## Related

- [[Related Procedure: Trigger-Referer-Header-Leakage-to-External-Site]]
