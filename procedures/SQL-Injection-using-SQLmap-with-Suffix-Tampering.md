---
id: 695b4ec8-aafa-42ce-b078-aa5df6f8bc27
name: SQL-Injection-using-SQLmap-with-Suffix-Tampering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.480484+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/SQL Injection]]'
  - '[[tags/SQLmap]]'
  - '[[tags/Suffix Tampering]]'
commands:
  - '[[commands/sqlmap-test-injection-with-suffix-tampering]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# SQL-Injection-using-SQLmap-with-Suffix-Tampering

## Summary

This procedure demonstrates how to use SQLmap to detect and exploit SQL injection vulnerabilities in a web application's URL parameters by applying suffix tampering. Suffix tampering involves appending a custom string (such as '-- ') to the injection payload to close SQL statements prematurely and bypass basic filters or WAF rules, allowing automated detection and exploitation of vulnerabilities leading to unauthorized database access.

## Description

SQL injection (SQLi) attacks target web applications that fail to properly sanitize user inputs, enabling attackers to inject malicious SQL code into backend database queries. SQLmap automates the detection and exploitation process using techniques like error-based, boolean-based, and time-based blind SQLi. Suffix tampering enhances this by modifying the payload's end (e.g., adding comments like '-- ' for MySQL) to evade detection mechanisms that block standard payloads. This procedure is applicable in penetration testing scenarios against public-facing web apps with dynamic parameters (e.g., ?id=1). Successful execution can reveal database structure, extract sensitive data like user credentials, or execute arbitrary commands if the database server allows. Prerequisites include a vulnerable target and network access; it maps to exploiting public-facing applications for initial access.

## Requirements

1. Network access to the target web application (e.g., HTTP/HTTPS endpoint with query parameters).
2. SQLmap tool installed on the attacker's system (Kali Linux recommended).
3. Basic knowledge of the target's URL structure and potentially vulnerable parameters (e.g., via manual testing or reconnaissance).
4. Optional: A wordlist for credential dumping if exploitation escalates to data extraction.

## Defense

Defensive measures and detection strategies:

- Use prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) with SQLi rules (e.g., ModSecurity) tuned to detect tampered payloads.
- Enable database logging and monitor for anomalous queries (e.g., unusual comment suffixes or error messages).
- Regularly perform vulnerability scans with tools like SQLmap from an authorized perspective and apply input validation/sanitization.

## Objectives

1. Detect SQL injection vulnerabilities in specified URL parameters.
2. Bypass basic filters using suffix tampering to confirm exploitability.
3. Extract database information or sensitive data upon successful injection.
4. Escalate to arbitrary SQL command execution if the vulnerability allows.

## Instructions

### Step 1: Identify the Target URL and Parameter

**Context**: Begin by confirming the target endpoint and the parameter likely vulnerable to injection (e.g., 'id' in a search or product page). This step ensures the test is focused and reduces false positives; manual inspection or tools like Burp Suite can help pinpoint injectable points.

No command required for this preparatory step. Manually review the URL (e.g., http://example.com/?id=1) and note the parameter.

**Expected Output**: Documented target URL and parameter (e.g., http://example.com/?id=1, parameter: id).

### Step 2: Run Basic SQLmap Detection

**Context**: Test for SQLi without tampering first to establish a baseline. This verifies if the parameter is injectable using SQLmap's default techniques, providing initial vulnerability confirmation before applying advanced evasion.

**Command** ([[commands/sqlmap-test-injection-with-suffix-tampering]]):

Use the command without the suffix initially by omitting --suffix:

```bash
python sqlmap.py -u "http://example.com/?id=1" -p id
```

> This command scans the specified URL and parameter for SQLi vulnerabilities using automated payloads. SQLmap will attempt error-based, union-based, and blind techniques. If vulnerable, it reports the injection type and database backend.

**Expected Output**: Console output indicating vulnerability, e.g., "[INFO] the back-end DBMS is MySQL" and "Parameter: id (GET) is vulnerable."

### Step 3: Apply Suffix Tampering for Evasion

**Context**: If basic detection fails due to filters, apply suffix tampering to modify the payload end (e.g., '-- ' comments out trailing SQL). This step evades simple WAFs or input filters that block standard quotes or unions, confirming tamperable vulnerabilities.

**Command** ([[commands/sqlmap-test-injection-with-suffix-tampering]]):

```bash
python sqlmap.py -u "http://example.com/?id=1" -p id --suffix="-- "
```

> This appends '-- ' to payloads, closing statements for databases like MySQL. It helps bypass filters expecting complete SQL without comments. Monitor for successful injection indicators like database errors or delayed responses.

**Expected Output**: Similar to Step 2 but with successful detection if tampering evades filters, e.g., "Payload: 1' [suffix: -- ] --> " followed by vulnerability confirmation.

### Step 4: Enumerate and Exploit if Vulnerable

**Context**: Upon detection, enumerate database details and extract data. This escalates from detection to exploitation, dumping tables or users to achieve objectives like data theft.

**Command** ([[commands/sqlmap-test-injection-with-suffix-tampering]]):

Extend with enumeration flags:

```bash
python sqlmap.py -u "http://example.com/?id=1" -p id --suffix="-- " --dbs --tables
```

> The --dbs flag lists databases, --tables enumerates table names. Use --dump for full data extraction if needed. This step verifies success by revealing schema and content.

**Expected Output**: List of databases (e.g., "Available databases [2]: [*] information_schema [*] webapp_db") and tables (e.g., "Database: webapp_db [3 tables] + users + products + orders").
