---
id: uuid-for-apktool-command
data: apktool d target.apk -o decompiled_dir
tags:
  - decompilation
  - android
type: command
output: |
  I: Using Apktool 2.7.0 on target.apk
  I: Decoding AndroidManifest.xml with resources...
  I: Loading resource table...
  I: Decoding file-resources...
  I: Decoding values resources...
  I: Copying raw classes.dex file...
  I: Copying raw assets...
  I: Baksmaling classes.dex...
  I: Copying libs...
  I: Copying unknown files...
  I: Copying original files...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.120Z'
verified: false
validated: true
submitted: true
---
# apktool-decompile

## Command

```bash
apktool d target.apk -o decompiled_dir
```

## Description

Decompiles an Android APK file into its resource and code components, allowing inspection of internal files like strings.xml for sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `d` | Decode/decompile mode | Yes |
| `target.apk` | Path to the input APK file | Yes |
| `-o decompiled_dir` | Output directory for decompiled files | Yes |

## Examples

### Basic Usage

```bash
apktool d app.apk -o output
```

### Advanced Usage

```bash
apktool d -r app.apk -o output  # Skip resource decoding for faster execution
```

## Expected Output

Console logs indicating successful decoding of manifest, resources, and dex files, followed by a new directory with unpacked contents.

## Related

- [[Related Procedure: Decompile-Android-APK-to-Access-Resources]]
