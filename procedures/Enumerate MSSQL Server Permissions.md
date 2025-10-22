---
id: 92bd7efd-47c3-4b9f-ae27-bbdd6365d9a6
name: Enumerate MSSQL Server Permissions
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.959915+00:00'
updated_at: '2023-04-10T20:36:33.536708+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Process Injection|T1055 - Process Injection]]'
tags:
- '[[Effective Permissions from the Server]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Retrieve server level permissions]]'
---

# Enumerate MSSQL Server Permissions

## Summary

This procedure involves querying the MSSQL Server to enumerate effective permissions from the server. This can be used to identify potential attack vectors and to determine what access an attacker may have if they are able to gain a foothold on the server. Technically, this involves running a SQL q

## Description

# Description

This procedure involves querying the MSSQL Server to enumerate effective permissions from the server. This can be used to identify potential attack vectors and to determine what access an attacker may have if they are able to gain a foothold on the server. Technically, this involves running a SQL query to identify the effective permissions for each user or role on the server. The business value of this procedure is that it can help organizations identify and mitigate potential security risks on their MSSQL servers.

## Requirements

1. Authenticated access to the MSSQL server

1. Knowledge of SQL queries

## Defense

1. Ensure that MSSQL servers are properly secured and access is restricted to authorized personnel only

1. Implement strong password policies and multi-factor authentication to prevent unauthorized access to MSSQL servers

1. Regularly monitor MSSQL server logs for suspicious activity and implement intrusion detection and prevention systems

## Objectives

1. Identify potential attack vectors on the MSSQL server

1. Determine what access an attacker may have if they gain a foothold on the server

1. Mitigate potential security risks on MSSQL servers

# Instructions

1. This command retrieves a list of permissions that the current user has for the SQL Server instance.

**Code**: [[select * from fn_my_permissions(null, 'server');]]

> The 'fn_my_permissions' function is used to retrieve information about the permissions that are granted to the current user or to roles in which the user is a member. The first argument is set to 'null' to indicate that the permissions for the current user are to be retrieved. The second argument is set to 'server' to indicate that the permissions are for the SQL Server instance. The result set includes columns for the permission name, permission state, permission type, and the object name (if applicable).

**Command** ([[Retrieve server level permissions]]):

```bash
select * from fn_my_permissions(null, 'server');
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Process Injection|T1055 - Process Injection]]

## Commands Used

- [[Retrieve server level permissions]]

## Tags

- [[Effective Permissions from the Server]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]
