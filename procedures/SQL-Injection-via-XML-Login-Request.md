---
id: 6620ebfc-361c-4441-8717-88ad0391a365
name: SQL-Injection-via-XML-Login-Request
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T18:35:21.094312+00:00'
updated_at: '2023-05-26T18:50:18.347221+00:00'
platforms:
  - Web
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/SQL]]'
  - '[[tags/sqli]]'
  - '[[tags/SQL Injection]]'
  - '[[tags/Web Applications]]'
  - '[[tags/xml]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-send-malicious-xml-login]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# SQL-Injection-via-XML-Login-Request

## Summary

This procedure demonstrates how to perform a SQL injection attack on a web application's XML-based login request to bypass authentication. By intercepting the XML payload and injecting a malicious SQL payload like ' or '1'='1 into the password field, an attacker can authenticate without valid credentials, exploiting improper input validation in the backend SQL query construction.

## Description

SQL injection in XML requests occurs when user-supplied data in XML format is not properly sanitized before being concatenated into SQL queries. In login scenarios, applications often send credentials in XML over HTTP POST requests. An attacker can intercept these requests using a proxy tool, modify the XML to inject SQL logic that always evaluates to true (e.g., ' or '1'='1), and bypass the authentication check. This technique targets web applications vulnerable to classic SQL injection in XML parsers or backend databases like MySQL or SQL Server. It requires network interception capabilities and is commonly used in penetration testing to assess authentication security.

## Requirements

1. Access to the target web application's login page over HTTP/HTTPS.
2. A proxy tool like [[tools/Burp-Suite]] configured to intercept traffic (requires browser proxy settings).
3. Basic knowledge of XML structure and SQL syntax.
4. Valid username for the target account (password not needed due to bypass).

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries to separate SQL code from user input.
- Validate and sanitize all XML inputs using XML parsers with security features (e.g., disable external entity processing).
- Implement web application firewalls (WAFs) to detect and block SQL injection patterns in requests.
- Enable database logging to monitor anomalous queries like those with unescaped quotes.
- Enforce HTTPS and certificate pinning to prevent easy interception.

## Objectives

1. Intercept and analyze the legitimate XML login request structure.
2. Inject a SQL payload to bypass password validation.
3. Achieve unauthorized access to the authenticated session.
4. Verify successful bypass without disrupting the application.

## Instructions

### Step 1: Intercept the Legitimate XML Login Request

**Context**: Configure a proxy to capture the XML payload sent during a normal login attempt. This reveals the structure of the username and password fields in the XML body, allowing identification of the injectable parameter.

**Tool**: Use [[tools/Burp-Suite]] to set up interception. Navigate to the login page, enter a valid username and invalid password, and submit to capture the request.

> In Burp Suite Proxy, ensure interception is on. The request will show an HTTP POST with Content-Type: application/xml, containing the XML body like <login><username>user</username><password>pass</password></login>.

### Step 2: Modify the XML Payload with SQL Injection

**Context**: Alter the password field in the intercepted XML to include a SQL injection payload that makes the authentication query always true, such as appending ' or '1'='1 to close the string and add a tautology.

**Instructions**: In the Burp Repeater tab, edit the XML body to inject the payload. For example, change <password>invalid</password> to <password>' or '1'='1</password>. Ensure the XML remains well-formed.

**Command** (Alternative simulation using [[commands/curl-send-malicious-xml-login]]):
```bash
curl -X POST http://target.com/login \
  -H "Content-Type: application/xml" \
  -d '<login><username>validuser</username><password>\' or \'1\'=\'1</password></login>'
```

> This curl command simulates the modified request. The escaped quotes (\') ensure the payload is properly sent. Expected output includes a 200 OK response with session cookies or redirect to dashboard, indicating successful authentication.

### Step 3: Forward the Modified Request and Verify Access

**Context**: Send the tampered request to the server and check for successful login, confirming the injection worked by gaining access without the correct password.

**Instructions**: In Burp, forward the request from the Proxy/Intruder tab or resend from Repeater. Monitor the response for authentication success indicators like set-cookie headers or dashboard content.

> If using curl, inspect the response body for success messages or HTML indicating logged-in state. Failure would show error like "Invalid credentials" (HTTP 401/403).

## Expected Output

Successful execution produces an HTTP 200 response with authentication tokens, session cookies, or a redirect to a protected page, granting access as the targeted user without knowing the password.
