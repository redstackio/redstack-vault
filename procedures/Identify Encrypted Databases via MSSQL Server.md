---
id: 27e649a7-d2cb-427d-aaa2-63ed241164bf
name: Identify Encrypted Databases via MSSQL Server
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.856484+00:00'
updated_at: '2023-04-10T20:36:43.197994+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Modify Registry|T1112 - Modify Registry]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Identify Encrypted databases]]'
- '[[Identify Instances and Databases]]'
- '[[MSSQL Server]]'
---

# Identify Encrypted Databases via MSSQL Server

## Summary

This procedure aims to identify encrypted databases via MSSQL Server. Attackers can use this technique to identify databases that are encrypted and containing sensitive information. In order to do so, attackers can use the 'Decrypt-SQLDatabase' command which can decrypt the database and reveal its 

## Description

# Description

This procedure aims to identify encrypted databases via MSSQL Server. Attackers can use this technique to identify databases that are encrypted and containing sensitive information. In order to do so, attackers can use the 'Decrypt-SQLDatabase' command which can decrypt the database and reveal its contents. This technique can be used in combination with other techniques to achieve the attacker's goals.

Technical Explanation: The 'Decrypt-SQLDatabase' command is used to decrypt an encrypted database. The command requires administrative privileges and access to the master key or password. The database is decrypted using the database encryption key and the master key or password. Once decrypted, the contents of the database can be accessed.

Business Value: This technique can be used by attackers to gain access to sensitive information stored in encrypted databases. By identifying and decrypting these databases, attackers can gain unauthorized access to sensitive data which can be used for financial gain or other malicious purposes.

 

## Requirements

1. Administrative privileges on the MSSQL Server

1. Access to the master key or password

 

## Defense

1. Ensure that MSSQL Server is properly secured and only accessible to authorized personnel

1. Implement strong password policies and ensure that the master key is protected

1. Monitor MSSQL Server logs for any suspicious activity, such as attempts to access encrypted databases

 

## Objectives

1. Identify encrypted databases via MSSQL Server

1. Decrypt encrypted databases to access sensitive information

 

# Instructions

1. This command retrieves a list of encrypted SQL databases and automatically decrypts them for admins.

 



**Code**: [[Get-SQLDatabase -Username sa -Password Password123]]



> The command uses the Get-SQLDatabase cmdlet to retrieve a list of SQL databases that are encrypted. The Where-Object cmdlet is used to filter the results to only include databases where the 'is_encrypted' property is equal to 'True'. The ForEach-Object cmdlet is then used to loop through each database and call the 'Decrypt()' method to automatically decrypt the database for admins. The '-Username' and '-Password' parameters are used to provide the necessary authentication credentials, and the '-Instance' parameter specifies the name of the SQL Server instance to connect to.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Modify Registry|T1112 - Modify Registry]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Identify Encrypted databases]]
- [[Identify Instances and Databases]]
- [[MSSQL Server]]


