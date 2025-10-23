---
id: 9e79f41a-6268-45f4-bcdb-1249e3cb393b
name: MSSQL List Tables
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.715890+00:00'
updated_at: '2023-04-10T20:22:43.807048+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Hardware Additions|T1200 - Hardware Additions]]'
- '[[Supply Chain Compromise|T1195 - Supply Chain Compromise]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL List tables]]'
---

# MSSQL List Tables

## Summary

MSSQL List Tables is a technique used in MSSQL injection attacks to retrieve a list of tables from a targeted database. This technique involves exploiting vulnerabilities in the database software or web application to execute arbitrary SQL commands. By injecting specially crafted SQL queries, an at

## Description

# Description

MSSQL List Tables is a technique used in MSSQL injection attacks to retrieve a list of tables from a targeted database. This technique involves exploiting vulnerabilities in the database software or web application to execute arbitrary SQL commands. By injecting specially crafted SQL queries, an attacker can bypass authentication and gain access to sensitive data stored in the database. The business value of this technique lies in the ability to obtain valuable data such as customer information, intellectual property, and financial data.

 

## Requirements

1. Access to the target web application or database

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Implement least privilege access controls to limit the impact of a successful attack

 

## Objectives

1. Retrieve a list of tables from a targeted MSSQL database

1. Identify potential targets for further exploitation

 

# Instructions

1. Use the above SQL commands to list database objects. The first command will list all user tables in the current database. The second command will list all user tables in another database. The third command will list column names and types for a specific table. The fourth command will list all tables in all databases. The fifth command will list all user tables in the current database with their names separated by a delimiter of your choice.

 



**Code**: [[SELECT name FROM master..sysobjects WHERE xtype = ]]



> The commands in this JSON object are SQL commands that can be used to list various database objects. The first command will list all user tables in the current database. The second command will list all user tables in another database. The third command will list column names and types for a specific table. The fourth command will list all tables in all databases. The fifth command will list all user tables in the current database with their names separated by a delimiter of your choice.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Hardware Additions|T1200 - Hardware Additions]]
- [[Supply Chain Compromise|T1195 - Supply Chain Compromise]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL List tables]]


