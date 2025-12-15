---
data: adb pull /data/data/co.vine.android/databases/webview.db .
tags:
  - adb
  - extraction
type: command
output: pulled 12345 bytes in 0.002s
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.785Z'
id: 4ad16038-36a8-422f-8122-dcfe3171e82c
verified: false
validated: true
submitted: true
---
# adb-pull-database

## Command

```bash
adb pull /data/data/co.vine.android/databases/webview.db .
```

## Description

This ADB command pulls the WebView SQLite database from the Vine app's internal storage to the local directory, enabling offline analysis of stored credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pull` | ADB subcommand to copy files from device | Yes |
| `/data/data/co.vine.android/databases/webview.db` | Path to the target database file | Yes |
| `.` | Destination directory on host (current dir) | Yes |

## Examples

### Basic Usage

```bash
adb pull /data/data/co.vine.android/databases/webview.db .
```

### Advanced Usage

```bash
adb pull /data/data/co.vine.android/databases/webview.db /tmp/extracted/
```

## Expected Output

Transfer progress and confirmation, e.g., "4480 KB/s (12345 bytes in 0.002s)". The file webview.db appears in the destination.

## Related

- [[Related Procedure|procedures/Extract-Credentials-from-Vine-WebView-Database]]
