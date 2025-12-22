---
id: 85356103-4c38-4e2c-9f46-fc9054b577a1
name: DB2-SQL-Injection-Using-ASCII-Concatenation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.071338+00:00'
updated_at: '2023-04-10T20:22:01.532995+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/SQL Injection]]'
  - '[[tags/DB2]]'
  - '[[tags/Avoiding Quotes]]'
  - '[[tags/ASCII Bypass]]'
commands:
  - '[[commands/db2-concatenate-ascii-values]]'
platforms:
  - Database
  - DB2
tools: []
validated: true
---

# DB2-SQL-Injection-Using-ASCII-Concatenation

## Summary

This procedure demonstrates how to perform SQL injection in IBM DB2 databases by using ASCII concatenation to construct strings without quotes, bypassing filters that block direct quote usage in payloads. It is useful in scenarios where input validation strips or escapes quotes, allowing attackers to build malicious SQL statements character by character using the CHR() function and concatenation operator (||).

## Description

DB2 SQL injection via ASCII concatenation targets web applications connected to DB2 databases that fail to properly sanitize user inputs. Attackers identify injectable parameters (e.g., login forms, search fields) and craft payloads that convert ASCII values to characters using CHR(), then concatenate them to form strings like table names, values, or commands. For example, to inject a condition like 'OR 1=1', quotes around 'OR' can be avoided by using CHR(79)||CHR(82). This technique exploits the DB2-specific CHR() function and || operator. Success can lead to data extraction, authentication bypass, or command execution, depending on privileges. It applies to DB2 versions on Linux, Windows, or Unix systems with vulnerable front-end applications.

## Requirements

1. Access to a web application or interface with a vulnerable input field connected to a DB2 database (e.g., via HTTP POST/GET parameters).
2. Knowledge of the target application's SQL query structure (e.g., through error messages or blind injection testing).
3. A SQL client or proxy tool like [[tools/sqlmap]] or Burp Suite to craft and send payloads.
4. Basic understanding of ASCII values for desired characters (e.g., A=65, space=32).

## Defense

- Implement strict input validation and sanitization, rejecting or escaping special characters including those used in CHR().
- Use prepared statements or parameterized queries in application code to separate SQL logic from user input.
- Enable DB2 logging (e.g., audit facilities) to monitor for anomalous queries involving CHR() or excessive concatenations.
- Apply web application firewalls (WAFs) with rules detecting ASCII-based obfuscation patterns.
- Regularly audit and patch DB2 instances and front-end applications for known injection vulnerabilities.

## Objectives

1. Bypass quote-based input filters in DB2-connected applications to inject malicious SQL.
2. Construct string literals using ASCII values to extract sensitive data or escalate access.
3. Verify successful injection through data retrieval or error manipulation.

## Instructions

### Step 1: Identify Vulnerable Input and Test Basic Injection

**Context**: Begin by confirming the input field is vulnerable to SQL injection. Use a standard payload like ' OR 1=1 -- to check for boolean-based or error-based responses. If quotes are filtered, proceed to ASCII concatenation for string construction.

Observe application responses for delays, errors, or data leaks indicating injection success.

### Step 2: Craft ASCII Concatenation Payload Using CHR() Function

**Context**: Replace quote-enclosed strings in your SQL payload with concatenated CHR() calls. For instance, to form the string 'ADRI' (ASCII: A=65, D=68, R=82, I=73), use the command below. This builds the payload without triggering quote filters. Integrate this into the full injection, e.g., in a WHERE clause: username=admin' AND 1=CHR(49)||CHR(48) -- (for '10').

**Command** ([[commands/db2-concatenate-ascii-values]]):

**Code** ([[codes/DB2-ASCII-Concatenation-Example]]):

```sql
SELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sysibm.sysdummy1 -- returns “ADRI”. Works without select too
```

> This command uses the CHR() function to convert numeric ASCII values to characters and concatenates them with ||. The sysibm.sysdummy1 table provides a single dummy row for execution without needing a real table. Expected output is the string 'ADRI'. If integrated into an injection, success is indicated by altered query results, such as dumping user data or bypassing auth.

### Step 3: Integrate and Execute in Target Application

**Context**: Submit the crafted payload via the vulnerable input (e.g., using Burp Repeater or curl). Monitor for successful execution, such as returned data or privilege escalation. If blind, use time-based delays with functions like SLEEP(CHR(53)) for '5' seconds.

Adjust ASCII values based on the target string (e.g., for passwords or table names). Verify by extracting known data like version: SELECT version FROM sysibm.sysdummy1.
