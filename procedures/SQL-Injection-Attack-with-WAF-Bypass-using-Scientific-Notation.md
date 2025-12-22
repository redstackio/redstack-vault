---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - SQL Injection
  - WAF Bypass
  - MySQL
  - Scientific Notation
commands: []
platforms:
  - Web
  - MySQL
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SQL-Injection-Attack-with-WAF-Bypass-using-Scientific-Notation

## Summary

This procedure demonstrates a SQL injection attack targeting a vulnerable web application backed by a MySQL database. It uses scientific notation (e.g., 1.e for obfuscation) to bypass Web Application Firewall (WAF) filters, allowing authentication bypass and extraction of sensitive data such as user passwords from the database.

## Description

SQL injection exploits insufficient input validation in web applications to inject malicious SQL code into backend queries. In this technique, scientific notation is leveraged to encode parts of the payload, evading signature-based WAF detection that looks for common SQLi patterns like ' OR 1=1. The attack begins with a basic authentication bypass, progresses to WAF evasion, and culminates in blind SQL injection to extract password characters via ASCII comparison. This is effective against MySQL databases where numeric functions can be manipulated with exponent notation. The target is typically a login form or search field that concatenates user input directly into SQL queries without parameterization.

## Requirements

1. Access to a vulnerable web application with a MySQL backend (e.g., via browser or proxy like Burp Suite).
2. Knowledge of the target database structure, such as the existence of a 'users' table with a 'password' field.
3. A tool for intercepting and modifying HTTP requests (e.g., browser dev tools or proxy) to inject payloads.
4. Basic understanding of SQL syntax and blind injection techniques for data extraction.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries in application code to prevent direct SQL concatenation.
- Implement a robust WAF with behavioral analysis beyond simple signatures, such as anomaly detection for unusual query patterns.
- Enable database logging (e.g., MySQL general query log) and monitor for errors or unexpected queries involving functions like SUBSTRING or ASCII.
- Conduct regular input validation, sanitization, and web vulnerability scanning with tools like OWASP ZAP.

## Objectives

1. Bypass application authentication using basic SQL injection.
2. Evade WAF protections with obfuscated payloads employing scientific notation.
3. Extract sensitive data, such as user passwords, from the MySQL database via blind injection.
4. Achieve unauthorized access to database contents without triggering security alerts.

## Instructions

### Step 1: Basic Authentication Bypass

**Context**: Test for SQL injection vulnerability by injecting a payload that forces the query to always evaluate to true, bypassing login checks. This confirms the endpoint is vulnerable before attempting WAF evasion.

**Code** ([[codes/Basic-SQL-Injection-Auth-Bypass]]):

```sql
' or ''='
```

> Inject this payload into the username or password field of the login form (e.g., via POST request). The query will interpret it as a tautology, authenticating without valid credentials. Expected output: Successful login or access to the application dashboard, indicating vulnerability.

### Step 2: WAF Bypass with Scientific Notation

**Context**: If the basic payload is blocked by the WAF, obfuscate it using scientific notation (1.e as a no-op equivalent to 1* or similar) to alter the string without changing its logical effect, slipping past pattern matching.

**Code** ([[codes/SQL-Injection-WAF-Bypass-with-Scientific-Notation]]):

```sql
' or 1.e('')='
```

> Submit this modified payload in the same input field. The scientific notation (1.e('')) evaluates to 1=1 but evades filters looking for direct ' OR 1=1 patterns. Expected output: Bypassed authentication, granting access despite WAF presence.

### Step 3: Extract Password via Blind SQL Injection

**Context**: With access confirmed, use blind injection to extract data character-by-character from the 'users' table. This step employs nested scientific notation to obfuscate functions like SUBSTRING and ASCII, comparing against known values (e.g., ASCII 70 for 'F') to infer the password.

**Code** ([[codes/MySQL-Password-Extraction-using-Scientific-Notation-and-ASCII]]):

```sql
1.e(ascii 1.e(substring(1.e(select password from users limit 1 1.e,1 1.e) 1.e,1 1.e,1 1.e)1.e)1.e) = 70 or'1'='2
```

> Inject this into a searchable field or error-prone endpoint that reveals boolean responses (true/false based on page behavior). Iterate by changing the position (e.g., substring index) and comparison value (48-122 for printable ASCII). If the condition matches (e.g., first character is 'F'), the page loads normally; otherwise, it errors. Expected output: Boolean responses allowing reconstruction of the full password over multiple requests.
