---
id: f5555197-62cd-45cd-b344-49038113cc4a
name: MSSQL Server - Identify Sensitive Information - Get Tables and Column Details
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.917908+00:00'
updated_at: '2023-04-10T20:36:30.027871+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Get Tables from a Specific Database]]'
- '[[Identify Sensitive Information]]'
- '[[MSSQL Server]]'
commands:
- '[[Get Column Details from a Table]]'
- '[[Get SQL Tables from a Database]]'
---

# MSSQL Server - Identify Sensitive Information - Get Tables and Column Details

## Summary

This procedure is used to identify sensitive information stored in a MSSQL database. By using the 'Get Tables from a Specific Database' command along with 'Get Column Details from a Table', the user can quickly identify tables and columns that contain sensitive information such as usernames, passwo

## Description

# Description

This procedure is used to identify sensitive information stored in a MSSQL database. By using the 'Get Tables from a Specific Database' command along with 'Get Column Details from a Table', the user can quickly identify tables and columns that contain sensitive information such as usernames, passwords, or other confidential data. This can be useful for both offensive and defensive purposes, allowing the user to identify potential attack vectors or areas of the database that require additional security measures.

Technical Explanation: The 'Get Tables from a Specific Database' command is used to retrieve a list of all tables within a specified database. The 'Get Column Details from a Table' command is then used to retrieve information about the columns within each table, including data type and whether or not the column is nullable. By analyzing this information, the user can identify tables and columns that contain sensitive information.

Business Value: By identifying sensitive information stored in a MSSQL database, organizations can take steps to better secure their data and prevent potential data breaches. This can help to protect sensitive information such as customer data, financial information, and intellectual property.

 

## Requirements

1. Access to a MSSQL database

1. Valid credentials with appropriate permissions

 

## Defense

1. Ensure that MSSQL databases are properly secured with strong authentication and access controls

1. Encrypt sensitive data stored in MSSQL databases to protect against unauthorized access

1. Regularly audit MSSQL databases for vulnerabilities and misconfigurations

 

## Objectives

1. Identify tables and columns that contain sensitive information

1. Assess the security posture of a MSSQL database

1. Identify potential attack vectors

 

# Instructions

1. To get column details from a table, use the following commands:
1. Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DBNameFromGet-SQLDatabaseCommand> -NoDefaults
2. Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName <DBName> -TableName <TableName>


 



**Code**: [[Get-SQLInstanceDomain | Get-SQLTable -DatabaseName]]



> This command will retrieve the column details of a specified table in a specified database. The first command will retrieve the database name from the Get-SQLDatabase command and the second command will retrieve the column details from the specified table. Replace <DBNameFromGet-SQLDatabaseCommand> with the database name retrieved from the first command and replace <DBName> and <TableName> with the name of the database and table you want to retrieve the column details from.



**Command** ([[Get SQL Tables from a Database]]):

```bash
Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DBNameFromGet-SQLDatabaseCommand> -NoDefaults
```





**Command** ([[Get Column Details from a Table]]):

```bash
Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName <DBName> -TableName <TableName>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get Column Details from a Table]]
- [[Get SQL Tables from a Database]]

## Tags

- [[Get Tables from a Specific Database]]
- [[Identify Sensitive Information]]
- [[MSSQL Server]]


