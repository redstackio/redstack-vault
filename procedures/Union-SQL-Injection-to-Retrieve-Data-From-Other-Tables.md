---
id: 2269e6cf-ec4c-443b-8ab6-c3e81c0d0d60
name: Union-SQL-Injection-to-Retrieve-Data-From-Other-Tables
type: procedure
verified: true
submitted: true
created_at: '2020-08-28T06:13:51.602441+00:00'
updated_at: '2023-05-26T01:33:56.323376+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - sql
  - sqli
  - sql-injection
  - web-applications
commands:
  - '[[commands/curl-send-union-sqli-column-test]]'
  - '[[commands/curl-send-union-sqli-data-retrieval]]'
platforms:
  - Web
tools: []
validated: true
---

# Union-SQL-Injection-to-Retrieve-Data-From-Other-Tables

## Summary

This procedure demonstrates how to perform a Union-based SQL injection attack to determine the number of columns in a vulnerable query and subsequently retrieve sensitive data, such as usernames and passwords, from other database tables like the 'users' table. It targets web applications where user input in URL parameters is not properly sanitized, allowing attackers to append UNION SELECT statements to extract data from the database.

## Description

Union SQL injection exploits vulnerabilities in web applications that concatenate user input directly into SQL queries without proper parameterization or escaping. By injecting a UNION SELECT statement, an attacker can append a custom query to the original one, provided the number of columns matches and data types are compatible. This technique is commonly used after identifying a injectable parameter (e.g., via error-based or boolean-based SQLi) to escalate from basic injection confirmation to data exfiltration. The target environment is typically a web application backed by a relational database like MySQL, interacting via GET parameters in URLs. Prerequisites include identifying a vulnerable endpoint, such as a search or category filter. Success allows dumping sensitive data like credentials, which can lead to further compromise such as account takeover or lateral movement.

## Requirements

1. Access to a vulnerable web application with a SQL injection point in a GET parameter (e.g., ?category= or ?id=).
2. Knowledge of the base URL and the injectable parameter name.
3. Tools like curl for sending HTTP requests (or a proxy like Burp Suite for manual testing).
4. Basic understanding of SQL syntax and URL encoding to craft payloads.
5. Network connectivity to the target application.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries in application code to prevent injection.
- Implement web application firewalls (WAFs) to detect and block anomalous SQL patterns in requests.
- Enable database logging to monitor for unexpected UNION queries or data access from non-standard tables.
- Input validation and sanitization: Whitelist allowed characters and escape special SQL keywords.
- Regular vulnerability scanning with tools like sqlmap or OWASP ZAP to identify injectable points.

## Objectives

1. Confirm the number of columns in the original query to craft a valid UNION payload.
2. Inject a UNION SELECT to retrieve data from a target table (e.g., users).
3. Extract and observe sensitive information like usernames and passwords.
4. Validate successful data exfiltration without causing application errors.

## Instructions

### Step 1: Identify and Test Number of Columns

**Context**: Begin by injecting a UNION SELECT with dummy string values to determine the number of columns in the vulnerable query. Start with a small number (e.g., 2) and increment until the payload executes without errors, indicating a match. This step confirms the structure needed for data retrieval.

**Command** ([[commands/curl-send-union-sqli-column-test]]):
```bash
curl "http://$_TARGET_URL?$_PARAMETER='"+UNION+SELECT+'abc','def'--" -v
```

> This command sends a GET request to the vulnerable endpoint with a URL-encoded UNION SELECT payload using string literals ('abc', 'def') to test for 2 columns. The -- comment terminator prevents further query execution. If the application responds normally (e.g., displays the dummy values or no error), the column count matches. Expected output includes the page rendering with injected strings visible, or no SQL errors. If errors occur (e.g., "unknown column"), try increasing columns (e.g., add more 'null' or strings). Why: Matching columns ensures the UNION appends correctly without syntax errors.

### Step 2: Craft and Execute Data Retrieval Payload

**Context**: Once the column count is confirmed (e.g., 2 columns), replace the dummy values with a SELECT from the target table (e.g., username, password from users). This step exfiltrates real data by unioning it into the application's response.

**Command** ([[commands/curl-send-union-sqli-data-retrieval]]):
```bash
curl "http://$_TARGET_URL?$_PARAMETER='"+UNION+SELECT+username,password+FROM+users--" -v
```

> This command injects a UNION SELECT to pull username and password columns from the 'users' table, assuming 2 columns. The payload is URL-encoded for safe transmission. Expected output shows the application's page populated with actual usernames and hashed/plaintext passwords from the database, blended into the legitimate results. If no data appears, verify table/column names via error messages or blind techniques. Why: This directly achieves the objective of data exfiltration, revealing sensitive information for further attacks like credential stuffing.
