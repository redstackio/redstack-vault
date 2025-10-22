---
id: e638b29e-490a-4140-8350-4842f131c657
name: Oracle SQL List Tables and Columns
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.244903+00:00'
updated_at: '2023-04-10T20:23:09.929027+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[Oracle SQL Injection]]'
- '[[Oracle SQL List Tables]]'
commands:
- '[[List all tables]]'
- '[[List tables with owner]]'
- '[[List tables with owner and columns with ''PASS'']]'
---

# Oracle SQL List Tables and Columns

## Summary

Oracle SQL List Tables and Columns is a technique used to extract information from an Oracle database using SQL injection. Attackers use this technique to obtain information about the database schema, including the names of tables and columns. This information can be used to identify valuable data 

## Description

# Description

Oracle SQL List Tables and Columns is a technique used to extract information from an Oracle database using SQL injection. Attackers use this technique to obtain information about the database schema, including the names of tables and columns. This information can be used to identify valuable data and plan further attacks. The attack starts with identifying a vulnerable input field that can be used to inject malicious SQL code. Once the code is executed, the output is parsed to extract the desired information. This technique can be used to obtain sensitive information such as usernames, passwords, and other credentials.

From a technical perspective, this technique relies on the ability to inject SQL code into a vulnerable input field. The attacker needs to have an understanding of the database schema to identify the tables and columns they wish to extract information from. The output of the injection needs to be parsed to extract the relevant information.

From a business perspective, this technique can be used to obtain sensitive information that can be used to further compromise the system or steal valuable data. It is important to ensure that input validation is performed to prevent SQL injection attacks.

## Requirements

1. Access to a vulnerable input field that can be used to inject SQL code

1. Understanding of the database schema

## Defense

1. Perform input validation to prevent SQL injection attacks

1. Use parameterized queries to avoid SQL injection vulnerabilities

1. Monitor logs for suspicious activity related to database queries

## Objectives

1. Extract information about the database schema

1. Identify valuable data for further attacks

# Instructions

1. This command lists all tables in the database and then lists the owner and table name for each table. It then lists the owner, table name, and columns that contain the word 'PASS' in their name. This can be useful for identifying tables and columns that may contain sensitive information such as passwords.

**Code**: [[SELECT table_name FROM all_tables;
SELECT owner, t]]

> The first SELECT statement retrieves a list of all table names in the database. The second SELECT statement retrieves the owner and table name for each table in the database. The third SELECT statement retrieves the owner, table name, and columns that contain the word 'PASS' in their name. The WHERE clause filters the results to only include columns with 'PASS' in their name.

**Command** ([[List all tables]]):

```bash
SELECT table_name FROM all_tables;
```

**Command** ([[List tables with owner]]):

```bash
SELECT owner, table_name FROM all_tables;
```

**Command** ([[List tables with owner and columns with 'PASS']]):

```bash
SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%';
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Commands Used

- [[List all tables]]
- [[List tables with owner]]
- [[List tables with owner and columns with 'PASS']]

## Tags

- [[Oracle SQL Injection]]
- [[Oracle SQL List Tables]]
