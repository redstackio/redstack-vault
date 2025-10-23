---
id: f6e83705-b8ba-4f4c-a4dd-5b9aa58ba685
name: Linked Database Table Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.171055+00:00'
updated_at: '2023-04-10T20:36:35.208000+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Input Capture|T1056 - Input Capture]]'
tags:
- '[[Determine All the Tables Names from a Selected Linked Database]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
---

# Linked Database Table Enumeration

## Summary

This procedure enables an attacker to enumerate all the tables names from a selected linked database in a MSSQL Server. The attacker can use this information to identify potential targets for further exploitation. To execute this procedure, the attacker must have access to a linked database and ret

## Description

# Description

This procedure enables an attacker to enumerate all the tables names from a selected linked database in a MSSQL Server. The attacker can use this information to identify potential targets for further exploitation. To execute this procedure, the attacker must have access to a linked database and retrieve SQL query results from it. By using the 'Retrieve SQL Query Results from Linked Server' command, the attacker can execute a query that retrieves all the table names from the linked database. This procedure can be used to gather valuable information about the target's infrastructure and data.

 

## Requirements

1. Access to a linked database

1. Ability to retrieve SQL query results from the linked database

 

## Defense

1. Limit access to linked databases to authorized users only

1. Monitor for suspicious activity related to linked databases and SQL queries

1. Implement network segmentation to limit the impact of a compromised linked database

 

## Objectives

1. Enumerate all the tables names from a selected linked database

1. Identify potential targets for further exploitation

 

# Instructions

1. This command retrieves SQL query results from a linked server. It requires the instance name of the database server and the name of the linked server to be specified as arguments. The query to be executed is also required and can be passed as a string argument. The results of the query are returned as a table.

 



**Code**: [[Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>"]]



> The 'Get-SQLQuery' command is used to retrieve SQL query results from a linked server. The '-Instance' parameter is used to specify the instance name of the database server. The '-Query' parameter is used to specify the query to be executed. The query is passed as a string argument and can include placeholders for variables. In this case, the query is selecting the names of all tables in a specific database on the linked server. The '-Verbose' parameter is optional and can be used to display additional information about the execution of the command. The command returns the results of the query as a table, which can be further processed or displayed as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Input Capture|T1056 - Input Capture]]

## Tags

- [[Determine All the Tables Names from a Selected Linked Database]]
- [[Linked Database]]
- [[MSSQL Server]]


