---
id: 31612c7d-c5d0-4a82-ad78-db8bd9bfb6fe
name: SQLite Injection - Count Tables
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.038195+00:00'
updated_at: '2023-04-10T20:24:31.945675+00:00'
tags:
- '[[Boolean - Count number of tables]]'
- '[[SQLite Injection]]'
---

# SQLite Injection - Count Tables

## Summary

This procedure involves performing a SQLite injection attack to count the number of tables in a database. SQLite injection is a technique used to exploit web applications that use SQLite databases. By injecting malicious SQL code, an attacker can manipulate the database to perform unintended action

## Description

# Description

This procedure involves performing a SQLite injection attack to count the number of tables in a database. SQLite injection is a technique used to exploit web applications that use SQLite databases. By injecting malicious SQL code, an attacker can manipulate the database to perform unintended actions, such as extracting sensitive information. In this case, the attacker is attempting to discover the number of tables in the database.

To perform this attack, the attacker will need to identify a vulnerable web application that uses an SQLite database. They will then use a tool such as sqlmap to automate the injection process and extract the number of tables in the database. This information can be used to further target the database and extract sensitive information.

This procedure can be used by attackers to gain unauthorized access to sensitive information stored in an SQLite database.

## Requirements

1. Access to a vulnerable web application that uses an SQLite database

1. A tool such as sqlmap to automate the injection process

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries to protect against SQL injection attacks

1. Regularly monitor and review database logs for suspicious activity

## Objectives

1. Discover the number of tables in an SQLite database

1. Identify vulnerable web applications that use SQLite databases

1. Extract sensitive information from the database

# Instructions

1. To use this command, replace 'number_of_table' with the maximum number of tables you expect to have in your database. This command will check the number of tables in your database and return true if the number of tables is less than the specified number.

**Code**: [[and (SELECT count(tbl_name) FROM sqlite_master WHE]]

> This command is useful for ensuring that your database has the expected number of tables. If the number of tables in your database is greater than the specified number, it could indicate that there is an issue with your database schema or that there are tables that were not properly deleted. By using this command, you can ensure that your database is in the expected state.

## Tags

- [[Boolean - Count number of tables]]
- [[SQLite Injection]]
