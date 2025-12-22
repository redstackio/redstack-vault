---
id: 4dc86340-342b-4018-b8a5-3e48cf93cbe4
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T15:48:34.879652+00:00'
updated_at: '2023-05-26T15:59:03.892256+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp-top-10
  - web-applications
  - xpath-injection
commands:
  - '[[commands/curl-test-single-quote-xpath]]'
  - '[[commands/curl-inject-xpath-payload]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Authentication-Bypass-Through-XPath-Injection

## Summary

This procedure demonstrates how to bypass authentication mechanisms in web applications that use XPath queries for XML-based user validation. By injecting specially crafted payloads into the login form's username or password fields, an attacker can manipulate the XPath query to always evaluate to true, granting unauthorized access without valid credentials.

## Description

XPath injection occurs when user input from a login form is directly concatenated into an XPath query without proper sanitization, allowing attackers to alter the query logic. This is common in legacy web applications or those parsing XML for authentication data. The technique exploits the structure of XPath expressions, such as those checking username and password equality (e.g., //user[name/text()='$username' and password/text()='$password']). By closing the string and adding logical conditions like ' or '1'='1, the query returns all users, bypassing authentication. This procedure assumes a vulnerable login endpoint accepting POST requests and focuses on identification and exploitation steps. Successful bypass leads to session establishment as an authenticated user, potentially enabling further actions like data access or privilege escalation.

## Requirements

1. Network access to the target web application's login endpoint (e.g., HTTP/HTTPS).
2. Knowledge of the login form fields (typically 'username' and 'password') and submission method (POST).
3. Tools like curl for automated testing or a browser/proxy like Burp Suite for manual interception.
4. Basic understanding of HTTP requests and XPath syntax.

## Defense

Defensive measures and detection strategies:

- Use parameterized XPath queries or XML APIs that bind inputs safely (e.g., XmlDocument.SelectNodes with parameters).
- Implement input validation to reject special characters like single quotes ('), or use allowlists for alphanumeric inputs.
- Enable web application firewall (WAF) rules to detect XPath injection patterns (e.g., ' or '1'='1).
- Log and monitor authentication attempts for anomalous payloads, including error messages revealing XPath usage.
- Conduct regular code reviews and use tools like OWASP ZAP or Burp Suite for vulnerability scanning.

## Objectives

1. Confirm the presence of XPath-based authentication by triggering syntax errors.
2. Exploit the vulnerability using logical payloads to bypass login.
3. Gain unauthorized access to the application as an authenticated user.
4. Validate success through session cookies or dashboard access.

## Instructions

### Step 1: Test for XPath Injection Vulnerability

**Context**: Begin by injecting a single quote (') into the username field to disrupt the XPath query string. This should cause a syntax error if the backend uses unsanitized user input in XPath, confirming the vulnerability. Use a tool like curl to send the test request, monitoring for error messages that mention XML or XPath parsing issues.

**Command** ([[commands/curl-test-single-quote-xpath]]):
```bash
curl -X POST -d "username='&password=test" http://target.example.com/login -c cookies.txt
```

> This command sends a POST request with a single quote in the username field. The quote prematurely closes the XPath string, leading to a malformed query. If vulnerable, the response will include an error like "XPath syntax error" or "Invalid XML." If no error occurs, the input may be sanitized, and further testing is needed. Check the response body for clues.

### Step 2: Exploit with XPath Bypass Payloads

**Context**: Once the vulnerability is confirmed, inject payloads that manipulate the XPath logic to always return true. Common payloads close the original string and add a tautology (e.g., ' or '1'='1), causing the query to match any user. Test multiple variations to account for different XPath structures. Submit with a dummy password and observe if authentication succeeds without valid credentials.

**Command** ([[commands/curl-inject-xpath-payload]]):
```bash
curl -X POST -d "username=' or '1'='1&password=test" http://target.example.com/login -c cookies.txt -v
```

> Replace the payload with alternatives like ' or ''=' or x' or 1=1 or 'x'='y if the first fails. The -v flag enables verbose output to inspect headers and status codes. Success is indicated by a 200 OK response with a session cookie or redirect to a protected page, instead of an authentication failure. If successful, the attacker gains access without knowing valid credentials. Verify by accessing a post-login resource.
