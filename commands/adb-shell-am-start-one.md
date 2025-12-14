---
data: >-
  adb shell am start -a "android.intent.action.VIEW" -d
  "one://part/?start=PartTwoActivity"
tags:
  - deep-link
type: command
output: Activity launched successfully
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.925Z'
id: d83ce0b0-a715-4e06-a61a-3d824336167b
verified: false
validated: true
submitted: true
---
# adb-shell-am-start-one

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -d "one://part/?start=PartTwoActivity"
```

## Description

Launch APK activity via deep link.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Action VIEW | Yes |
| -d | Deep link URI | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -a "android.intent.action.VIEW" -d "one://part/?start=PartTwoActivity"
```

## Expected Output

Activity starts.

## Related

- [[procedures/Extract-API-Token-from-APK-Using-ADB-and-Frida]]
