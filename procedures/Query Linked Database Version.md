---
id: ddd0e1c8-818f-43cb-adbf-47fa26a578d4
name: Query Linked Database Version
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.110942+00:00'
updated_at: '2023-04-10T20:36:45.010007+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Linked Database]]'
- '[[MSSQL Server]]'
- '[[Query Version of Linked Database]]'
---

# Query Linked Database Version

## Summary

The Query Linked Database Version procedure involves querying the version of a linked database in an MSSQL Server environment. This information can be used to identify vulnerabilities and determine potential attack vectors. To execute this procedure, the user must have access to the linked database

## Description

# Description

The Query Linked Database Version procedure involves querying the version of a linked database in an MSSQL Server environment. This information can be used to identify vulnerabilities and determine potential attack vectors. To execute this procedure, the user must have access to the linked database and the necessary permissions to execute the 'Get SQL Server Version' command. 

From a technical perspective, this procedure involves executing a SQL query against the linked database to retrieve its version information. The business value of this procedure is that it allows organizations to proactively identify and remediate vulnerabilities in their MSSQL Server environments.

 

## Requirements

1. Valid credentials with the necessary permissions to execute the 'Get SQL Server Version' command

1. Access to the linked database

 

## Defense

1. Ensure that only authorized personnel have access to the MSSQL Server environment and the linked database

1. Implement proper access control measures to prevent unauthorized access to the linked database

1. Regularly monitor the MSSQL Server environment for suspicious activity

 

## Objectives

1. Retrieve version information for a linked database

1. Identify potential vulnerabilities in the MSSQL Server environment

 

# Instructions

1. This command is used to retrieve the version of the SQL Server running on the specified instance. The command requires the following arguments:
- <DBSERVERNAME\DBInstance>: The name of the SQL Server instance you want to retrieve the version for.

Example usage: Get-SQLQuery -Instance "MyDBServer\SQLEXPRESS" -Query "select * from openquery(`"MyDBServer\SQLEXPRESS`",'select @@version')" -Verbose

 



**Code**: [[Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>"]]



> The Get-SQLQuery command is used to execute a SQL query against a specified SQL Server instance. In this case, the query being executed is "select @@version", which returns the version of the SQL Server instance. The -Instance parameter is used to specify the name of the SQL Server instance to connect to. The -Query parameter is used to specify the SQL query to execute. The -Verbose parameter is optional and will display detailed information about the execution of the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[Linked Database]]
- [[MSSQL Server]]
- [[Query Version of Linked Database]]


