---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  adb shell run-as com.vkontakte.android cp databases/vk.db /sdcard/ && adb pull
  /sdcard/vk.db .
tags:
  - android
  - debug
  - file-access
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.708Z'
verified: false
validated: true
submitted: true
---
# adb-pull-cache

## Command

```bash
adb shell run-as com.vkontakte.android cp databases/vk.db /sdcard/ && adb pull /sdcard/vk.db .
```

## Description

This command uses Android Debug Bridge (ADB) to access the VK.com app's runtime context, copy the database cache file to shared storage, and pull it to the connected host machine for analysis. It is used in scenarios involving local information disclosure from Android app data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `run-as com.vkontakte.android` | Switches to the app's user context to access protected files | Yes |
| `cp databases/vk.db /sdcard/` | Copies the specific DB file to external storage | Yes |
| `adb pull /sdcard/vk.db .` | Transfers the file from device to current directory on host | Yes |

## Examples

### Basic Usage

```bash
adb shell run-as com.vkontakte.android cp databases/vk.db /sdcard/ && adb pull /sdcard/vk.db .
```

### Advanced Usage

To pull multiple files:

```bash
adb shell run-as com.vkontakte.android cp databases/*.db /sdcard/ && adb pull /sdcard/*.db .
```

## Expected Output

Successful transfer: "vk.db: 1 file pulled. X.XX MB/s (size bytes in Xs)"
Error if app not running or no debug: "run-as: package not debuggable"

## Related

- [[Related Procedure: Access-VK-Android-App-DB-Cache]]
