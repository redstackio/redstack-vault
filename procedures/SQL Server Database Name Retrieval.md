---
id: a869171c-0416-4e7c-8a40-33aea9201948
name: SQL Server Database Name Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.776308+00:00'
updated_at: '2023-04-10T20:36:33.881118+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Current DB]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Select current database name]]'
---

# SQL Server Database Name Retrieval

## Summary

This procedure involves manually querying the SQL Server to retrieve the name of the current database. This information can be used to identify the target's environment and plan further attacks. To retrieve the current database name, the attacker can use the 'Retrieve Current Database Name' command

## Description

# Description

This procedure involves manually querying the SQL Server to retrieve the name of the current database. This information can be used to identify the target's environment and plan further attacks. To retrieve the current database name, the attacker can use the 'Retrieve Current Database Name' command. This technique can be used as part of the initial reconnaissance phase of an attack.

 

## Requirements

1. Access to the SQL Server.

 

## Defense

1. Ensure that the SQL Server is properly secured with strong authentication mechanisms and access controls.

1. Monitor for any unusual queries or activity on the SQL Server.

1. Regularly review and update the security policies and configurations of the SQL Server.

 

## Objectives

1. Retrieve the name of the current database on the target SQL Server.

 

# Instructions

1. This command retrieves the name of the current database being used.

 



**Code**: [[select db_name()]]



> The 'select db_name()' command is used to retrieve the name of the current database being used. This can be useful when working with multiple databases and needing to ensure that the correct database is being used for a given task.



**Command** ([[Select current database name]]):

```bash
select db_name()
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Select current database name]]

## Tags

- [[Current DB]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]


