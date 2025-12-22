---
id: 4f15d675-07a6-4d67-85be-97a684b75bb0
name: Execute-Stored-SQL-Injection-via-Blog-Entry-Field
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T17:37:22.800268+00:00'
updated_at: '2023-05-26T01:07:56.772476+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp-top-10
  - sql
  - sql-stored
  - web-applications
commands:
  - '[[commands/curl-test-single-quote-sql-injection]]'
  - '[[commands/curl-extract-database-version]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: high
detection_risk: high
validated: true
---

# Execute-Stored-SQL-Injection-via-Blog-Entry-Field

## Summary

This procedure demonstrates how to test for stored SQL injection vulnerabilities in web applications by injecting malicious payloads into persistent input fields, such as blog entry or comment boxes. The payload is stored in the database and executed when the content is retrieved and displayed, potentially exposing sensitive information like database versions to all users viewing the page. It targets applications using vulnerable SQL queries without proper input sanitization, allowing attackers to manipulate database responses.

## Description

Stored SQL injection occurs when user-supplied input is not properly sanitized and is stored directly in the database, then retrieved and rendered in application responses without further validation. This differs from reflected SQLi as the payload persists and affects multiple users. In this scenario, we target a blog or comment feature where entries are saved and displayed publicly. By injecting SQL syntax like single quotes or UNION-based queries, we can trigger errors or extract data, such as the database version (e.g., MariaDB). This technique is common in legacy web apps using direct string concatenation in SQL statements. Successful exploitation can lead to data leakage, unauthorized data access, or full compromise if chained with other vulnerabilities. The procedure assumes access to a web form for submitting entries and focuses on manual testing to identify and confirm the vulnerability.

## Requirements

1. Network access to the target web application (e.g., HTTP/HTTPS connectivity).
2. A tool like [[tools/Burp-Suite]] or curl for submitting and intercepting requests.
3. Basic knowledge of SQL syntax and the target's form structure (e.g., POST endpoint for blog submissions).
4. No authentication required if the input field is public; otherwise, valid session cookies.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries to separate SQL code from user input.
- Use web application firewalls (WAFs) to detect and block common SQL injection patterns, such as single quotes or UNION keywords.
- Enable database error logging and monitoring for anomalous queries; suppress detailed error messages in production to avoid information disclosure.
- Sanitize and validate all user inputs, especially for stored fields, using libraries like OWASP ESAPI.
- Regularly scan for vulnerabilities using tools like sqlmap or application security testing (DAST) tools.

## Objectives

1. Identify if the blog entry field is vulnerable to stored SQL injection by triggering a database error.
2. Extract database metadata, such as the version, to assess the target's environment and potential for further exploitation.
3. Confirm persistence by verifying that the injected payload affects subsequent page loads for other users.
4. Demonstrate information disclosure without requiring repeated injections.

## Instructions

### Step 1: Test Input Field for SQL Parsing

**Context**: Begin by submitting a simple payload containing a single quote to check if the input is parsed as SQL. This will trigger a syntax error if the application concatenates input directly into queries, revealing the vulnerability and potentially the database type.

**Command** ([[commands/curl-test-single-quote-sql-injection]]):
```bash
curl -X POST -d "entry='" -d "title=Test Entry" http://$_TARGET_URL/blog/add -c cookies.txt
```

> This command simulates submitting a blog entry with a single quote in the content field via a POST request. Replace $_TARGET_URL with the application's submission endpoint (e.g., http://example.com). The -c flag saves cookies for session persistence. If the form uses CSRF tokens, intercept and include them using [[tools/Burp-Suite]].

Navigate to the blog listing page after submission to view the entry. Look for an error message at the bottom of the page indicating a SQL syntax error, such as "You have an error in your SQL syntax".

### Step 2: Analyze Error Message for Database Identification

**Context**: The error from Step 1 provides clues about the backend database. Common errors include MySQL/MariaDB-specific messages. This step confirms the DB type (e.g., MariaDB) and guides payload crafting.

**Command** (No specific command; use browser or [[commands/curl-test-single-quote-sql-injection]] to resubmit if needed):

> Reload the blog page or use curl to fetch the entry:
```bash
curl -b cookies.txt http://$_TARGET_URL/blog/list
```

Examine the response for error details. For MariaDB, errors often reference its syntax or version indirectly.

### Step 3: Craft and Submit Payload to Extract Database Version

**Context**: Using the identified DB type, construct a UNION-based query to extract the version() function output. This payload is stored and displayed when the entry is rendered, leaking info to all viewers.

**Command** ([[commands/curl-extract-database-version]]):
```bash
curl -X POST -d "entry=' UNION SELECT version()--" -d "title=Version Test" http://$_TARGET_URL/blog/add -c cookies.txt
```

> This injects a UNION SELECT to append the database version to the legitimate query results. The -- comments out the rest of the query. Submit via the form or curl, then view the blog page. The version (e.g., "10.3.22-MariaDB") should appear in the entry display for all users.

Verify by loading the page in an incognito session or another browser to confirm persistence and visibility.

### Step 4: Verify Persistence and Impact

**Context**: Ensure the injection persists across sessions and affects multiple users, distinguishing it from reflected SQLi. This confirms the stored nature and potential for broad exposure.

**Command** (Use [[commands/curl-extract-database-version]] to resubmit if cleared, or fetch with curl):
```bash
curl -b cookies.txt http://$_TARGET_URL/blog/list
```

> Check the output for the injected content. Success is indicated by the version info displaying without re-submission.

If the entry is moderated or cleaned, the vulnerability may be partially mitigated, but error disclosure still indicates risk.
