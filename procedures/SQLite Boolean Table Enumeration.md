---
id: 1bfb8099-1bec-4c67-934b-f137ac970012
name: SQLite Boolean Table Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.055399+00:00'
updated_at: '2023-04-10T20:24:30.423621+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Boolean - Enumerating table name]]'
- '[[SQLite Injection]]'
---

# SQLite Boolean Table Enumeration

## Summary

SQLite Boolean Table Enumeration is an injection technique that allows an attacker to enumerate table names within an SQLite database using a boolean-based SQL injection attack. This technique is useful when the attacker has limited knowledge of the database schema and wants to discover the names o

## Description

# Description

SQLite Boolean Table Enumeration is an injection technique that allows an attacker to enumerate table names within an SQLite database using a boolean-based SQL injection attack. This technique is useful when the attacker has limited knowledge of the database schema and wants to discover the names of tables that may contain sensitive information. By leveraging the SQLite Table Length Command, the attacker can determine the length of the table name and then use a binary search to enumerate the characters of the table name one at a time.

## Requirements

1. Access to a vulnerable SQLite database

## Defense

1. Use parameterized queries to prevent SQL injection attacks

1. Implement proper input validation to prevent malicious input

1. Restrict access to SQLite databases to authorized personnel only

## Objectives

1. Identify the names of tables in an SQLite database

# Instructions

1. This command is used to retrieve the length of the name of the first non-system table in a SQLite database. Replace 'table_name_length_number' with the expected length of the table name.

**Code**: [[and (SELECT length(tbl_name) FROM sqlite_master WH]]

> The 'SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0' part of the command selects the length of the table name from the sqlite_master table where the type is 'table' and the table name does not start with 'sqlite_'. The 'table_name_length_number' part of the command is a placeholder for the expected length of the table name, which should be replaced with an integer value.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Boolean - Enumerating table name]]
- [[SQLite Injection]]
