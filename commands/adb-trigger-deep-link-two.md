---
data: >-
  adb shell am start -W -a android.intent.action.VIEW -d
  "two://part?two=light\&switch=on" bounty.pay
tags:
  - android
  - deep-link
type: command
output: Reveals screen with text box and MD5 hash
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.964Z'
id: 20c60070-4a76-45dd-9f43-542dd9e0a26f
verified: false
validated: true
submitted: true
---
# adb-trigger-deep-link-two

## Command

```bash
adb shell am start -W -a android.intent.action.VIEW -d "two://part?two=light\&switch=on" bounty.pay
```

## Description

Triggers the second deep link.

## Parameters

Similar to previous adb am start.

## Examples

See basic usage above.

## Expected Output

Next activity screen.

## Related

- [[tools/adb]]
