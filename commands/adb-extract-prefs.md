---
data: adb shell cat ./data/data/bounty.pay/shared_prefs/user_created.xml
tags:
  - android
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.185Z'
id: dc05305f-4419-4f30-9dda-8283e6e96117
verified: false
validated: true
submitted: true
---
# adb-extract-prefs

## Command

```bash
adb shell cat ./data/data/bounty.pay/shared_prefs/user_created.xml
```

## Description

Extracts shared preferences XML containing the API token.

## Parameters

None specific.

## Examples

### Basic Usage

As above.

## Expected Output

XML with API token.

## Related

- [[tools/ADB]]
- [[procedures/Android-APK-Reverse-Engineering]]
