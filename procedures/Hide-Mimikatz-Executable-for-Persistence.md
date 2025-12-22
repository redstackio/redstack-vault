---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.609420+00:00'
updated_at: '2023-04-10T20:37:30.062948+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Hide-Artifacts|T1564 - Hide Artifacts]]'
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques:
  - >-
    [[sub-techniques/Hidden-Files-and-Directories|T1564.001 - Hidden Files and
    Directories]]
tags:
  - '[[tags/Hide-Your-Binary]]'
  - '[[tags/Windows-Persistence]]'
commands:
  - '[[commands/attrib-set-hidden-attribute-on-mimikatz]]'
platforms:
  - Windows
tools: []
validated: true
---

# Hide-Mimikatz-Executable-for-Persistence

## Summary

This procedure demonstrates how to hide the Mimikatz executable on a Windows system by setting its hidden file attribute, allowing an attacker to maintain persistence and evade basic detection mechanisms while continuing to use the tool for credential extraction and privilege escalation.

## Description

Mimikatz is a post-exploitation tool commonly used to dump credentials from memory on Windows systems. After gaining initial access and placing the Mimikatz binary (mimikatz.exe) on the target, attackers often need to conceal it to avoid discovery by users, antivirus scans, or basic file listings. This procedure uses the built-in Windows 'attrib' command to mark the file as hidden, which prevents it from appearing in standard file explorers or directory listings unless the 'show hidden files' option is enabled. This technique is particularly useful in scenarios where administrative privileges have been obtained, enabling persistence for repeated credential dumping or lateral movement without immediate detection. The method is simple but effective against non-forensic investigations, though advanced EDR tools may still detect file modifications or anomalous behavior.

## Requirements

1. Administrative privileges on the target Windows system to execute file attribute changes and run Mimikatz.
2. The Mimikatz binary (mimikatz.exe) already downloaded and placed in a target directory (e.g., C:\Windows\Temp\).
3. Access to a command prompt or PowerShell session on the target system.

## Defense

- Implement least-privilege access controls to prevent unauthorized administrative access.
- Deploy endpoint detection and response (EDR) solutions that monitor file attribute changes, unusual process executions, and credential dumping attempts.
- Enable file integrity monitoring and regularly audit system logs for suspicious 'attrib' command usage or hidden file creations.
- Use application whitelisting to block unsigned executables like Mimikatz.

## Objectives

1. Conceal the Mimikatz binary to maintain undetected persistence on the compromised system.
2. Enable continued use of Mimikatz for memory-based credential extraction.
3. Evade casual detection by hiding the file from standard visibility.

## Instructions

### Step 1: Set Hidden Attribute on Mimikatz Executable

**Context**: This step modifies the file attributes of mimikatz.exe to mark it as hidden, reducing its visibility in file explorers and command listings. This assumes the file is already present in the current directory or a specified path; adjust the path if necessary to avoid exposing the location.

**Command** ([[commands/attrib-set-hidden-attribute-on-mimikatz]]):
```cmd
attrib +h mimikatz.exe
```

> The 'attrib +h' flag adds the hidden attribute to the specified file. Run this from an elevated command prompt in the directory containing mimikatz.exe. If the file is in a different location, provide the full path (e.g., attrib +h C:\Windows\Temp\mimikatz.exe). This change is immediate and does not require a restart.

### Step 2: Verify the Hidden Status

**Context**: Confirm the attribute was applied successfully to ensure the file is now concealed. This step helps validate the persistence mechanism before proceeding to use Mimikatz.

**Command** ([[commands/attrib-set-hidden-attribute-on-mimikatz]]):
```cmd
attrib mimikatz.exe
```

> This lists the current attributes of the file. Look for the 'H' flag indicating hidden status. If not visible in dir listings without /a:h, the step succeeded. If the file still appears, re-run the hide command or check for permission issues.
