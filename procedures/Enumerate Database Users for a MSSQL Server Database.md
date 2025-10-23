---
id: da63583f-2adb-4837-a67c-50789f182ccf
name: Enumerate Database Users for a MSSQL Server Database
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.878093+00:00'
updated_at: '2023-04-10T20:36:41.700687+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[All Database Users for a Database]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
---

# Enumerate Database Users for a MSSQL Server Database

## Summary

This procedure aims to enumerate all the database users for a specific database in a MSSQL Server. This information can be used to identify potential targets for further exploitation or lateral movement. To execute this procedure, the user needs to have valid authentication credentials for the MSSQ

## Description

# Description

This procedure aims to enumerate all the database users for a specific database in a MSSQL Server. This information can be used to identify potential targets for further exploitation or lateral movement. To execute this procedure, the user needs to have valid authentication credentials for the MSSQL Server and the specific database. The user can execute a manual SQL query to retrieve the database users information. The query returns a list of all database users, their type, and their authentication type. Business value of this procedure is to identify potential targets for further exploitation or lateral movement.

 

## Requirements

1. Valid authentication credentials for the MSSQL Server and the specific database.

1. Access to execute a manual SQL query.

 

## Defense

1. Implement the principle of least privilege, and ensure that users have only the necessary permissions required to perform their job functions.

1. Regularly review and audit MSSQL Server logs to detect any suspicious activity, such as failed login attempts or unusual queries.

1. Use network segmentation to limit access to MSSQL Server instances to only authorized users and systems.

 

## Objectives

1. Enumerate all the database users for a specific database in a MSSQL Server.

 

# Instructions

1. This command retrieves the list of database principals that are not database roles.

 



**Code**: [[Select * from sys.database_principals where type_d]]



> The 'sys.database_principals' table contains a list of all database principals in the current database. This command filters out the principals that are database roles and returns the remaining principals. The 'type_desc' column in the table indicates whether a principal is a user, a role, or another type of principal. By excluding the principals that are database roles, this command provides a list of all users and other non-role principals in the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Tags

- [[All Database Users for a Database]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]


