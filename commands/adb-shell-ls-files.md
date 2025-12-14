---
id: 1fc74a79-c830-471b-8fd9-97c6e69ea815
name: adb-shell-ls-files
type: command
executor: bash
data: adb shell ls /data/data/jp.naver.line.android/files/
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.729Z'
platforms:
  - Android
tags:
  - file-inspection
  - debug
verified: false
validated: true
submitted: true
---

# adb-shell-ls-files

## Command

```bash
adb shell ls /data/data/jp.naver.line.android/files/
```

## Description

This command uses ADB shell to list files in the LINE app's private directory, helping verify overwrites from path traversal exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `adb shell ls` | Executes ls command on device shell | Yes |
| `/data/data/jp.naver.line.android/files/` | Path to LINE app files | Yes |

## Examples

### Basic Usage

```bash
adb shell ls /data/data/jp.naver.line.android/files/
```

### Advanced Usage

```bash
adb shell ls -la /data/data/jp.naver.line.android/files/
```

## Expected Output

List of files, e.g., "file1.txt  malicious_overwrite.txt", indicating changes.

## Related

- [[Related Procedure]]
