---
id: cmd-uuid-9012
data: adb devices
tags:
  - mobile
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.617Z'
verified: false
validated: true
submitted: true
---
# adb-devices-check

## Command

```bash
adb devices
```

## Description

Lists connected Android devices via ADB to verify debugging setup before log capture.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
adb devices
```

## Expected Output

List of devices, e.g., 'List of devices attached
emulator-5554	device' indicating successful connection.

## Related

- [[commands/adb-logcat-capture]]
- [[procedures/Access-VK-API-Data-via-Clover-Debug-Logs]]
