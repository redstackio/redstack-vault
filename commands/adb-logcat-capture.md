---
id: cmd-uuid-5678
data: 'adb logcat -s Clover:V > clover_logs.txt'
tags:
  - mobile
  - debug
  - logging
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.620Z'
verified: false
validated: true
submitted: true
---
# adb-logcat-capture

## Command

```bash
adb logcat -s Clover:V > clover_logs.txt
```

## Description

This command uses ADB to capture verbose logs from the Clover Android app, filtering for relevant entries and redirecting output to a file for analysis of sensitive API data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s Clover:V` | Filter logs to Clover app at verbose level | Yes |
| `> clover_logs.txt` | Redirect output to file | Yes |

## Examples

### Basic Usage

```bash
adb logcat -s Clover:V > clover_logs.txt
```

### Advanced Usage

```bash
adb logcat -s Clover:V *:S > clover_logs.txt
```

> Suppresses non-Clover logs for cleaner output.

## Expected Output

A text file (clover_logs.txt) populated with timestamped log entries, including VK API response JSON when app interactions occur.

## Related

- [[commands/adb-devices-check]]
- [[procedures/Access-VK-API-Data-via-Clover-Debug-Logs]]
