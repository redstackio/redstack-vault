---
data: adb devices
tags:
  - adb
  - device-discovery
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:40.075Z'
id: e27288ce-6477-4ece-9f6a-6211a52f5193
verified: false
validated: true
submitted: true
---
# list-adb-devices

## Command

```bash
adb devices
```

## Description

Lists all connected Android devices via ADB, verifying connection status before shell access or other operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; starts ADB server if needed | No |

## Examples

### Basic Usage

```bash
adb devices
```

### Advanced Usage

```bash
adb -s <serial> devices
```

## Expected Output

List of attached devices, e.g.,

List of devices attached

emulator-5554	device

## Related

- [[commands/open-adb-shell]]
