---
id: 6585eb03-ef7f-43f0-a2c6-71c62dbf999a
name: SQL Server Impersonation Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.013905+00:00'
updated_at: '2023-04-10T20:36:39.928368+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[Find SQL Server Logins Which can be Impersonated for the Current Database]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[List server principals with impersonation permission]]'
---

# SQL Server Impersonation Privilege Escalation

## Summary

This procedure is used to identify SQL Server logins that can be impersonated for the current database, which can then be used to escalate privileges. This technique is commonly used by attackers to gain access to sensitive information or perform unauthorized actions. To perform this procedure, the

## Description

# Description

This procedure is used to identify SQL Server logins that can be impersonated for the current database, which can then be used to escalate privileges. This technique is commonly used by attackers to gain access to sensitive information or perform unauthorized actions. To perform this procedure, the attacker must have valid credentials for the SQL Server instance.

When a SQL Server login has the IMPERSONATE permission, it can impersonate other logins or users within the same database. This can be used to perform actions that the impersonated user has permissions for, including accessing sensitive data or executing code with elevated privileges. This technique can be used to escalate privileges from a low-privileged account to an administrative account, allowing the attacker to take control of the SQL Server instance.

The business value of this procedure is that it allows attackers to gain access to sensitive information and perform unauthorized actions, potentially causing significant harm to the target organization.

 

## Requirements

1. Valid credentials for the SQL Server instance

 

## Defense

1. Limit the number of logins with IMPERSONATE permission

1. Monitor SQL Server logs for suspicious activity

1. Implement multi-factor authentication for SQL Server logins

 

## Objectives

1. Identify SQL Server logins that can be impersonated for the current database

1. Escalate privileges from a low-privileged account to an administrative account

 

# Instructions

1. This command lists all the principals that have impersonation permission. Impersonation permission allows a principal to impersonate another principal and perform actions on their behalf.

 



**Code**: [[select distinct b.name
from sys.server_permissions]]



> The 'sys.server_permissions' table contains information about the server-level permissions granted to principals. The 'sys.server_principals' table contains information about the server-level principals. In this command, we are selecting the distinct names of the principals who have 'impersonate' permission in the 'sys.server_permissions' table by joining it with the 'sys.server_principals' table using the 'principal_id' and 'grantor_principal_id' columns. The 'where' clause filters the results to only include rows where the permission_name is 'impersonate'.



**Command** ([[List server principals with impersonation permission]]):

```bash
select distinct b.name
from sys.server_permissions a
inner join sys.server_principals b
on a.grantor_principal_id = b.principal_id
where a.permission_name = 'impersonate'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[List server principals with impersonation permission]]

## Tags

- [[Find SQL Server Logins Which can be Impersonated for the Current Database]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]


