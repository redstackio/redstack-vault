---
data: >-
  am start -a android.intent.action.VIEW -d https://accounts.shopify.com/
  com.shopify.ping
tags:
  - oauth
  - login
type: command
output: >-
  Browser opens to Shopify login; redirect to
  com.shopify.ping://auth/callback?code=ABCDEFG&state=**************
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.094Z'
id: 99fc4fc4-2e3f-4fc3-9af9-6dc6f6cd1d71
verified: false
validated: true
submitted: true
---
# oauth-browser-redirect

## Command

```bash
am start -a android.intent.action.VIEW -d https://accounts.shopify.com/ com.shopify.ping
```

## Description

Triggers the Android intent to open the browser for Shopify OAuth login in the Ping app, leading to authorization code callback.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a android.intent.action.VIEW` | Intent action for viewing URL | Yes |
| `-d https://accounts.shopify.com/` | Data URL for login | Yes |
| `com.shopify.ping` | Target package | Yes |

## Examples

### Basic Usage

```bash
am start -a android.intent.action.VIEW -d https://accounts.shopify.com/ com.shopify.ping
```

### Advanced Usage

Use with ADB on connected device.

## Expected Output

Browser launches; post-login redirect with code.

## Related

- [[Related Procedure: Perform-OAuth-Login-in-Shopify-Ping-App]]
