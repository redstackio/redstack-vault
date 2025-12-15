---
id: cmd-frida-trace
data: frida -U -f com.coinbase.android -l bypass_auth.js --no-pause
tags:
  - android
  - dynamic-analysis
  - hooking
type: command
output: >-
  Spawned com.coinbase.android. Use %resume to let the main thread start
  executing.
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.903Z'
verified: false
validated: true
submitted: true
---
# frida-trace-auth

## Command

```bash
frida -U -f com.coinbase.android -l bypass_auth.js --no-pause
```

## Description

Attaches Frida to the Coinbase Android app process, loads a JavaScript hook to trace and modify authentication functions for bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-U` | USB device targeting | Yes |
| `-f` | Force spawn the app | Yes |
| `com.coinbase.android` | Package name | Yes |
| `-l` | Load script file | Yes |
| `--no-pause` | Start without pausing | No |

## Examples

### Basic Usage

```bash
frida -U -f com.coinbase.android -l bypass_auth.js --no-pause
```

### Advanced Usage

```bash
frida -U com.coinbase.android -l advanced_hook.js  # Attach to running process
```

## Expected Output

Frida console output showing attachment and script execution logs, such as 'Auth bypassed' from the hook.

## Related

- [[Related Procedure|procedures/Exploit-Improper-Authentication-in-Android-App-for-Info-Disclosure]]
