---
id: c9a09377-486b-4233-b6a1-cfc11b585671
name: MSSQL Injection to Grant DBA Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.077366+00:00'
updated_at: '2023-04-10T20:22:39.378597+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[New Service|T1050 - New Service]]'
- '[[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL Make user DBA (DB admin)]]'
commands:
- '[[Add user to sysadmin role]]'
---

# MSSQL Injection to Grant DBA Access

## Summary

MSSQL Injection is a technique used to exploit a vulnerability in a Microsoft SQL Server. By injecting malicious SQL code, an attacker can gain unauthorized access to the system, escalate privileges, and perform various malicious activities. In this specific procedure, the attacker is using an MSSQ

## Description

# Description

MSSQL Injection is a technique used to exploit a vulnerability in a Microsoft SQL Server. By injecting malicious SQL code, an attacker can gain unauthorized access to the system, escalate privileges, and perform various malicious activities. In this specific procedure, the attacker is using an MSSQL Injection to make a user a DBA (Database Administrator), which gives them full control over the database. This attack can be performed remotely, and can lead to a complete compromise of the database and potentially the entire system.

To execute this attack, the attacker will first identify a vulnerable SQL Server and then use an MSSQL Injection to execute a command to add a new user as a DBA. Once the user has been added, the attacker can connect to the database using the new user's credentials and perform any action they desire.

The business value of this attack is that the attacker can gain access to sensitive data, modify or delete data, and disrupt business operations. This can lead to financial loss, reputational damage, and regulatory fines.

 

## Requirements

1. Access to a vulnerable MSSQL Server

1. Knowledge of MSSQL Injection techniques

1. Access to tools to perform the attack

 

## Defense

1. Ensure that MSSQL Servers are up-to-date with the latest security patches

1. Implement strict access controls and authentication mechanisms for MSSQL Servers

1. Regularly perform security audits and penetration testing to identify and mitigate vulnerabilities

 

## Objectives

1. Gain DBA access to the MSSQL Server

1. Perform unauthorized actions on the database

1. Access sensitive data

 

# Instructions

1. To add a user as a sysadmin, execute the following SQL command:

 



**Code**: [[EXEC master.dbo.sp_addsrvrolemember 'user', 'sysad]]



> The 'sp_addsrvrolemember' system stored procedure adds a login as a member of a fixed server role. In this case, we are adding the 'user' login as a member of the 'sysadmin' server role. The semicolon at the end of the command signifies the end of the statement.



**Command** ([[Add user to sysadmin role]]):

```bash
EXEC master.dbo.sp_addsrvrolemember 'user', 'sysadmin';
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[New Service|T1050 - New Service]]
- [[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]

## Commands Used

- [[Add user to sysadmin role]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL Make user DBA (DB admin)]]


