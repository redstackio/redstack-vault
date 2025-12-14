---
data: adb shell
tags:
  - android
  - debug
type: command
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
id: 007e0ff3-bdcd-47cd-9dbd-2bd4812d522f
created_at: '2025-12-13T23:52:44.040Z'
updated_at: '2025-12-13T23:52:44.040Z'
verified: false
validated: true
submitted: true
---
# adb-shell

## Command

```bash
adb shell
```

## Description

Starts an interactive shell on the connected Android device via ADB, allowing execution of commands like 'am start' for activity launches.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
adb shell
```

### Advanced Usage

```bash
adb shell ls /sdcard/
```

## Expected Output

Interactive shell prompt on device (e.g., shell@device:~$).

## Related

- [[commands/am-start-actionbar-xss-alert]]
