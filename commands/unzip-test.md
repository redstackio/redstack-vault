---
id: cmd-unzip-test-001
data: unzip -t uber-dev.apk
tags:
  - verify
  - archive
type: command
output: |
  testing: AndroidManifest.xml   OK
  ...
  No errors detected in compressed data of /path/uber-dev.apk.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:43.022Z'
verified: false
validated: true
submitted: true
---
# unzip-test

## Command

```bash
unzip -t uber-dev.apk
```

## Description

Tests the integrity of an APK file (ZIP archive) without extracting, ensuring it's valid for decompilation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t | Test mode (check integrity) | Yes |
| file.apk | Path to the APK/ZIP file | Yes |

## Examples

### Basic Usage

```bash
unzip -t app.apk
```

### Advanced Usage

```bash
unzip -t -q app.apk
```

## Expected Output

List of files with "OK" status, ending with "No errors detected". Errors show corrupted entries.

## Related

- [[commands/zipinfo]]
- [[procedures/Download-APK-from-Development-Build-Server]]
