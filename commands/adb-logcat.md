---
data: adb logcat
tags:
  - logging
type: command
output: >-
  Logs like 'HOST IS:: http://api.bountypay.h1ctf.com' and 'TOKEN IS::
  8e9998ee3137ca9ade8f372739f062c1'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.908Z'
id: e08f7eef-74a4-4b14-890c-8e1b753e20e5
verified: false
validated: true
submitted: true
---
# adb-logcat

## Command

```bash
adb logcat
```

## Description

Dump Android device logs for app output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Filters optional | No |

## Examples

### Basic Usage

```bash
adb logcat
```

## Expected Output

App logs with host and token.

## Related

- [[procedures/Extract-API-Token-from-APK-Using-ADB-and-Frida]]
