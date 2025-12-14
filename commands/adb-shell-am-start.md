---
id: cmd-adb-shell-am-start
data: adb shell am start -n com.malicious/.MainActivity
tags:
  - execution
  - android
type: command
output: 'Starting: Intent { cmp=com.malicious/.MainActivity }'
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:41.872Z'
verified: false
validated: true
submitted: true
---
# adb shell am start

## Command

```bash
adb shell am start -n com.malicious/.MainActivity
```

## Description

Starts an Android activity by component name, used to launch malicious apps that dispatch intents to vulnerable components like in ownCloud exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Component name (package/activity) | Yes |
| /ActivityName | Specific activity class | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -n com.malicious/.MainActivity
```

### Advanced Usage

```bash
adb shell am start -n com.owncloud.android/.ui.activity.ReceiveExternalFilesActivity --ei extra_key 1
```

## Expected Output

Intent start confirmation, with the activity launching and potentially triggering background actions like file uploads.

## Related

- [[commands/adb-install-app]]
- [[procedures/Trigger-File-Upload-via-StartActivity]]
