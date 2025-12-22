---
id: dead20bf-0186-4fff-9539-c8100809beab
name: NoSQL-Injection-Authentication-Bypass-Using-Not-Equal-or-Greater
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.421773+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Authentication Bypass]]'
  - '[[tags/Exploit]]'
  - '[[tags/NoSQL Injection]]'
commands:
  - '[[commands/curl-nosql-injection-auth-bypass-form]]'
  - '[[commands/curl-nosql-injection-auth-bypass-json]]'
platforms:
  - Web
tools: []
validated: true
---

# NoSQL-Injection-Authentication-Bypass-Using-Not-Equal-or-Greater

## Summary

This procedure demonstrates how to bypass authentication in web applications using NoSQL databases like MongoDB by injecting query operators such as $ne (not equal), $gt (greater than), $lt (less than), $regex, and $nin into login form fields. By crafting payloads that manipulate the database query to return all records or ignore authentication checks, an attacker can gain unauthorized access without valid credentials.

## Description

NoSQL injection targets applications that directly embed user input into database queries without proper sanitization. In authentication scenarios, login forms often construct queries like {username: input_username, password: input_password}. An attacker injects MongoDB operators to alter this logic, for example, using $ne: null to match any username not equal to null, effectively bypassing the check. This exploit works on vulnerable web apps using MongoDB or similar NoSQL backends, typically over HTTP POST requests to login endpoints. Success grants access to the application as an authenticated user, potentially exposing sensitive data like user records or admin functions. The procedure assumes a web proxy like Burp Suite for interception and assumes the target uses unsanitized input in queries.

## Requirements

1. Access to the target's login page over HTTP/HTTPS.
2. Knowledge of the login form fields (e.g., username, password).
3. Tools for sending HTTP requests, such as curl or a browser with developer tools.
4. Optional: Intercepting proxy like Burp Suite to modify requests.
5. Target application must use NoSQL (e.g., MongoDB) with direct input injection.

## Defense

- Implement input validation and sanitization to strip or escape special characters and operators like $ne, $gt.
- Use parameterized queries or an ORM that binds parameters safely, preventing injection.
- Apply web application firewalls (WAFs) to detect and block anomalous payloads containing MongoDB operators.
- Enforce multi-factor authentication (MFA) to add layers beyond username/password.
- Regularly audit and fuzz login endpoints for injection vulnerabilities.

## Objectives

1. Bypass the authentication mechanism without valid credentials.
2. Gain unauthorized access to the protected application resources.
3. Extract or manipulate sensitive data post-bypass.

## Instructions

### Step 1: Identify the Login Endpoint and Form Fields

**Context**: Locate the login form and confirm it accepts POST requests with username and password fields. Use browser developer tools or intercept traffic to observe the normal request format.

Intercept the login request using a proxy and note the endpoint URL (e.g., http://target.com/login) and field names.

### Step 2: Craft and Send Form-Encoded Payload

**Context**: Use URL-encoded form data to inject operators that make the query always true, such as $ne to exclude invalid values or $nin to avoid specific strings.

**Command** ([[commands/curl-nosql-injection-auth-bypass-form]]):
```bash
curl -X POST -d 'username[$ne]=toto&password[$ne]=toto' http://target.com/login
```

> This sends a payload where the query becomes {username: {$ne: 'toto'}, password: {$ne: 'toto'}}, matching any credentials not equal to 'toto' (i.e., all valid users). Expected output: Successful login response, such as a redirect to the dashboard or session cookie.

Test variations like login[$regex]=a.*&pass[$ne]=lol to match any username starting with 'a'.

### Step 3: Craft and Send JSON Payload

**Context**: If the application accepts JSON requests, inject operators directly into the JSON body to bypass authentication.

**Command** ([[commands/curl-nosql-injection-auth-bypass-json]]):
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$ne": null}, "password": {"$ne": null}}' http://target.com/login
```

> This crafts a query like {username: {$ne: null}, password: {$ne: null}}, returning all non-null credentials. Expected output: Authentication success without valid input. Try alternatives like {"username": {"$gt": ""}, "password": {"$gt": ""}} for empty string comparisons.

### Step 4: Verify Access and Extract Data

**Context**: Confirm bypass by checking for authenticated features, such as accessing user profiles or admin panels.

After successful response, inspect cookies or tokens. If access granted, enumerate data via subsequent requests.

**Success Indicators**:
- HTTP 200 or redirect to authenticated page instead of 401/403.
- Session established without error messages.
- Access to restricted resources.
