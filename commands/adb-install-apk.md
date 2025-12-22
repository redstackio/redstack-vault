---
data: adb install BountyPay.apk
tags:
  - android
type: command
output: Success message confirming installation
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.971Z'
id: a298bc75-9cb9-42d8-86d4-38ff42a380f6
verified: false
validated: true
submitted: true
---
# adb-install-apk

## Command

```bash
adb install BountyPay.apk
```

## Description

Installs an APK on a connected Android device or emulator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| install | Install action | Yes |
| APK path | File to install | Yes |

## Examples

### Basic Usage

```bash
adb install app.apk
```

## Expected Output

'Success' message.

## Related

- [[tools/adb]]
