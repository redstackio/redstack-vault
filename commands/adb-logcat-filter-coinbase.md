---
id: cmd-adb-logcat-001
data: adb logcat -s Coinbase
tags:
  - logcat
  - monitoring
type: command
output: Log entries including the OAuth response code during authorization
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.144Z'
verified: false
validated: true
submitted: true
---
# adb logcat -s Coinbase

## Command

```bash
adb logcat -s Coinbase
```

## Description

This command uses ADB to monitor and display Android device logs filtered by the 'Coinbase' tag, useful for capturing app output during OAuth authorization to detect leaked sensitive information like response codes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Specifies the tag to filter logs (e.g., Coinbase) | Yes |
| `Coinbase` | The exact tag name for Coinbase app logs | Yes |

## Examples

### Basic Usage

```bash
adb logcat -s Coinbase
```

### Advanced Usage

```bash
adb logcat -s Coinbase *:V
```

> Adds verbosity level filter for verbose logs only.

## Expected Output

Real-time streaming of log entries tagged 'Coinbase', such as:

I/Coinbase: OAuth authorization initiated
D/Coinbase: Response code: abc123def456

## Related

- [[Related Procedure|procedures/Monitor-Android-Logs-for-Coinbase-OAuth-Activity]]
