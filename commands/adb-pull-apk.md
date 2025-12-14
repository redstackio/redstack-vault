---
data: >-
  adb shell pm path com.application.zomato && adb pull
  /data/app/com.application.zomato-*/base.apk zomato.apk
tags:
  - adb
  - apk-extraction
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.215Z'
id: c93b2e0d-c207-412e-ad77-588634ac7e78
verified: false
validated: true
submitted: true
---
# adb-pull-apk

## Command

```bash
adb shell pm path com.application.zomato && adb pull /data/app/com.application.zomato-*/base.apk zomato.apk
```

## Description

Retrieves the package path and pulls the APK file of the Zomato app from an Android device for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pm path` | Lists APK path for the package | Yes |
| `pull` | Downloads file from device | Yes |
| `zomato.apk` | Local output filename | Yes |

## Examples

### Basic Usage

```bash
adb shell pm path com.application.zomato && adb pull /data/app/com.application.zomato-*/base.apk zomato.apk
```

### Advanced Usage

```bash
adb shell pm path com.application.zomato > path.txt && adb pull $(cat path.txt) zomato.apk
```

## Expected Output

First line: package:/data/app/com.application.zomato-xxx/base.apk
APK file downloaded to current directory.

## Related

- [[Related Procedure]]
