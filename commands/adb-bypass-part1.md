---
data: >-
  adb shell am start -a android.intent.action.VIEW -d
  "one://part?start=PartTwoActivity" -n bounty.pay/.PartOneActivity
tags:
  - android
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.194Z'
id: c149eb86-fe2f-4a06-b0ab-1c1ef07e6210
verified: false
validated: true
submitted: true
---
# adb-bypass-part1

## Command

```bash
adb shell am start -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" -n bounty.pay/.PartOneActivity
```

## Description

Bypasses PartOneActivity intent check to advance to PartTwoActivity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Intent action | Yes |
| -d | Data URI | Yes |
| -n | Component name | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Activity advances.

## Related

- [[tools/ADB]]
- [[procedures/Android-APK-Reverse-Engineering]]
