---
data: adb logcat | grep NextcloudTalk
tags:
  - android
  - logging
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.570Z'
id: 4c4c76c0-c24b-4084-8272-2e864473d663
verified: false
validated: true
submitted: true
---
# adb-logcat-filter

## Command

```bash
adb logcat | grep NextcloudTalk
```

## Description

Captures and filters Android device logs via ADB to identify broadcast actions or app behaviors in Nextcloud Talk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `grep` pattern | Filter string for logs | Yes |

## Examples

### Basic Usage

```bash
adb logcat | grep NextcloudTalk
```

### Advanced Usage

```bash
adb logcat -s NextcloudTalk:D | grep broadcast
```

## Expected Output

Filtered log entries, e.g., "Broadcast sent: com.nextcloud.talk.CALL_START".

## Related

- [[commands/adb-send-broadcast]]
- [[procedures/Send-Malicious-Broadcast-to-Unprotected-Receiver]]
