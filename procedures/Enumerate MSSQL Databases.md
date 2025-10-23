---
id: 2f7cad72-2762-4191-9c98-b70c3c058757
name: Enumerate MSSQL Databases
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.823541+00:00'
updated_at: '2023-04-10T20:36:33.171505+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[List all databases]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Retrieve database names]]'
---

# Enumerate MSSQL Databases

## Summary

The 'Enumerate MSSQL Databases' procedure is used to discover all available databases on a MSSQL server. This information can be used by an attacker to identify valuable data and plan further attacks. To enumerate the databases, the user can execute a simple SQL query that retrieves the names of al

## Description

# Description

The 'Enumerate MSSQL Databases' procedure is used to discover all available databases on a MSSQL server. This information can be used by an attacker to identify valuable data and plan further attacks. To enumerate the databases, the user can execute a simple SQL query that retrieves the names of all databases on the server. This can be done manually through a SQL client or automated through a script.

From a technical standpoint, the procedure relies on the ability to connect to the MSSQL server and execute SQL queries. The attacker needs to have valid credentials or exploit a vulnerability to gain access to the server. The procedure can be run from a compromised host or directly from the attacker's machine if network access is available.

The business value of this procedure lies in the fact that it enables the attacker to identify the most valuable targets for further attacks. By knowing which databases are present on the server, the attacker can focus on those that contain sensitive information, such as customer data, financial records, or intellectual property.

 

## Requirements

1. Valid credentials or exploit to gain access to the MSSQL server

1. Ability to execute SQL queries

 

## Defense

1. Ensure that the MSSQL server is properly secured and up-to-date with the latest patches

1. Use strong and unique credentials for all MSSQL accounts

1. Monitor network traffic for suspicious activity and SQL injection attempts

 

## Objectives

1. Discover all available MSSQL databases

1. Identify valuable data for further attacks

 

# Instructions

1. To list all available databases, execute the following SQL query:

 



**Code**: [[select name from master..sysdatabases]]



> This command retrieves the names of all databases present in the SQL Server instance.



**Command** ([[Retrieve database names]]):

```bash
select name from master..sysdatabases
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Retrieve database names]]

## Tags

- [[List all databases]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]


