---
id: 957d1175-fa46-48d2-85b8-ba46d932e1da
name: PostgreSQL Error Based Injection for Database and Table Information Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.743098+00:00'
updated_at: '2023-04-10T20:23:15.213133+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[PostgreSQL Error Based]]'
- '[[PostgreSQL injection]]'
---

# PostgreSQL Error Based Injection for Database and Table Information Retrieval

## Summary

PostgreSQL Error Based Injection is a technique used to extract sensitive information from a PostgreSQL database. This technique involves injecting malicious SQL code into a PostgreSQL query to cause the database to generate an error message that contains sensitive information. The attacker can the

## Description

# Description

PostgreSQL Error Based Injection is a technique used to extract sensitive information from a PostgreSQL database. This technique involves injecting malicious SQL code into a PostgreSQL query to cause the database to generate an error message that contains sensitive information. The attacker can then use this information to gain a better understanding of the database structure and data. This technique can be used to extract information such as database and table names, user names and passwords, and other sensitive information.

From an offensive standpoint, this technique can be used to gain access to sensitive data stored within a PostgreSQL database. From a technical perspective, this technique involves injecting malicious SQL code into a query that causes the database to generate an error message. From a business perspective, this technique can be used to identify and mitigate security risks associated with PostgreSQL databases.

## Requirements

1. Access to a PostgreSQL database

1. Knowledge of SQL injection techniques

## Defense

1. Ensure that all user input is properly sanitized to prevent SQL injection attacks

1. Implement proper access controls to limit database access to authorized users

1. Regularly monitor database activity for suspicious behavior

## Objectives

1. Retrieve database and table information from a PostgreSQL database

1. Identify potential security risks associated with PostgreSQL databases

# Instructions

1. This command is used to retrieve information about the database and tables. The 'data_offset' parameter is used to specify the offset for the data to be retrieved. The 'data_table' parameter is used to specify the name of the table to retrieve information from. The 'data_column' parameter is used to specify the column of the table to retrieve data from.

**Code**: [[,cAsT(chr(126)||vErSiOn()||chr(126)+aS+nUmeRiC)
,c]]

> The command works by injecting SQL code into a vulnerable web application. The injected code retrieves the database version, table names, column names, and data from the specified table and column. The retrieved data is returned as a response to the injected code. The 'data_offset' parameter is used to retrieve data in chunks, as the command limits the amount of data that can be retrieved at once. The retrieved data can be used for further exploitation of the web application.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[PostgreSQL Error Based]]
- [[PostgreSQL injection]]
