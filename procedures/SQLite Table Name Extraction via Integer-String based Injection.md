---
id: 12475944-e98e-420a-9f82-a429b7faad65
name: SQLite Table Name Extraction via Integer/String based Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.003189+00:00'
updated_at: '2023-04-10T20:24:32.645255+00:00'
tags:
- '[[Integer/String based - Extract table name]]'
- '[[SQLite Injection]]'
---

# SQLite Table Name Extraction via Integer/String based Injection

## Summary

SQLite is a popular database management system used in a variety of applications. However, it is vulnerable to SQL injection attacks that can be used to extract data from the database. In this procedure, an attacker can extract table names using integer/string based injection. This can be used to i

## Description

# Description

SQLite is a popular database management system used in a variety of applications. However, it is vulnerable to SQL injection attacks that can be used to extract data from the database. In this procedure, an attacker can extract table names using integer/string based injection. This can be used to identify tables that contain sensitive information, and can also be used as a stepping stone for further attacks.

SQLite databases are commonly used in mobile applications, and extracting table names can provide valuable information for attackers looking to steal data or compromise the application. The attacker can use various injection techniques to extract table names, including integer and string based injection. By manipulating the input to the application, the attacker can cause the application to execute SQL queries that reveal the names of the tables in the database.

The business value of this attack lies in the ability to extract sensitive information from an application's database. This can include user credentials, financial information, and other sensitive data that can be used for further attacks or sold on the black market.

## Requirements

1. Access to the application that uses SQLite as its database management system

1. Knowledge of SQL injection techniques

1. Ability to manipulate input to the application

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries to prevent injection attacks

1. Limit access to the database and its tables to only authorized users

## Objectives

1. Extract table names from the SQLite database

1. Identify tables that contain sensitive information

1. Use extracted table names as a stepping stone for further attacks

# Instructions

1. This command lists all the tables present in the SQLite database.

**Code**: [[SELECT tbl_name FROM sqlite_master WHERE type='tab]]

> The 'SELECT' statement is used to retrieve data from one or more tables in the database. In this case, we are selecting the 'tbl_name' column from the 'sqlite_master' table. The 'WHERE' clause is used to filter the results based on a condition. Here, we are only selecting tables whose type is 'table' and whose name does not start with 'sqlite_'.

## Tags

- [[Integer/String based - Extract table name]]
- [[SQLite Injection]]
