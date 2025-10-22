---
id: 27532978-d3c9-4c8c-9121-88d6a47c4976
name: MYSQL Error Based - NAME_CONST Function Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.530284+00:00'
updated_at: '2023-04-10T20:22:55.875905+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[MYSQL Error Based]]'
- '[[MYSQL Error Based - NAME_CONST function (only for constants)]]'
- '[[MYSQL Injection]]'
commands:
- '[[MySQL version check]]'
---

# MYSQL Error Based - NAME_CONST Function Injection

## Summary

MYSQL Error Based - NAME_CONST function is a type of SQL injection attack that targets the NAME_CONST function in MYSQL databases. This attack can be used to retrieve sensitive information such as usernames, passwords, and other data stored in the database. The NAME_CONST function is used to assign

## Description

# Description

MYSQL Error Based - NAME_CONST function is a type of SQL injection attack that targets the NAME_CONST function in MYSQL databases. This attack can be used to retrieve sensitive information such as usernames, passwords, and other data stored in the database. The NAME_CONST function is used to assign a value to a variable, and the attacker can inject malicious code into this function in order to execute arbitrary SQL commands. This type of attack can be difficult to detect and can result in significant data loss or damage to the target system.

Technical Explanation: The attacker can use the NAME_CONST function to inject malicious SQL code into the database. This code can be used to retrieve sensitive information or to modify the data stored in the database. The attacker can also use this technique to execute arbitrary SQL commands on the target system. The attack can be carried out using tools such as SQLmap or manually by modifying the SQL queries sent to the database.

Business Value: This attack can result in significant data loss or damage to the target system, which can have a negative impact on the business. It can also lead to a loss of customer trust and damage to the company's reputation.

## Requirements

1. Access to the MYSQL database

1. Knowledge of SQL injection techniques

1. SQL injection tool such as SQLmap

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Regularly update and patch the MYSQL database to prevent vulnerabilities

## Objectives

1. Retrieve sensitive information such as usernames, passwords, and other data stored in the database

1. Modify the data stored in the database

1. Execute arbitrary SQL commands on the target system

# Instructions

1. To check the compatibility of MySQL with version &gt;= 5.0, run the following command: 'mysql --version'

**Code**: [[MySQL &gt;= 5.0]]

> This command will display the version of MySQL installed on the system. If the version is greater than or equal to 5.0, then it is compatible with the data provided. If the version is lower than 5.0, then it may not work properly.

**Command** ([[MySQL version check]]):

```bash
mysql --version
```

2. This command can be used to retrieve the MySQL version, user and database name. The command uses SQL injection to execute the query. The query is executed by appending it to the URL after the '?' symbol. The 'id=1' parameter is used to bypass any authentication checks and the query is executed using the 'AND' operator. The 'NAME_CONST' function is used to retrieve the MySQL version, user and database name. The 'x' table name is used to alias the subquery. 

**Code**: [[?id=1 AND (SELECT * FROM (SELECT NAME_CONST(versio]]

> The 'version()' function is used to retrieve the MySQL version. The 'user()' function is used to retrieve the current user. The 'database()' function is used to retrieve the current database name. The '--' symbol is used to comment out the rest of the query and prevent any errors. This command can be used by attackers to gather information about the target system and plan further attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[MySQL version check]]

## Tags

- [[MYSQL Error Based]]
- [[MYSQL Error Based - NAME_CONST function (only for constants)]]
- [[MYSQL Injection]]
