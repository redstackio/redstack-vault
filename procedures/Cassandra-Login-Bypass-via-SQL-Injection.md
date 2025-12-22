---
id: 34efeff9-5f0c-4f09-a541-796c1c9d6faa
name: Cassandra-Login-Bypass-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.505979+00:00'
updated_at: '2023-04-06T03:56:32.524988+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - cassandra-injection
  - cassandra-login-bypass
  - login-bypass
commands: []
platforms:
  - Web
  - Database
tools: []
validated: true
---

# Cassandra-Login-Bypass-via-SQL-Injection

## Summary

This procedure demonstrates how to bypass the authentication mechanism of a Cassandra database login interface using SQL injection techniques. By injecting specially crafted payloads into the username and password fields of a vulnerable web-based login form, an attacker can manipulate the underlying CQL (Cassandra Query Language) query to authenticate as an administrative user without valid credentials, granting unauthorized access to the database.

## Description

Cassandra is a distributed NoSQL database commonly used for handling large-scale data. While NoSQL, its web interfaces or custom applications may use SQL-like queries vulnerable to injection attacks. This procedure targets a login page where user input is not properly sanitized, allowing attackers to comment out portions of the authentication query and append conditions that always evaluate to true. This bypasses the password check, enabling login as 'admin' or similar privileged accounts.

The attack assumes a web application frontend interacting with Cassandra via CQL. Success leads to full database access, potentially allowing data exfiltration, modification, or further exploitation. This is particularly dangerous in environments where Cassandra stores sensitive information like user credentials or application data. The technique relies on classic SQLi principles adapted for CQL, such as using comments (/* */) to truncate queries and logical operators to force true conditions.

## Requirements

1. Network access to the target web application hosting the Cassandra login interface (typically over HTTP/HTTPS on port 80/443).
2. A browser or proxy tool like Burp Suite to intercept and modify login requests.
3. Basic knowledge of SQL/CQL injection payloads and web form manipulation.
4. The login form must be vulnerable to injection, with unsanitized inputs directly influencing the backend query.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in the application code to separate user input from CQL execution.
- Validate and sanitize all user inputs, rejecting or escaping special characters like quotes and comments.
- Deploy Web Application Firewalls (WAFs) tuned to detect injection patterns, such as unusual comment usage in login fields.
- Enable Cassandra authentication with strong passwords and role-based access control (RBAC).
- Monitor database logs for anomalous queries, including those with injected comments or always-true conditions.
- Regularly audit and patch the web application and Cassandra installation to address known vulnerabilities.

## Objectives

1. Identify and confirm a vulnerable login endpoint in the Cassandra web interface.
2. Inject payloads to bypass authentication and gain access as a privileged user.
3. Verify access by querying or extracting data from the database.

## Instructions

### Step 1: Identify the Vulnerable Login Form

**Context**: Locate the login page of the web application connected to Cassandra. Inspect the form to confirm username and password fields are present and submitted via POST.

Use browser developer tools or a proxy to examine the request. Look for direct concatenation of user input into CQL statements in the backend (if source code is available) or test for vulnerability by submitting simple payloads like a single quote (') to observe errors.

**Expected Output**: Error messages indicating injection potential, such as CQL syntax errors, or no errors but unusual behavior.

### Step 2: Craft and Submit the Bypass Payload

**Context**: Use a comment-based injection to truncate the password check and append a tautology (always-true condition) to authenticate as 'admin'.

Enter the following payloads into the login fields:

**Code** ([[codes/Cassandra-Login-Bypass-Input-Payload]]):

```sql
username: admin'/*
password: */and pass>'
```

Submit the form. The payload comments out the password verification in the query (e.g., SELECT * FROM users WHERE user = 'admin'/*' AND pass = 'password' becomes SELECT * FROM users WHERE user = 'admin'/* AND then appends and pass>' which is always true due to the comparison.

If using a proxy like Burp Suite, intercept the POST request and modify the parameters accordingly.

**Expected Output**: Successful login redirection to the dashboard or admin panel, without requiring a valid password.

### Step 3: Verify Access and Extract Data

**Context**: Once logged in, confirm privileged access by executing a sample query to retrieve user data.

Use the application's query interface or inject further to run a full query:

**Code** ([[codes/Cassandra-Auth-Bypass-Query-Payload]]):

```sql
SELECT * FROM users WHERE user = 'admin'/*' AND pass = '*/and pass>'' ALLOW FILTERING;
```

This payload logs in as admin by commenting out the password clause and forcing a true condition with 'and pass>'' (an invalid but non-breaking comparison). The ALLOW FILTERING clause permits the query despite potential inconsistencies in Cassandra.

**Expected Output**: Response containing admin user details or full user table data, confirming bypass success.

### Step 4: Escalate or Exfiltrate

**Context**: With access, enumerate the database schema or export sensitive data.

Decision point: If the interface allows, query keyspaces and tables (e.g., DESCRIBE KEYSPACES;). If further injection is possible, chain to data exfiltration.

If no direct query access, use the authenticated session to perform authorized actions that reveal data.
