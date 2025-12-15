---
data: >-
  adb shell pm path com.linecorp.linelite | xargs adb pull && unzip base.apk
  AndroidManifest.xml && aapt dump xmltree AndroidManifest.xml
  AndroidManifest.xml > manifest.txt && grep -i exported manifest.txt
tags:
  - recon
  - android
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.042Z'
id: 6de2293a-2883-4061-ac84-2bd8b2190f95
verified: false
validated: true
submitted: true
---
# adb-pull-manifest

## Command

```bash
adb shell pm path com.linecorp.linelite | xargs adb pull && unzip base.apk AndroidManifest.xml && aapt dump xmltree AndroidManifest.xml AndroidManifest.xml > manifest.txt && grep -i exported manifest.txt
```

## Description

This command retrieves and analyzes the AndroidManifest.xml from the LINE Lite APK to identify exported activities. Use it during reconnaissance to find vulnerable components.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `com.linecorp.linelite` | Package name of the target app | Yes |
| `base.apk` | Pulled APK filename | No (default) |
| `manifest.txt` | Output file for decoded manifest | No |

## Examples

### Basic Usage

```bash
adb shell pm path com.linecorp.linelite | xargs adb pull && unzip base.apk AndroidManifest.xml && aapt dump xmltree AndroidManifest.xml AndroidManifest.xml > manifest.txt && grep -i exported manifest.txt
```

### Advanced Usage

```bash
adb shell pm path $PACKAGE | xargs adb pull $APK && unzip $APK AndroidManifest.xml && aapt dump xmltree AndroidManifest.xml AndroidManifest.xml > manifest.txt && grep -i "exported=true" manifest.txt
```

## Expected Output

Lines showing exported components, e.g., activity android:exported="true" for SelectShareActivity.

## Related

- [[Related Procedure: Identify Exported Activity in Android App]]
