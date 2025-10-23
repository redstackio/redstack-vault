---
id: 7e89b582-71cb-45bb-9086-539c72ce75cf
name: PostgreSQL List Columns Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.724518+00:00'
updated_at: '2023-04-10T20:23:22.469461+00:00'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL List Columns]]'
commands:
- '[[Retrieve Column Names]]'
---

# PostgreSQL List Columns Injection

## Summary

PostgreSQL List Columns Injection is a technique used to gather information about the database schema. This technique can be used to enumerate the names of columns in a specific table or view. This information can be used to aid in further attacks such as data exfiltration or privilege escalation. 

## Description

# Description

PostgreSQL List Columns Injection is a technique used to gather information about the database schema. This technique can be used to enumerate the names of columns in a specific table or view. This information can be used to aid in further attacks such as data exfiltration or privilege escalation. 

To execute this technique, an attacker can inject a specially crafted query into an input field that is not properly sanitized. This query will cause the database to return the names of columns in the specified table. 

This technique can be valuable to an attacker as it provides insight into the structure of the database, which can be used to plan further attacks or to gather sensitive information.

 

## Requirements

1. Access to a vulnerable PostgreSQL database

 

## Defense

1. Implement input validation to prevent injection attacks

1. Use prepared statements to prevent injection attacks

1. Enforce principle of least privilege by limiting database user permissions

 

## Objectives

1. Enumerate the names of columns in a specific table or view

 

# Instructions

1. To retrieve the column names of a specific table in the database, use this SQL query. Replace 'data_table' with the name of the table you want to retrieve the column names from.

 



**Code**: [[SELECT column_name FROM information_schema.columns]]



> This command retrieves the column names of a specified table in the database. The 'information_schema.columns' table contains information about all columns in all tables in a database. By specifying the table name in the WHERE clause, we can retrieve only the column names for that specific table.



**Command** ([[Retrieve Column Names]]):

```bash
SELECT column_name FROM information_schema.columns WHERE table_name='data_table'
```



## Commands Used

- [[Retrieve Column Names]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL List Columns]]


