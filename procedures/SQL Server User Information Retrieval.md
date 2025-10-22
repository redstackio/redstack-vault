---
id: 51ce57c7-1fae-4d5c-8a7d-0bccc1290910
name: SQL Server User Information Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.722023+00:00'
updated_at: '2023-04-10T20:36:36.432821+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
tags:
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
- '[[Query Current User & determine if the user is a sysadmin]]'
commands:
- '[[Get Current User and Role]]'
---

# SQL Server User Information Retrieval

## Summary

The SQL Server User Information Retrieval procedure involves querying the current user and determining if the user is a sysadmin. This information can be used to escalate privileges and gain access to sensitive data. To execute this procedure, the attacker will need to have access to the SQL Server

## Description

# Description

The SQL Server User Information Retrieval procedure involves querying the current user and determining if the user is a sysadmin. This information can be used to escalate privileges and gain access to sensitive data. To execute this procedure, the attacker will need to have access to the SQL Server and have the necessary permissions to run manual queries. Once the user information is obtained, the attacker can use it to plan further attacks and gain deeper access to the system.

From a technical perspective, this procedure involves executing a query to retrieve the current user information and then checking if the user is a sysadmin. The business value of this procedure is that it allows attackers to gain access to sensitive data, which can be used for financial gain or to gain a competitive advantage.

## Requirements

1. Access to the SQL Server

1. Necessary permissions to run manual queries

## Defense

1. Limit access to the SQL Server to only authorized personnel

1. Implement strong authentication mechanisms to prevent unauthorized access

1. Regularly monitor SQL Server logs for suspicious activity

## Objectives

1. Retrieve SQL Server User Information

1. Determine if the user is a sysadmin

# Instructions

1. To retrieve information about the current SQL Server user, execute the following commands:

**Code**: [[select suser_sname()
Select system_user
select is_]]

> The first command 'select suser_sname()' returns the name of the current SQL Server user. The second command 'Select system_user' returns the login name of the current user. The third command 'select is_srvrolemember('sysadmin')' returns whether the current user is a member of the sysadmin fixed server role, which is the highest level of server-level permissions.

**Command** ([[Get Current User and Role]]):

```bash
select suser_sname()
Select system_user
select is_srvrolemember('sysadmin')
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[Get Current User and Role]]

## Tags

- [[Manual SQL Server Queries]]
- [[MSSQL Server]]
- [[Query Current User & determine if the user is a sysadmin]]
