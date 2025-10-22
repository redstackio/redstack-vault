---
id: f00bf17b-74b5-4683-84f4-2e4e942bfe82
name: MSSQL Server - Identify Sensitive Information - Gather Top 5 Entries from a
  Specific Table
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.972682+00:00'
updated_at: '2023-04-10T20:36:38.941589+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Gather 5 Entries from a Specific Table]]'
- '[[Identify Sensitive Information]]'
- '[[MSSQL Server]]'
commands:
- '[[Get Top 5 Rows from a Table]]'
---

# MSSQL Server - Identify Sensitive Information - Gather Top 5 Entries from a Specific Table

## Summary

This procedure allows an attacker to gather sensitive information from a specific table in a MSSQL database. By using the 'Get Top 5 Rows from a SQL Table' command, the attacker can quickly gather the top 5 entries from a table of their choosing. This information can be used to identify potential t

## Description

# Description

This procedure allows an attacker to gather sensitive information from a specific table in a MSSQL database. By using the 'Get Top 5 Rows from a SQL Table' command, the attacker can quickly gather the top 5 entries from a table of their choosing. This information can be used to identify potential targets or to gather additional information for a more targeted attack. From a technical perspective, this procedure involves querying the database and extracting the desired information. From a business perspective, this procedure could be used to gather competitive intelligence or to identify potential vulnerabilities in the database.

## Requirements

1. Access to the MSSQL database

1. Credentials with appropriate permissions

1. Ability to run SQL commands

## Defense

1. Restrict access to the MSSQL database to only authorized users

1. Implement strong password policies and multi-factor authentication

1. Monitor database activity for suspicious behavior

## Objectives

1. Gather sensitive information from a specific table in a MSSQL database

1. Identify potential targets or vulnerabilities

# Instructions

1. This command retrieves the top 5 rows from a specified SQL table.

Arguments:
- DBSERVERNAME\DBInstance: The name of the SQL server and instance where the database resides.
- DatabaseName: The name of the database where the table resides.
- TableName: The name of the table to retrieve data from.

**Code**: [[Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>"]]

> The Get-SQLQuery command is used to retrieve data from a SQL database. In this case, we are using it to retrieve the top 5 rows from a specified table. The -Instance parameter specifies the server and instance where the database resides. The -Query parameter is used to specify the SQL query to execute. In this case, we are using the SELECT TOP 5 statement to retrieve only the top 5 rows from the table. The * symbol is used to specify all columns in the table. The <DatabaseName> and <TableName> placeholders should be replaced with the actual names of the database and table, respectively.

**Command** ([[Get Top 5 Rows from a Table]]):

```bash
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query 'select TOP 5 * from <DatabaseName>.dbo.<TableName>'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get Top 5 Rows from a Table]]

## Tags

- [[Gather 5 Entries from a Specific Table]]
- [[Identify Sensitive Information]]
- [[MSSQL Server]]
