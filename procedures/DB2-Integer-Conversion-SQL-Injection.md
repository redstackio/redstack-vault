---
id: a05a105b-1fb6-4de4-a86e-f1af0cf9c9fa
name: DB2-Integer-Conversion-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.996648+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Casting]]'
  - '[[tags/DB2-Cheatsheet]]'
  - '[[tags/DB2-Injection]]'
  - sqli
  - database-exploitation
commands:
  - '[[commands/db2-cast-string-to-integer]]'
  - '[[commands/db2-cast-integer-to-char]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# DB2-Integer-Conversion-SQL-Injection

## Summary

DB2 Integer Conversion Injection is a SQL injection technique that exploits improper handling of type conversions in DB2 databases. By injecting inputs that manipulate the CAST function to convert strings to integers or vice versa, attackers can bypass validation checks designed for numeric inputs, leading to arbitrary SQL command execution. This allows unauthorized access to sensitive data, privilege escalation within the database, or full system compromise in vulnerable applications.

## Description

This procedure targets applications connected to IBM DB2 databases where user input is cast to integer types without proper sanitization. For example, a query like SELECT * FROM users WHERE id = CAST($_INPUT as INTEGER) can be exploited by providing a string input that, when cast, alters the query structure. The technique relies on DB2's lenient type conversion behavior, where invalid casts may result in errors that leak information or allow union-based injections. It is commonly used in web applications with direct SQL concatenation. Prerequisites include identifying an injectable parameter, typically via error-based or blind SQLi testing. Success enables data exfiltration or command execution, mapping to exploitation of remote database services.

## Requirements

1. Valid credentials or unauthenticated access to a DB2 database instance (e.g., via a vulnerable web application).
2. Knowledge of the target query structure, such as parameter positions expecting integer inputs.
3. A SQL client tool like db2 command-line or a web proxy (e.g., Burp Suite) to inject and observe responses.
4. Basic understanding of DB2 syntax and error messages for validation.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to reject non-numeric inputs before casting.
- Use parameterized queries or prepared statements to separate code from data, preventing injection.
- Apply least privilege principles to database users and regularly audit/ patch DB2 for known conversion vulnerabilities.
- Enable database logging for SQL errors and monitor for anomalous CAST usage or type mismatch errors.

## Objectives

1. Bypass input validation on integer-expecting parameters to inject malicious SQL payloads.
2. Execute arbitrary queries to extract sensitive data like user credentials or table contents.
3. Escalate access to modify database structures or execute system commands if extended privileges are obtained.

## Instructions

### Step 1: Identify Injectable Integer Parameter

**Context**: Probe the application to find endpoints where user input is cast to integer in SQL queries, such as user ID lookups. Use error-based testing to confirm DB2 as the backend and identify conversion points.

**Command** (Use a generic SQL probe like [[commands/sqlmap-test-injection]] or manual input):

Provide input like '1' UNION SELECT to trigger errors revealing CAST usage.

> Observe DB2-specific errors like SQLCODE -301 for type mismatches, confirming the vulnerability.

### Step 2: Demonstrate String to Integer Conversion for Injection Setup

**Context**: Test basic type casting to understand DB2's behavior. This step verifies the conversion mechanism and sets up for payload injection by showing how strings can be forced into integer contexts.

**Command** ([[commands/db2-cast-string-to-integer]]):

```sql
select cast('123' as integer) from sysibm.sysdummy1;
```

> This executes without error, returning 123, demonstrating successful string-to-integer conversion. In an injection scenario, replace '123' with a payload like '1; SELECT * FROM sensitive_table--' to append queries.

### Step 3: Demonstrate Integer to String Conversion for Payload Obfuscation

**Context**: Use reverse casting to obfuscate payloads or extract data in union-based attacks, where numeric results are concatenated as strings.

**Command** ([[commands/db2-cast-integer-to-char]]):

```sql
select cast(1 as char) from sysibm.sysdummy1;
```

> This returns '1' as a character, allowing injection of numeric data into string fields. Success is indicated by no conversion errors and the ability to chain with union selects for data exfiltration.

### Step 4: Craft and Execute Injection Payload

**Context**: Combine conversions in a full payload. For a vulnerable query like SELECT * FROM users WHERE id = $_INPUT, inject: 1 UNION SELECT cast((SELECT username FROM admins) as integer)--. Monitor for data leakage in responses.

Inject the payload via the application interface or SQL client.

> Expected success: Application returns additional rows or errors revealing injected data, confirming arbitrary query execution.
