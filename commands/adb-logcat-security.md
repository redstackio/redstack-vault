---
id: bc82feb5-dd57-4ce3-a596-8df541748313
name: adb-logcat-security
type: command
executor: bash
data: adb logcat | grep SecurityException
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.733Z'
platforms:
  - Android
tags:
  - debug
  - crash
verified: false
validated: true
submitted: true
---

# adb-logcat-security

## Command

```bash
adb logcat | grep SecurityException
```

## Description

This command uses ADB to capture Android logcat output and filter for SecurityException entries, useful for detecting crashes during app exploitation like ZIP extraction failures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `adb` | Android Debug Bridge tool | Yes |
| `logcat` | Dumps device logs | Yes |
| `grep SecurityException` | Filters for security-related crashes | Yes |

## Examples

### Basic Usage

```bash
adb logcat | grep SecurityException
```

### Advanced Usage

```bash
adb logcat -s LINE:* | grep SecurityException
```

## Expected Output

Log lines showing SecurityException stack traces, e.g., "java.lang.SecurityException: Permission denied during extraction".

## Related

- [[Related Procedure]]
