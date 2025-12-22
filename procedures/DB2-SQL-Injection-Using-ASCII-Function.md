---
id: 9ff78cbd-a43d-4088-b585-6139d1bf8eaf
name: DB2-SQL-Injection-Using-ASCII-Function
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.969921+00:00'
updated_at: '2023-04-10T20:22:04.455338+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Char -> ASCII Value]]'
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
commands:
  - '[[commands/db2-select-ascii-character]]'
platforms:
  - Database
  - DB2
tools: []
validated: true
---

# DB2-SQL-Injection-Using-ASCII-Function

## Summary

This procedure demonstrates how to use the ASCII function in DB2 SQL queries as part of a SQL injection attack to convert characters to their ASCII values, potentially bypassing input validation filters that block direct character input. By injecting ASCII-based payloads, attackers can construct malicious queries to extract sensitive data from DB2 databases.

## Description

DB2 Injection exploits vulnerabilities in DB2 database applications through SQL Injection, allowing attackers to inject and execute unauthorized SQL code. The 'Char to ASCII Conversion' method involves using the ASCII() function to translate characters into numeric ASCII codes (e.g., 'A' becomes 65), which can evade filters designed to block specific strings or characters. This technique is particularly useful in scenarios where direct injection of special characters is sanitized, but numeric representations are allowed. In a typical attack, this enables querying database schema, extracting user data, or escalating to remote code execution on the database server. The target environment is a web application connected to a DB2 backend with insufficient input sanitization. Success allows unauthorized access to sensitive information like customer records or financial data, leading to data breaches or further lateral movement.

## Requirements

1. Valid user access to the target web application or direct DB2 connection (e.g., via a vulnerable login form or API endpoint).
2. Knowledge of the injection point, such as a search field, login parameter, or URL query string vulnerable to SQLi.
3. Tools for SQL injection testing, such as a database client (e.g., db2 command-line tool) or a proxy like Burp Suite to craft and send payloads.
4. Basic understanding of DB2 SQL syntax and ASCII encoding to construct effective payloads.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to reject or escape special characters and numeric sequences that could form SQL payloads.
- Use parameterized queries or prepared statements in application code to prevent direct SQL concatenation.
- Enable database activity monitoring (e.g., DB2 audit logging) to detect anomalous queries involving functions like ASCII() or unusual numeric conversions.
- Deploy web application firewalls (WAFs) tuned to identify SQLi patterns, including ASCII-based evasions.

## Objectives

1. Bypass input validation filters using ASCII conversions to inject and execute SQL code.
2. Extract sensitive information from the DB2 database, such as table schemas or user credentials.
3. Achieve unauthorized data access or enable further exploitation like privilege escalation on the database server.

## Instructions

### Step 1: Identify Injection Point and Test ASCII Conversion

**Context**: Locate a vulnerable input field in the target application (e.g., a search box) and inject a basic ASCII function query to verify if numeric conversions can be executed without triggering filters. This step confirms the vulnerability by retrieving a known ASCII value, such as for 'A' (65), using the sysibm.sysdummy1 table as a dummy source.

**Command** ([[commands/db2-select-ascii-character]]):

```sql
select ascii('A') from sysibm.sysdummy1
```

> This command executes the ASCII function on the character 'A', returning its integer value (65). In an injection context, replace 'A' with a variable or payload component (e.g., ascii(substr(password,1,1))) to extract data character-by-character. If successful, the output confirms the injection point allows function execution. If blocked, try encoding the entire query or chaining with union-based injection.
