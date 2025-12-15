---
id: cmd-uuid-001
data: adb logcat | grep twitter
tags:
  - android
  - logging
  - grep
type: command
output: Log entries including leaked OAuth token from Twitter login
executor: bash
platforms:
  - Android
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.240Z'
verified: false
validated: true
submitted: true
---
# logcat-grep-twitter

## Command

```bash
adb logcat | grep twitter
```

## Description

This command uses ADB to stream Android device logs via logcat and pipes them to grep to filter for entries containing 'twitter', revealing leaked OAuth tokens from Fabric Twitter Kit during login. Use it post-authentication to detect sensitive information disclosure in logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `adb` | Android Debug Bridge tool for device communication | Yes |
| `logcat` | Captures system and app logs | Yes |
| `|` | Pipe output to next command | Yes |
| `grep` | Filters lines matching the pattern | Yes |
| `twitter` | Search string for Twitter-related log entries | Yes |

## Examples

### Basic Usage

```bash
adb logcat | grep twitter
```

Streams live logs and shows only Twitter mentions, useful for real-time monitoring after login.

### Advanced Usage

```bash
adb logcat -d | grep -i twitter > twitter_logs.txt
```

Dumps current logs to a file with case-insensitive grep for offline analysis.

## Expected Output

Log lines such as: `I/Twitter: Authorizing with oauth_token=ABC123def...` where the token is exposed in the URL parameter, allowing extraction for credential theft.

## Related

- [[Related Procedure|procedures/Extract-Leaked-OAuth-Token-from-Logcat]]
