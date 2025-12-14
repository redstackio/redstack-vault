---
data: >-
  adb shell am start -a android.intent.action.VIEW -d
  "two://part?two=light&switch=on" -n bounty.pay/.PartTwoActivity
tags:
  - android
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.191Z'
id: 30510b8e-03be-468d-a4fd-93e1d697c576
verified: false
validated: true
submitted: true
---
# adb-bypass-part2

## Command

```bash
adb shell am start -a android.intent.action.VIEW -d "two://part?two=light&switch=on" -n bounty.pay/.PartTwoActivity
```

## Description

Bypasses PartTwoActivity to show submit form.

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

Form displayed.

## Related

- [[tools/ADB]]
- [[procedures/Android-APK-Reverse-Engineering]]
