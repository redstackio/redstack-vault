---
id: 651db1ab-db19-41ce-9fc4-6e35d030b957
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.742998+00:00'
updated_at: '2023-04-10T20:24:17.351454+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/No Equal]]'
  - '[[tags/SQL Injection]]'
  - '[[tags/WAF Bypass]]'
commands:
  - '[[commands/curl-send-sql-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# SQL-Injection-WAF-Bypass-Using-Version-Checks

## Summary

This procedure demonstrates how to bypass a Web Application Firewall (WAF) protecting against SQL injection attacks by using version-specific SQL operators like LIKE, NOT IN, IN, and BETWEEN to probe and extract database information without triggering standard equality-based filters.

## Description

SQL injection vulnerabilities allow attackers to inject malicious SQL code into a web application's database queries. WAFs often block common injection patterns, such as equality checks (e.g., '=1'), but may overlook version probing techniques that use conditional operators on database functions like version(). This procedure targets WAFs that enforce strict rules on certain SQL syntax while permitting others, enabling data extraction, modification, or control over the application. It is applicable in scenarios where the target uses a versioned database like MySQL or PostgreSQL, and the WAF fails to normalize or detect these operators. Success depends on identifying a vulnerable parameter (e.g., 'id' in a URL) and iteratively testing payloads to confirm bypass and extract data.

## Requirements

1. Access to a web application with a known SQL injection vulnerability in a parameter (e.g., GET/POST 'id' field).
2. Knowledge of basic SQL syntax and the target database type/version (e.g., MySQL 5.x).
3. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
4. Network access to the target application without additional authentication barriers.

## Defense

- Implement a WAF with comprehensive rule sets that normalize and block all SQL operators, including LIKE, IN, NOT IN, and BETWEEN, when used in conditional contexts.
- Use prepared statements and parameterized queries in the application code to prevent injection entirely.
- Regularly fuzz and test the application with tools like sqlmap to identify and patch bypass techniques.
- Enable database logging and monitor for anomalous queries involving version() or substring() functions.

## Objectives

1. Bypass WAF filters to inject SQL payloads without detection.
2. Probe the database version to confirm bypass viability.
3. Extract sensitive data, such as user information or configuration details.
4. Escalate to data modification or full application compromise if possible.

## Instructions

### Step 1: Identify the Vulnerable Parameter and Test Basic Injection

**Context**: Begin by confirming the SQL injection point and ensuring the WAF blocks standard payloads, setting the stage for bypass attempts. This step verifies the vulnerability exists and isolates the parameter (e.g., 'id' in a search endpoint).

Navigate to the target page (e.g., http://target.com/search?id=1) and append a basic injection like 'id=1' OR '1'='1 to observe if it returns unexpected data or errors. If blocked by WAF, proceed to bypass.

**Expected Output**: Normal page for valid input; error or block for obvious injections, confirming WAF presence.

### Step 2: Inject Version Bypass Payloads Using Conditional Operators

**Context**: Use the payloads from [[codes/SQL-Version-Bypass-Payloads]] to probe the database version without using blocked equality operators. These payloads leverage substring(version(),1,1) to check the first digit of the DB version, adapting to WAF rules that allow certain operators.

Execute [[commands/curl-send-sql-payload]] to send the payloads, substituting the target URL and payload. Test each variant (LIKE, NOT IN, IN, BETWEEN) iteratively to find which evades the WAF.

For example:

```bash
curl "http://target.com/search?id=1 and substring(version(),1,1)like(5)" -v
```

Observe the response for data leakage or version confirmation.

**Expected Output**: If successful, the page returns database-derived data or confirms version (e.g., true/false behavior based on version digit matching the condition), without WAF alerts.

### Step 3: Verify Bypass and Extract Data

**Context**: Once a payload succeeds, chain it with union-based extraction or blind injection to pull data. This step confirms control and begins exfiltration.

If the LIKE(5) payload works (indicating MySQL 5.x), extend to extract tables: append ' UNION SELECT table_name FROM information_schema.tables--' adjusted with the bypass operator.

Use the same [[commands/curl-send-sql-payload]] for testing, monitoring response differences.

**Expected Output**: List of database tables or error messages revealing schema, indicating successful bypass and injection.
