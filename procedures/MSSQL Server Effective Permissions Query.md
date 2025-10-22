---
id: b1894b1e-e024-480a-86b0-3e5f0ae148c7
name: MSSQL Server Effective Permissions Query
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.988809+00:00'
updated_at: '2023-04-10T20:36:36.827450+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[Effective Permissions from the Database]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
---

# MSSQL Server Effective Permissions Query

## Summary

The MSSQL Server Effective Permissions Query allows an attacker to determine the level of access a user has to a specific database. By running the 'List Database Permissions' command, the attacker can retrieve a list of all permissions granted to a specific user. This information can be used to ide

## Description

# Description

The MSSQL Server Effective Permissions Query allows an attacker to determine the level of access a user has to a specific database. By running the 'List Database Permissions' command, the attacker can retrieve a list of all permissions granted to a specific user. This information can be used to identify high-value targets and to plan further attacks against the database. With this information, an attacker can escalate privileges and gain access to sensitive data. 

To execute this query, the attacker needs to have valid credentials for the database. Once authenticated, the attacker can execute the 'List Database Permissions' command to retrieve the necessary information. 

The business value of this procedure is that it allows an attacker to identify weaknesses in the database's security and take corrective action to prevent further attacks.

## Requirements

1. Valid credentials for the database

## Defense

1. Ensure that all credentials for the database are strong and complex

1. Monitor the database for any unusual activity or access attempts

1. Implement access controls and limit the number of users who have access to sensitive data

## Objectives

1. Identify the level of access a user has to a specific database

1. Plan further attacks against the database

1. Escalate privileges and gain access to sensitive data

# Instructions

1. This command lists all the permissions associated with a database. The output will contain details such as the name of the user, the type of permission they have, and the object they have permission on.

**Code**: [[SELECT * FROM fn_dp1my_permissions(NULL, 'DATABASE]]

> The first argument of the function is the name of the user whose permissions you want to list. If you pass NULL, it will list permissions for all users. The second argument is the type of object you want to list permissions for. In this case, we are listing permissions for a database. You can replace 'DATABASE' with other object types such as 'TABLE' or 'VIEW'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]

## Tags

- [[Effective Permissions from the Database]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]
