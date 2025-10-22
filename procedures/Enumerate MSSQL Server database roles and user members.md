---
id: 80f66788-169b-462f-8a4e-60a110283c9e
name: Enumerate MSSQL Server database roles and user members
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.929026+00:00'
updated_at: '2023-04-10T20:36:30.362827+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[List All Database Roles]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Query Database Role Members]]'
---

# Enumerate MSSQL Server database roles and user members

## Summary

This procedure allows an attacker to enumerate all database roles and user members on a MSSQL Server. By listing all the database roles and user members, the attacker can identify potential targets for privilege escalation or lateral movement. To execute this procedure, the attacker needs to have v

## Description

# Description

This procedure allows an attacker to enumerate all database roles and user members on a MSSQL Server. By listing all the database roles and user members, the attacker can identify potential targets for privilege escalation or lateral movement. To execute this procedure, the attacker needs to have valid credentials and access to the MSSQL Server. The attacker can use various tools to execute SQL queries on the server, such as SQL Server Management Studio, sqlcmd, or PowerShell.

## Requirements

1. Valid credentials for the MSSQL Server

1. Access to the MSSQL Server

1. Ability to execute SQL queries on the MSSQL Server

## Defense

1. Enforce least privilege by granting only necessary permissions to MSSQL Server users

1. Monitor MSSQL Server logs for suspicious activity, such as failed login attempts or unusual SQL queries

1. Implement network segmentation to limit the exposure of the MSSQL Server to the internet or untrusted networks

## Objectives

1. Enumerate all database roles on the MSSQL Server

1. Enumerate all user members of each database role

# Instructions

1. This command returns a list of all database roles and their members in a SQL Server instance. It uses the sys.database_role_members and sys.database_principals system views to retrieve the necessary information. The result set includes the name of the database role and the name of the database user who is a member of that role. If a role has no members, the result set will show 'No members' instead of a user name.

**Code**: [[SELECT DB1.name AS DatabaseRoleName,
isnull (DB2.n]]

> To use this command, simply copy and paste it into a SQL Server Management Studio query window and execute it. The result set will be displayed in the Results pane. The command can be modified to filter the results based on specific criteria, such as the name of a role or user. For more information on the sys.database_role_members and sys.database_principals system views, refer to the SQL Server documentation.

**Command** ([[Query Database Role Members]]):

```bash
SELECT DB1.name AS DatabaseRoleName,
isnull (DB2.name, 'No members') AS DatabaseUserName
FROM sys.database_role_members AS DRM
RIGHT OUTER JOIN sys.database_principals AS DB1
ON DRM.role_principal_id = DB1.principal_id
LEFT OUTER JOIN sys.database_principals AS DB2
ON DRM.member_principal_id = DB2.principal_id
WHERE DB1.type = 'R'
ORDER BY DB1.name;
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Commands Used

- [[Query Database Role Members]]

## Tags

- [[List All Database Roles]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]
