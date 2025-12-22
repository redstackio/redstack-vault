---
data: >-
  adb shell am start -a android.intent.action.VIEW -d
  "three://part?three=UGFydFRocmVlQWN0aXZpdHk=&switch=b24=&header=X-Token" -n
  bounty.pay/.PartThreeActivity
tags:
  - android
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.188Z'
id: 01c7a502-e9ab-4645-867d-48fa3e230487
verified: false
validated: true
submitted: true
---
# adb-bypass-part3

## Command

```bash
adb shell am start -a android.intent.action.VIEW -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk=&switch=b24=&header=X-Token" -n bounty.pay/.PartThreeActivity
```

## Description

Bypasses PartThreeActivity with base64 params to reach hash input.

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

Advances to next activity.

## Related

- [[tools/ADB]]
- [[procedures/Android-APK-Reverse-Engineering]]
