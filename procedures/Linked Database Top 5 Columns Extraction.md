---
id: 68ffdd86-c51c-41ed-a132-378cfa289c54
name: Linked Database Top 5 Columns Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.190392+00:00'
updated_at: '2023-04-10T20:36:35.709138+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Gather the Top 5 Columns from a Selected Linked Table]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
---

# Linked Database Top 5 Columns Extraction

## Summary

This procedure is used to extract the top 5 columns from a selected table in a linked database. This can be useful for an attacker to better understand the structure and contents of the linked database. The procedure involves using the Get-Top5RowsFromTable command to retrieve the top 5 rows from t

## Description

# Description

This procedure is used to extract the top 5 columns from a selected table in a linked database. This can be useful for an attacker to better understand the structure and contents of the linked database. The procedure involves using the Get-Top5RowsFromTable command to retrieve the top 5 rows from the selected table, then parsing the output to extract the column names.

From a technical perspective, this procedure leverages the linked database functionality in MSSQL Server to access data from a remote database. The Get-Top5RowsFromTable command is then used to retrieve the top 5 rows from the selected table, which includes the column names and their values. By parsing the output, an attacker can quickly identify the top columns in the table and gain insight into the data stored within.

The business value of this procedure is that it allows an attacker to gain a better understanding of the data stored within a linked database, which can be used to inform further attacks or data exfiltration.

 

## Requirements

1. Access to a linked database in MSSQL Server

1. Ability to execute PowerShell commands on the target system

1. Permission to query the selected table

 

## Defense

1. Restrict access to the linked database to only authorized users

1. Monitor for unusual or suspicious activity, such as repeated queries of the same table

1. Implement network segmentation to limit the impact of a potential compromise of the linked database

 

## Objectives

1. Extract the top 5 columns from a selected table in a linked database

1. Gain insight into the structure and contents of the linked database

 

# Instructions

1. This command retrieves the top 5 rows from a specified table in a database.

 



**Code**: [[Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>"]]



> The 'Get-SQLQuery' command is used to execute a SQL query against a specified database instance. The '-Instance' parameter is used to specify the name of the database server and instance to connect to. The '-Query' parameter is used to specify the SQL query to execute. In this case, the query is retrieving the top 5 rows from a table using the 'TOP' keyword. The 'openquery' function is used to execute the query against a linked server. The name of the linked server is specified using the '<DatabaseLinkName>' placeholder. The name of the database and table to retrieve data from are specified using the '<DatabaseNameFromPreviousCommand>' and '<TableNameFromPreviousCommand>' placeholders respectively. The '-Verbose' parameter is used to display detailed output during the execution of the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]
- [[Remote Services|T1021 - Remote Services]]

## Tags

- [[Gather the Top 5 Columns from a Selected Linked Table]]
- [[Linked Database]]
- [[MSSQL Server]]


