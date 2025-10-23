---
id: c90306e8-09b2-44ab-a17f-9e0eb568cbba
name: Oracle SQL Column Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.205410+00:00'
updated_at: '2023-04-10T20:23:10.715048+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Oracle SQL Injection]]'
- '[[Oracle SQL List Columns]]'
commands:
- '[[Retrieve column names for table ''blah'']]'
- '[[Retrieve column names for table ''blah'' owned by ''foo'']]'
---

# Oracle SQL Column Enumeration

## Summary

Oracle SQL Column Enumeration is a technique used to extract column names from a table using SQL injection. This technique is commonly used by attackers to identify sensitive information such as usernames, passwords, and other confidential data stored in a database. To perform this technique, the a

## Description

# Description

Oracle SQL Column Enumeration is a technique used to extract column names from a table using SQL injection. This technique is commonly used by attackers to identify sensitive information such as usernames, passwords, and other confidential data stored in a database. To perform this technique, the attacker injects specially crafted SQL queries into the vulnerable application to extract the column names from the database. This technique can be used to perform reconnaissance and identify potential targets for further exploitation. 

From a technical perspective, this technique exploits the vulnerability in the application that allows untrusted input to be executed as part of a SQL query. By injecting a specially crafted query, the attacker can manipulate the behavior of the application and extract sensitive information. 

From a business perspective, this technique can be used to identify potential targets for further exploitation. It can also be used to identify sensitive data that may be at risk of compromise.

 

## Requirements

1. Access to a vulnerable application

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection vulnerabilities

1. Regularly update and patch vulnerable applications

1. Implement database access control mechanisms to prevent unauthorized access to sensitive information

 

## Objectives

1. Identify column names from a table using SQL injection

1. Perform reconnaissance to identify potential targets for further exploitation

1. Identify sensitive information stored in a database

 

# Instructions

1. To retrieve the column names of a table, use the following SQL query:
SELECT column_name FROM all_tab_columns WHERE table_name = 'table_name';
To retrieve the column names of a table owned by a specific user, use the following SQL query:
SELECT column_name FROM all_tab_columns WHERE table_name = 'table_name' and owner = 'owner_name';

 



**Code**: [[SELECT column_name FROM all_tab_columns WHERE tabl]]



> The 'all_tab_columns' view contains information about all tables, views and synonyms that are accessible to the current user.
The 'table_name' argument specifies the name of the table whose columns you want to retrieve.
The 'owner' argument specifies the name of the user who owns the table. If not specified, it will retrieve the columns of all tables with the specified name regardless of the owner.



**Command** ([[Retrieve column names for table 'blah']]):

```bash
SELECT column_name FROM all_tab_columns WHERE table_name = 'blah';
```





**Command** ([[Retrieve column names for table 'blah' owned by 'foo']]):

```bash
SELECT column_name FROM all_tab_columns WHERE table_name = 'blah' and owner = 'foo';
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Retrieve column names for table 'blah']]
- [[Retrieve column names for table 'blah' owned by 'foo']]

## Tags

- [[Oracle SQL Injection]]
- [[Oracle SQL List Columns]]


