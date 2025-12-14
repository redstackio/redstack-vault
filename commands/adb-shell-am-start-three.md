---
data: >-
  adb shell am start -a "android.intent.action.VIEW" -d
  "three://part/?three=UGFydFRocmVlQWN0aXZpdHk=\\&switch=b24=\\&header=X-Token"
tags:
  - deep-link
type: command
output: 'Activity launched, reveals token input'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.919Z'
id: 4319581d-64cd-4540-b60a-1d93084649ad
verified: false
validated: true
submitted: true
---
# adb-shell-am-start-three

## Command

```bash
adb shell am start -a "android.intent.action.VIEW" -d "three://part/?three=UGFydFRocmVlQWN0aXZpdHk=\\&switch=b24=\\&header=X-Token"
```

## Description

Launch final activity with base64 params.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Action | Yes |
| -d | Encoded URI | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -a "android.intent.action.VIEW" -d "three://part/?three=UGFydFRocmVlQWN0aXZpdHk=\\&switch=b24=\\&header=X-Token"
```

## Expected Output

Token input field appears.

## Related

- [[procedures/Extract-API-Token-from-APK-Using-ADB-and-Frida]]
