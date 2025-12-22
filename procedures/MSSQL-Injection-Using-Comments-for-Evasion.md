---
id: 041b0839-cd3d-4b52-962e-44de4fc64206
name: MSSQL-Injection-Using-Comments-for-Evasion
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.499757+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - mssql-injection
  - sql-injection
  - evasion
  - comments
commands: []
platforms:
  - Windows
  - MSSQL
tools: []
validated: true
---

# MSSQL-Injection-Using-Comments-for-Evasion

## Summary

This procedure demonstrates how to perform SQL injection attacks on Microsoft SQL Server (MSSQL) databases by incorporating comments into the payload to evade web application firewalls (WAFs), input filters, or detection mechanisms. Comments allow attackers to truncate or ignore parts of the original query, enabling arbitrary SQL execution while bypassing simplistic security checks that look for complete malicious keywords.

## Description

MSSQL Injection using comments targets vulnerable input fields in web applications connected to MSSQL databases, such as login forms or search parameters. By appending SQL comments (single-line with '--' or multi-line with '/* */'), the injected payload can neutralize the rest of the application's query after the injection point, allowing execution of malicious code like union-based data extraction or command execution via xp_cmdshell. This technique is particularly effective against filters that block full keywords (e.g., 'UNION SELECT') but fail to account for commented fragments. The attack assumes a reflected or stored SQL injection vulnerability exists, typically identified via error-based or boolean blind techniques. Success can lead to data exfiltration, privilege escalation, or remote code execution, depending on database permissions.

## Requirements

1. Network access to the target web application with an MSSQL backend.
2. Identification of a vulnerable input parameter (e.g., via tools like [[tools/sqlmap]] or manual testing with payloads like ' OR 1=1--).
3. Basic knowledge of SQL syntax and MSSQL-specific functions (e.g., @@version for version detection).
4. A proxy tool like [[tools/Burp-Suite]] for intercepting and modifying requests (optional but recommended for precision).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, escaping special characters like '-', '/', and '*'.
- Use parameterized queries or prepared statements in application code to prevent direct query concatenation.
- Deploy a WAF configured to detect comment-based obfuscation patterns (e.g., rules for '--' or '/*' near SQL keywords).
- Enable MSSQL logging (e.g., via SQL Server Audit) and monitor for anomalous queries containing comments in user inputs.
- Regularly audit database permissions to limit xp_cmdshell or other extended stored procedures.

## Objectives

1. Bypass input filters or WAF rules blocking standard SQL injection payloads.
2. Execute arbitrary SQL commands to extract sensitive data (e.g., user credentials, database schema).
3. Achieve unauthorized access or escalation within the MSSQL database.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Confirm the vulnerability by testing for SQL errors or boolean responses. This step verifies that the input is unsanitized and directly influences the SQL query.

Inject a simple test payload to probe for MSSQL-specific errors:

```sql
' AND 1=CONVERT(int, (SELECT @@version))--
```

> This payload attempts a type conversion error if MSSQL is in use. If successful, you'll see a database error message revealing the backend (e.g., "Syntax error converting the varchar value...").

### Step 2: Craft Payload with Comments for Evasion

**Context**: Use comments to truncate the original query and append malicious SQL. Single-line comments (--) ignore everything after them on the line, while multi-line (/* */) can span lines to obfuscate longer payloads.

Construct a basic union-based payload with comments. For example, to extract database version:

```sql
' UNION SELECT @@version--
```

Or for multi-line obfuscation:

```sql
'/* malicious comment */ UNION SELECT user_name() AS username FROM sysusers--
```

> Replace the single quote (') with the appropriate delimiter based on the injection context. The comment ensures the application's trailing query (e.g., WHERE id=...) is ignored. Test incrementally: first confirm union works, then extract data column-by-column matching the original query's column count.

### Step 3: Execute and Extract Data

**Context**: Once the payload evades filters, use it to dump sensitive information or escalate. This step focuses on verification and expansion.

For blind injection (no visible output), use time-based delays with comments:

```sql
' AND IF(1=1, WAITFOR DELAY '00:00:05'--, 0)--
```

> If the page delays by 5 seconds, the injection succeeded. Scale to extract data via conditional delays (e.g., substring comparisons). For error-based, force errors with comments to reveal data: `' AND 1=CAST((SELECT @@version) AS int)--`.

### Step 4: Verify Success and Clean Up

**Context**: Confirm data access and minimize traces. Check for any logged anomalies.

Review extracted output for accuracy (e.g., valid usernames or hashes). If RCE is possible (e.g., via `'; EXEC xp_cmdshell 'whoami'--`), test sparingly to avoid alerts.

> Success is indicated by returned data matching expected database content, without triggering application errors or WAF blocks.
