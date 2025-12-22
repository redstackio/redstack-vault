---
type: procedure
description: >-
  A procedure to detect SQL injection vulnerabilities using a polyglot
  sleep/delay payload that works across multiple database contexts, particularly
  MySQL.
verified: true
submitted: false
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Polyglot injection (multicontext)]]'
  - '[[tags/SQL Injection]]'
commands:
  - '[[commands/curl-inject-sql-payload]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Detect-SQL-Injection-with-Polyglot-Sleep-Payload

## Summary

This procedure exploits potential SQL injection vulnerabilities in web applications by injecting a polyglot sleep command payload. The payload causes a deliberate delay in the database response if the injection succeeds, allowing attackers to confirm the vulnerability through time-based blind SQL injection techniques. It is designed to work across multiple SQL contexts and database versions, particularly MySQL, without requiring visible error messages or data output.

## Description

SQL injection remains one of the most common web application vulnerabilities, enabling attackers to manipulate backend database queries. This procedure focuses on time-based blind SQL injection, where no data is directly returned, but the presence of a vulnerability is inferred from response delays. The polyglot payload incorporates universal comment wrappers and conditional logic to evade basic filters and ensure compatibility with MySQL versions. It uses functions like SLEEP() for delays or BENCHMARK() for older versions, combined with XOR and comment obfuscation to bypass Web Application Firewalls (WAFs). This technique is typically applied during reconnaissance or initial access phases against public-facing web apps with unsanitized user inputs, such as login forms or search fields. Success confirms the vulnerability, paving the way for data extraction or command execution. Prerequisites include identifying injectable parameters via manual testing or automated scanners.

## Requirements

1. Access to a web application with a suspected SQL injection point (e.g., via browser or proxy).
2. Knowledge of the target URL and injectable parameters (e.g., query strings like ?id=1).
3. Tools for crafting and sending HTTP requests, such as curl or a proxy like Burp Suite.
4. A timer or stopwatch to measure response times accurately (delays of 5+ seconds indicate success).
5. Optional: sqlmap for automated testing, but manual injection is covered here.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, sanitization, and escaping for all user inputs using prepared statements or ORM frameworks like PDO in PHP.
- Use parameterized queries and stored procedures to separate code from data.
- Deploy Web Application Firewalls (WAFs) tuned to detect time-based anomalies and common SQLi patterns.
- Monitor application logs for unusual delays in database queries or high-latency responses from web servers.
- Enable database error logging and review for injection attempts; use least-privilege database accounts.

## Objectives

1. Confirm the presence of SQL injection vulnerabilities through response delays.
2. Infer database type and version without direct data leakage.
3. Bypass basic input filters using polyglot payloads for broader compatibility.
4. Lay groundwork for further exploitation, such as data exfiltration or RCE.

## Instructions

### Step 1: Identify Injectable Parameter

**Context**: Locate a user input field or URL parameter that interacts with the database, such as a search box, login form, or GET parameter (e.g., /page?id=1). Test for basic injection by appending a single quote (') and observing for errors or unusual behavior. This step ensures you're targeting a vulnerable endpoint before injecting the sleep payload.

**Why**: Without a confirmed injection point, the payload may fail silently. Basic tests help differentiate reflected inputs from database-interacting ones.

If errors occur (e.g., SQL syntax error), proceed; otherwise, try other parameters.

**Expected Output**: Database error message or application crash indicating unescaped input, or no change (proceed to next steps for blind testing).

### Step 2: Craft and Inject Polyglot Sleep Payload

**Context**: Use the polyglot SQL sleep payload to introduce a delay if injected successfully. This payload works in multiple contexts (e.g., string, numeric) and handles MySQL version differences. Inject it into the identified parameter using a tool like curl to send the HTTP request.

**Command** ([[commands/curl-inject-sql-payload]]):
```bash
curl "http://target.com/page?id=1$_PAYLOAD" -v
```

**Code Reference** ([[codes/Polyglot-MySQL-Sleep-Delay-Payload]]): Embed the payload as $_PAYLOAD, e.g., id=1' SLEEP(5) -- or the full polyglot version for evasion.

> This command sends the request with the payload appended. Replace http://target.com/page?id=1 with your target URL. The -v flag provides verbose output for timing. Measure the total response time; a delay of ~5 seconds (adjust SLEEP value) confirms injection success. If no delay, try variations or different parameters. The polyglot nature ensures it closes quotes and comments properly across contexts.

**Expected Output**: HTTP response with a noticeable delay (e.g., 5+ seconds) if vulnerable; normal response time otherwise. Verbose curl output shows timing details.

**Success Indicators**:
- Response time exceeds baseline by the specified sleep duration.
- No immediate errors, but consistent delays across multiple requests.

### Step 3: Verify and Enumerate Database Details

**Context**: If delay observed, refine the injection to extract information like database version. Use conditional logic in the payload to test specifics, such as version checks, and measure delays to infer yes/no answers (e.g., delay = true condition met).

**Why**: Confirmation alone isn't enough; enumeration reveals database type, version, and structure for targeted follow-up attacks.

Modify the payload to include version checks, e.g., append && (IF(@@version LIKE '5.%', SLEEP(5), 0)) to the injection point, and re-inject using the curl command from Step 2.

**Expected Output**: Selective delays based on conditions (e.g., delay on version 5.x confirms MySQL 5).

**Success Indicators**:
- Conditional delays match expected database traits.
- Ability to chain payloads for boolean-based data extraction.
