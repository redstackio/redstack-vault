---
id: f733ba0b-7216-4b6c-9890-b64c37c99bd9
name: Linked Database Column Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.215337+00:00'
updated_at: '2023-04-10T20:36:40.297040+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Gather Entries from a Selected Linked Column]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
---

# Linked Database Column Extraction

## Summary

Linked Database Column Extraction is a technique used to gather entries from a selected linked column in a SQL Server database. This technique can be used to extract sensitive information such as usernames, passwords, and other credential information. An attacker can use this technique to gain unau

## Description

# Description

Linked Database Column Extraction is a technique used to gather entries from a selected linked column in a SQL Server database. This technique can be used to extract sensitive information such as usernames, passwords, and other credential information. An attacker can use this technique to gain unauthorized access to a database, and can then use the information obtained to escalate their privileges and gain further access to the target system.

To execute this technique, an attacker would need to have access to a SQL Server instance that has a linked server configured. They would then need to execute a query against the linked server to extract the desired information. This technique can be used to bypass network segmentation and access data on a remote system.

The business value of this technique lies in the ability of an attacker to obtain sensitive information that can be used to further compromise a system. By gaining access to a database, an attacker can potentially obtain access to confidential information such as customer data, financial data, and intellectual property.

 

## Requirements

1. Access to a SQL Server instance with a linked server configured

1. Ability to execute a query against the linked server

 

## Defense

1. Configure proper access controls and permissions for SQL Server instances and linked servers

1. Use network segmentation to limit access to sensitive systems and data

1. Monitor for unauthorized access and unusual database activity

 

## Objectives

1. Extract sensitive information from a linked database column

1. Gain unauthorized access to a database

1. Escalate privileges to gain further access to the target system

 

# Instructions

1. This command retrieves SQL query results from a linked server. The command requires the following parameters:
1. DBSERVERNAME\DBInstance: The name of the SQL Server instance.
2. DatabaseLinkName: The name of the linked server.
3. DatabaseNameFromPreviousCommand: The name of the database from the previous command.
4. TableNameFromPreviousCommand: The name of the table from the previous command.
5. ColumnNameFromPreviousCommand: The name of the column from the previous command.
6. ColumnValueFromPreviousCommand: The value of the column from the previous command.

 



**Code**: [[Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>"]]



> This command uses the Get-SQLQuery cmdlet to retrieve SQL query results from a linked server. The command includes the instance name, the name of the linked server, and the SQL query to execute. The SQL query includes a reference to the database, table, column, and value from the previous command. The results of the query are returned as a table.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Tags

- [[Gather Entries from a Selected Linked Column]]
- [[Linked Database]]
- [[MSSQL Server]]


