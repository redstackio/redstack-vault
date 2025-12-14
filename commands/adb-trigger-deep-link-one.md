---
data: >-
  adb shell am start -W -a android.intent.action.VIEW -d
  "one://part?start=PartTwoActivity" bounty.pay
tags:
  - android
  - deep-link
type: command
output: App launches PartOneActivity and proceeds to PartTwoActivity if conditions met
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.968Z'
id: 201bb067-2b20-4aa7-a741-de432baa82ef
verified: false
validated: true
submitted: true
---
# adb-trigger-deep-link-one

## Command

```bash
adb shell am start -W -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" bounty.pay
```

## Description

Triggers the first deep link in the app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-W` | Wait for launch | No |
| `-a` | Action | Yes |
| `-d` | Data URI | Yes |

## Examples

### Basic Usage

```bash
adb shell am start -a VIEW -d "scheme://data" package
```

## Expected Output

Activity launched.

## Related

- [[tools/adb]]
