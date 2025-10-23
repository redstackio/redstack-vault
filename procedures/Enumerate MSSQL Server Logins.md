---
id: 2f865ca6-656d-4bae-8804-9cedc1dccdff
name: Enumerate MSSQL Server Logins
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.847194+00:00'
updated_at: '2023-04-10T20:36:42.853427+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]'
tags:
- '[[All Logins on Server]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Query sys.server_principals table]]'
---

# Enumerate MSSQL Server Logins

## Summary

This procedure involves executing a manual SQL query to enumerate all the logins on an MSSQL server. This information can be useful for identifying potential targets for further exploitation or for auditing purposes. To execute this query, the user needs to have appropriate permissions on the serve

## Description

# Description

This procedure involves executing a manual SQL query to enumerate all the logins on an MSSQL server. This information can be useful for identifying potential targets for further exploitation or for auditing purposes. To execute this query, the user needs to have appropriate permissions on the server. The technical details of the query involve selecting information from the 'sys.server_principals' table. The business value of this procedure is that it can help organizations identify potential security risks and take appropriate measures to mitigate them.

 

## Requirements

1. Authenticated access to the MSSQL server

1. Appropriate permissions to execute the query

 

## Defense

1. Ensure that only authorized users have access to the MSSQL server

1. Regularly review and audit the logins on the server to identify potential security risks

1. Implement strong password policies for all logins

 

## Objectives

1. Identify all logins on an MSSQL server

1. Assess the security risks associated with each login

 

# Instructions

1. To retrieve information about server principals, use the following SQL query:

 



**Code**: [[Select * from sys.server_principals where type_des]]



> This query retrieves information about all server principals, except for those that are server roles. The result set includes details such as the principal's name, type, authentication type, and permission information.



**Command** ([[Query sys.server_principals table]]):

```bash
Select * from sys.server_principals where type_desc != 'SERVER_ROLE'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]

## Commands Used

- [[Query sys.server_principals table]]

## Tags

- [[All Logins on Server]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]


