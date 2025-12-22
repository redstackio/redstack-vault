---
id: a7dc5a6a-8998-44c2-97fd-5c66ff696787
name: Identifying Time-Based SQL Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T14:54:46.274454+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/SQL]]'
  - '[[tags/sqli]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-mysql-time-based-sqli-test]]'
  - '[[commands/curl-mssql-time-based-sqli-test]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Identifying Time-Based SQL Injection

## Summary

This procedure demonstrates how to identify time-based SQL injection vulnerabilities in web applications by injecting conditional payloads that introduce measurable delays in database responses. Time-based SQLi is useful when error-based or union-based techniques fail, as it relies on timing differences to infer data without visible errors or output changes.

## Description

Time-based SQL injection exploits vulnerabilities in web applications where user input is not properly sanitized before being incorporated into SQL queries. By injecting payloads that include time-delay functions (e.g., SLEEP in MySQL or WAITFOR DELAY in MSSQL), an attacker can determine if the input is executed by observing response delays. This technique is particularly effective against blind SQLi scenarios where the application does not reveal database errors or return injected data. The procedure targets input fields like search boxes, login forms, or URL parameters. Success confirms the vulnerability, allowing further exploitation for data extraction via conditional logic (e.g., IF statements combined with delays). This maps to exploiting public-facing applications and is common in OWASP Top 10 injection risks.

## Requirements

1. Access to a web application with user-controllable input fields or parameters (e.g., search functionality).
2. Knowledge of the target database type (MySQL, MSSQL, etc.) or ability to test multiple payloads.
3. Tools like a web browser, [[tools/Burp-Suite]] for proxying requests, or curl for command-line testing.
4. Network access to the target application without restrictions on HTTP requests.
5. Basic understanding of SQL syntax and web request manipulation.

## Defense

Defensive measures and detection strategies:

- Use prepared statements and parameterized queries to prevent input from altering SQL structure.
- Implement web application firewalls (WAFs) to detect and block suspicious payloads containing time functions like SLEEP or WAITFOR.
- Enable database logging to monitor query execution times and flag anomalies (e.g., queries taking longer than expected).
- Rate-limit requests to prevent timing attacks and use input validation to sanitize special characters.
- Monitor application logs for delayed responses correlated with user inputs.

## Objectives

1. Confirm the presence of a time-based SQL injection vulnerability in a target input field.
2. Differentiate between database types based on successful payload responses.
3. Establish a baseline for further blind SQLi exploitation, such as data enumeration.
4. Expected outcome: Observable delay in application response (e.g., 5-10 seconds) without errors.

## Instructions

### Step 1: Identify Testable Input Parameters

**Context**: Locate user input fields or URL parameters that interact with the database, such as search boxes or form fields. Prioritize those that return dynamic content, as static pages won't show delays.

Use a web browser or [[tools/Burp-Suite]] to inspect requests. No specific command needed here; manually navigate to the application and note the parameter name (e.g., 'q' in /search?q=value).

> If the parameter is in a POST request, capture it with Burp; for GET, append directly to the URL.

### Step 2: Test for MySQL Time-Based SQLi

**Context**: Inject a MySQL-specific payload to check if the input is vulnerable. The SLEEP function causes a delay if the query executes the injected code, confirming SQLi without needing output changes.

**Command** ([[commands/curl-mysql-time-based-sqli-test]]):
```bash
curl -G "http://target.com/search" -d "q=' or sleep(5) #" --max-time 10
```

> This sends a GET request with the payload in the 'q' parameter. The # comments out the rest of the query. Time the response: a 5-second delay indicates vulnerability. If no delay, try URL encoding the payload (%27%20or%20sleep(5)%20%23) or test in Burp Repeater for precision. Why: The conditional ' or ensures execution if the input is concatenated into the SQL.

### Step 3: Test for MSSQL Time-Based SQLi

**Context**: If MySQL payload fails, test MSSQL using WAITFOR DELAY. This introduces a time-based blind injection if the database executes it.

**Command** ([[commands/curl-mssql-time-based-sqli-test]]):
```bash
curl -G "http://target.com/search" -d "q=' waitfor delay '00:00:10'--" --max-time 15
```

> This payload uses -- to comment out trailing query parts. Expect a 10-second delay on success. Adjust delay time based on network latency. Use Burp to intercept and modify if curl shows false negatives due to timeouts. Why: Different databases have unique delay functions; testing variants confirms the backend.

### Step 4: Verify and Baseline Response Times

**Context**: Run a benign request first to measure normal response time, then compare with injected payloads. This rules out network issues.

Execute a standard search:
```bash
curl -G "http://target.com/search" -d "q=test" --max-time 5
```

> Normal response should be <2 seconds. Repeat injections and average timings. If consistent delays only with payloads, vulnerability confirmed. Decision point: If delay varies, test with conditional logic like AND (SELECT COUNT(*) FROM users)>0 AND SLEEP(5) to refine.

### Step 5: Document and Escalate if Vulnerable

**Context**: If delays confirm SQLi, note the working payload and parameter for further procedures like data extraction.

No command; log findings (e.g., payload, delay observed, DB type inferred). Proceed to boolean-based extraction if needed.

> Success here enables advanced techniques; always test ethically.
