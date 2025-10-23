---
id: a22b42b3-365a-472d-9299-24c8a53e8294
name: PostgreSQL Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.573427+00:00'
updated_at: '2023-04-10T20:23:16.856151+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL List Privileges]]'
commands:
- '[[Retrieve user information from PostgreSQL database]]'
---

# PostgreSQL Privilege Escalation

## Summary

PostgreSQL Privilege Escalation is a technique used by attackers to gain higher privileges on a PostgreSQL database by exploiting vulnerabilities in the database. Attackers can use this technique to gain access to sensitive data and perform unauthorized actions. This technique can be achieved by in

## Description

# Description

PostgreSQL Privilege Escalation is a technique used by attackers to gain higher privileges on a PostgreSQL database by exploiting vulnerabilities in the database. Attackers can use this technique to gain access to sensitive data and perform unauthorized actions. This technique can be achieved by injecting malicious SQL code into the database. Once the attacker has gained higher privileges, they can perform a variety of actions such as extracting data, modifying data, or deleting data. The business value of this technique is that it can help attackers gain access to sensitive data, which can be used for financial gain or to damage the reputation of the targeted organization.

 

## Requirements

1. Access to the PostgreSQL database

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Regularly patch and update the PostgreSQL database to mitigate known vulnerabilities

1. Implement access controls to limit privileges of users and prevent privilege escalation

 

## Objectives

1. Gain higher privileges on a PostgreSQL database

1. Perform unauthorized actions on the database

1. Extract sensitive data from the database

 

# Instructions

1. This command lists all the users in a PostgreSQL database along with their privileges.

 



**Code**: [[SELECT usename, usecreatedb, usesuper, usecatupd F]]



> The 'SELECT' statement is used to query the 'pg_user' table in the PostgreSQL database. This table contains information about all the users in the database. The 'usename' field lists the username of each user, while the 'usecreatedb', 'usesuper', and 'usecatupd' fields list the privileges of each user. 'usecreatedb' indicates whether the user is allowed to create new databases, 'usesuper' indicates whether the user is a superuser, and 'usecatupd' indicates whether the user is allowed to modify system catalogs. This command can be useful for administrators who need to manage user privileges or troubleshoot issues with user accounts.



**Command** ([[Retrieve user information from PostgreSQL database]]):

```bash
SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Retrieve user information from PostgreSQL database]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL List Privileges]]


