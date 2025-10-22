---
id: 9e9a34a5-3c43-4986-803f-f8c4122a2291
name: Query MSSQL Server for Sysadmins
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.904812+00:00'
updated_at: '2023-04-10T20:36:42.502671+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
tags:
- '[[List All Sysadmins]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Retrieve server principals with sysadmin role]]'
---

# Query MSSQL Server for Sysadmins

## Summary

Querying a MSSQL Server for a list of sysadmins can provide an attacker with a list of privileged accounts on the target network. This information can be used to further target those accounts for credential theft or privilege escalation.

To list all sysadmins on a MSSQL Server, a manual SQL query 

## Description

# Description

Querying a MSSQL Server for a list of sysadmins can provide an attacker with a list of privileged accounts on the target network. This information can be used to further target those accounts for credential theft or privilege escalation.

To list all sysadmins on a MSSQL Server, a manual SQL query can be run. This query will return a list of all users with sysadmin privileges on the server. This information can be used to identify high-value targets for further exploitation.

This procedure can provide valuable information for an attacker looking to escalate privileges or move laterally within a network.

## Requirements

1. Valid credentials for the MSSQL Server

1. Access to run SQL queries on the server

## Defense

1. Limit the number of accounts with sysadmin privileges on MSSQL Servers

1. Use strong passwords and multi-factor authentication for accounts with sysadmin privileges

1. Monitor for and alert on unusual activity related to account discovery and privilege escalation

## Objectives

1. Identify all sysadmins on a MSSQL Server

1. Gather information on high-value targets for further exploitation

# Instructions

1. This command lists all the system administrators in the SQL Server instance.

**Code**: [[SELECT name,type_desc,is_disabled FROM sys.server_]]

> The 'sys.server_principals' table contains information about server-level principals, such as logins and roles. The 'IS_SRVROLEMEMBER' function checks if a given principal is a member of a specified server role. In this case, we are checking if the principal is a member of the 'sysadmin' role, which is the highest level of administrative privilege in SQL Server. The 'name', 'type_desc', and 'is_disabled' columns of the 'sys.server_principals' table provide information about the principal, such as its name, type, and whether it is disabled or not.

**Command** ([[Retrieve server principals with sysadmin role]]):

```bash
SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[Retrieve server principals with sysadmin role]]

## Tags

- [[List All Sysadmins]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]
