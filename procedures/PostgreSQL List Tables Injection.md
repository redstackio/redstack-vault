---
id: 00bd5b96-5709-49d4-825e-eee5b352cea5
name: PostgreSQL List Tables Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.695228+00:00'
updated_at: '2023-04-10T20:23:20.347068+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL List Tables]]'
commands:
- '[[Retrieve table names]]'
---

# PostgreSQL List Tables Injection

## Summary

PostgreSQL List Tables Injection is a technique used to perform an SQL injection attack on a PostgreSQL database in order to obtain a list of all tables in the database. This attack can be used to gather information about the structure and contents of the database. The attacker can then use this in

## Description

# Description

PostgreSQL List Tables Injection is a technique used to perform an SQL injection attack on a PostgreSQL database in order to obtain a list of all tables in the database. This attack can be used to gather information about the structure and contents of the database. The attacker can then use this information to plan further attacks against the database, such as extracting sensitive data or modifying data.

To perform this attack, the attacker injects SQL code into a vulnerable parameter of a web application that interacts with the database. The injected code causes the database to return a list of all tables in the database. This attack can be performed using automated tools or manually.

The business value of this attack is that it allows an attacker to gain valuable information about the database, which can be used to plan further attacks against the organization.

 

## Requirements

1. Access to a vulnerable web application that interacts with the database

1. Knowledge of SQL injection techniques

 

## Defense

1. Use prepared statements and parameterized queries to prevent SQL injection attacks

1. Regularly update and patch the PostgreSQL database to fix known vulnerabilities

1. Implement access controls and user permissions to limit access to sensitive data

 

## Objectives

1. Obtain a list of all tables in the PostgreSQL database

1. Gather information about the structure and contents of the database

1. Plan further attacks against the database

 

# Instructions

1. This command is used to list all tables in the current database.

 



**Code**: [[SELECT table_name FROM information_schema.tables]]



> The SELECT statement is used to retrieve data from one or more tables in a database. In this case, we are selecting the 'table_name' column from the 'information_schema.tables' table. This table contains metadata about all tables in the current database. By executing this command, we can retrieve a list of all tables in the database.



**Command** ([[Retrieve table names]]):

```bash
SELECT table_name FROM information_schema.tables
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Retrieve table names]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL List Tables]]


