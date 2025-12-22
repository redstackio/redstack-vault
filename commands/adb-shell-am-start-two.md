---
data: >-
  adb shell am start -a "android.intent.action.VIEW" -d
  "two://part/?two=light\\&switch=on"
tags:
  - deep-link
type: command
output: 'Activity launched, lights up interface'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.922Z'
id: 8656797b-0410-4084-b3c1-4d2ceb57e09b
verified: false
validated: true
submitted: true
---
# adb-shell-am-start-two

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -d "two://part/?two=light\\&switch=on"
```

## Description

Launch second activity with escaped params.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Action | Yes |
| -d | URI with params | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -a "android.intent.action.VIEW" -d "two://part/?two=light\\&switch=on"
```

## Expected Output

Interface reveals inputs.

## Related

- [[procedures/Extract-API-Token-from-APK-Using-ADB-and-Frida]]
