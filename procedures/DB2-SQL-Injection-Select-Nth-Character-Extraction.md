---
id: 4233e7f2-57a8-4dc6-ae17-634fbe110544
name: DB2-SQL-Injection-Select-Nth-Character-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.888911Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Data from Information Repositories|T1213.001 - Local Data
    Staging]]
sub_techniques: []
tags:
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
  - '[[tags/Select Nth Char]]'
  - sql-injection
  - data-extraction
commands:
  - '[[commands/db2-select-substring-nth-character]]'
platforms:
  - Database
  - DB2
  - Web
tools: []
validated: true
---

# DB2-SQL-Injection-Select-Nth-Character-Extraction

## Summary

This procedure demonstrates how to perform SQL injection in IBM DB2 databases to extract individual characters from sensitive strings, such as passwords or credit card numbers, using the SUBSTR function. By iteratively extracting the nth character, attackers can reconstruct full data fields character by character, bypassing direct query limitations in blind SQL injection scenarios.

## Description

DB2 SQL Injection targets web applications connected to IBM DB2 databases, exploiting unsanitized inputs to inject malicious SQL queries. The Select Nth Char Extraction technique uses the SUBSTR function to pull specific characters from database strings, enabling gradual data exfiltration in scenarios where full string retrieval is blocked or detectable. This is particularly effective in blind injections where boolean conditions or time delays confirm character matches. The attack assumes a vulnerable input parameter (e.g., login form or search field) and requires knowledge of the target table/column structure, often obtained via prior enumeration. Success allows extraction of sensitive data like user credentials or financial information, potentially leading to privilege escalation or further system compromise. This procedure focuses on the extraction mechanics within an established injection point.

## Requirements

1. Access to a vulnerable web application parameter interacting with a DB2 backend database.
2. Knowledge of the target table and column names containing the sensitive string (e.g., via error-based injection or union queries).
3. A SQL injection tool or proxy like Burp Suite to craft and send payloads.
4. Basic understanding of DB2 syntax and blind injection techniques (boolean or time-based).

## Defense

- Implement strict input validation, sanitization, and escaping for all user inputs using prepared statements or parameterized queries.
- Use web application firewalls (WAFs) to detect and block SQL injection patterns, including SUBSTR usage in payloads.
- Enable database logging and monitoring for anomalous queries, such as repeated SUBSTR calls on sensitive columns.
- Apply least privilege to database accounts, limiting query access to necessary data.

## Objectives

1. Inject a payload to extract the nth character from a target string in the DB2 database.
2. Reconstruct sensitive information by iterating through all character positions.
3. Confirm extraction success via boolean responses or application behavior in blind scenarios.

## Instructions

### Step 1: Identify the Vulnerable Injection Point and Target Data

**Context**: Locate a parameter susceptible to SQL injection and determine the table/column holding the target string (e.g., users.password). Use error-based or union-based injection to confirm DB2 backend and schema details.

**Command** (use a generic SQLi tester like sqlmap or manual via proxy):

No specific command here; manually craft initial probes like `' OR 1=1 --` to confirm injection.

> Probe the application to verify injection and enumerate database type/version. Expected: Error messages revealing DB2 or successful bypass of authentication.

### Step 2: Craft the Nth Character Extraction Payload Using SUBSTR

**Context**: Construct a blind injection payload that uses SUBSTR to extract a single character at position N from the target string. Wrap in a conditional (e.g., ASCII(SUBSTR(...)) > X) for boolean-based extraction, iterating N from 1 to string length and testing ASCII values 32-126.

**Command** ([[commands/db2-select-substring-nth-character]]):

```sql
SELECT CASE WHEN (ASCII(SUBSTR((SELECT password FROM users LIMIT 1), $_N, 1)) > $_ASCII_VALUE) THEN (SELECT COUNT(*) FROM sysibm.sysdummy1) ELSE (SELECT COUNT(*) - 1 FROM sysibm.sysdummy1) END FROM sysibm.sysdummy1
```

> This query extracts the nth character from the password field and compares its ASCII value. Inject into the vulnerable parameter, e.g., `username=admin' AND [payload] --`. Adjust $_N (position) and $_ASCII_VALUE (e.g., 64 for testing >'A'). For time-based, use SLEEP functions if available. Expected: Application response differs based on true/false (e.g., page loads vs. error).

### Step 3: Iterate and Reconstruct the Full String

**Context**: Repeat Step 2 for each position N (1 to max length, e.g., 32 for passwords) and binary search ASCII values to build the string. Automate with scripts if manual iteration is inefficient.

No new command; reuse [[commands/db2-select-substring-nth-character]] with varying parameters.

> Log true/false responses to deduce each character. For example, if true for ASCII > 97 and false > 98, the char is 'a'. Expected: Full reconstructed string, e.g., 'password123'.

### Step 4: Verify and Use Extracted Data

**Context**: Validate the reconstructed data and apply it (e.g., test credentials). Monitor for detection to avoid alerting defenders.

No command; manual verification.

> Attempt login with extracted password. Expected: Successful authentication or data validation against known samples.
