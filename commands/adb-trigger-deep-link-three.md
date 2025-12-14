---
data: >-
  adb shell am start -W -a android.intent.action.VIEW -d
  "three://part?switch=b24\&three=UGFydFRocmVlQWN0aXZpdHk%3D\&header=X-Token"
  bounty.pay
tags:
  - android
  - deep-link
  - token-extraction
type: command
output: 'Logs reveal URL, header X-Token, and token value'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.961Z'
id: 5bc838cd-6184-405e-a5f9-0b63756d53d7
verified: false
validated: true
submitted: true
---
# adb-trigger-deep-link-three

## Command

```bash
adb shell am start -W -a android.intent.action.VIEW -d "three://part?switch=b24\&three=UGFydFRocmVlQWN0aXZpdHk%3D\&header=X-Token" bounty.pay
```

## Description

Triggers the final deep link to extract token from logs.

## Parameters

Encoded URI for third link.

## Examples

See adb examples.

## Expected Output

Token in logcat.

## Related

- [[tools/adb]]
