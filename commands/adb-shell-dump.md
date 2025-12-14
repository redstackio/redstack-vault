---
id: cmd-adb-shell-dump
data: >-
  adb shell su -c 'cat
  /data/data/com.coinbase.android/shared_prefs/sensitive_prefs.xml'
tags:
  - android
  - data-extraction
  - root
type: command
output: XML content with sensitive keys
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.897Z'
verified: false
validated: true
submitted: true
---
# adb-shell-dump

## Command

```bash
adb shell su -c 'cat /data/data/com.coinbase.android/shared_prefs/sensitive_prefs.xml'
```

## Description

Executes a shell command on a rooted Android device via ADB to dump sensitive files from the app's data directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `shell` | Invoke remote shell | Yes |
| `su -c` | Run as root | Yes |
| `cat ...` | Command to read file | Yes |

## Examples

### Basic Usage

```bash
adb shell su -c 'cat /data/data/com.coinbase.android/shared_prefs/sensitive_prefs.xml'
```

### Advanced Usage

```bash
adb shell su -c 'sqlite3 /data/data/com.coinbase.android/databases/app.db "SELECT * FROM users;"'
```

## Expected Output

Raw file content, such as XML with key-value pairs containing sensitive data like tokens.

## Related

- [[Related Procedure|procedures/Exploit-Improper-Authentication-in-Android-App-for-Info-Disclosure]]
