---
id: e2c48955-fa67-44c0-a8aa-71003f1098a4
name: Execute-Stored-Cross-Site-Scripting-Attack
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T15:47:48.948265+00:00'
updated_at: '2023-05-26T01:06:57.108768+00:00'
platforms:
  - Web
tags:
  - owasp
  - owasp-top-10
  - stored-xss
  - web-applications
  - xss
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands:
  - '[[commands/curl-post-xss-to-user-form]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Execute-Stored-Cross-Site-Scripting-Attack

## Summary

This procedure demonstrates how to perform a stored cross-site scripting (XSS) attack by injecting a malicious script into a web application's form field, such as a user's first name during registration. The script is persisted in the database and executes when an administrator or other user views the affected data, potentially leading to session hijacking, data theft, or further compromise.

## Description

Stored XSS occurs when user-supplied input containing malicious JavaScript is stored on the server (e.g., in a database) without proper sanitization and then rendered in the browser of subsequent users who access the page. This procedure targets vulnerable web applications with insufficient input validation on form submissions, such as user registration or profile update pages. It assumes a scenario where an attacker has unauthenticated access to submit data and can observe execution via another account or social engineering. The attack leverages JavaScript execution in the victim's browser, mapping to MITRE ATT&CK technique T1059.007 (JavaScript). Successful execution can enable phishing, keylogging, or credential theft within the application's context.

## Requirements

1. Access to a vulnerable web application with a form that stores user input (e.g., registration or profile form) without sanitizing HTML/JS.
2. Knowledge of the form's submission endpoint (e.g., POST to /register or /update-profile).
3. Ability to view the stored data from another account (e.g., admin panel) or entice a victim to access it.
4. Tools like Burp Suite for intercepting and modifying requests, or curl for automated submission.
5. A basic XSS payload, such as an alert box for testing.

## Defense

Defensive measures include:
- Input validation and sanitization using libraries like DOMPurify or OWASP ESAPI to strip dangerous tags.
- Content Security Policy (CSP) headers to restrict script execution.
- Output encoding when rendering user data (e.g., HTML entity encoding).
- Web Application Firewall (WAF) rules to detect and block common XSS patterns.
- Detection via monitoring for anomalous JavaScript execution in browser logs or server-side anomaly detection.

## Objectives

1. Inject and store a malicious script in the application's database via a vulnerable form field.
2. Trigger execution of the script when the stored data is loaded by an admin or victim.
3. Verify successful XSS by observing alert popups or other payload effects, confirming browser code execution.

## Instructions

### Step 1: Identify Vulnerable Form and Prepare Payload

**Context**: Locate a form field that accepts user input and stores it without sanitization, such as the 'First Name' in a registration form. Prepare a test XSS payload to inject, ensuring it's not escaped when stored and rendered.

Use the basic XSS payload from [[codes/basic-alert-xss-payload]] to confirm vulnerability.

Intercept the form submission using [[tools/Burp-Suite]] to modify the input if needed.

### Step 2: Submit Malicious Payload to Storage Endpoint

**Context**: Submit the form with the XSS payload in the vulnerable field to persist it in the database. This step assumes a POST request to an endpoint like /register; adjust based on the target application.

**Command** ([[commands/curl-post-xss-to-user-form]]):
```bash
curl -X POST http://target-app.com/register \
  -d "first_name=<script>alert('XSS')</script>&email=victim@example.com&submit=Register" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

> This command sends the XSS payload in the 'first_name' parameter. Expected output is a success response (e.g., HTTP 200 or redirect to profile page) confirming submission. If using a browser, enter the payload manually and submit; use Burp to tamper if direct submission escapes it.

### Step 3: Access Stored Data to Trigger Execution

**Context**: Log in as an admin or navigate to the page that displays the stored user data (e.g., /admin/users-list). The injected script will execute in the browser when the data is rendered without encoding.

No specific command is needed here; use the application's UI. If automated, use [[commands/curl-post-xss-to-user-form]] variant to fetch the list:
```bash
curl -X GET http://target-app.com/admin/users-list -b "session_cookie=your_admin_cookie"
```

> Observe the response or browser execution. Expected output includes the payload rendered as HTML, triggering the alert('XSS') popup in the viewing browser, confirming execution.

### Step 4: Verify and Escalate

**Context**: Confirm the alert or other effects (e.g., cookie theft via advanced payload). Escalate by replacing the alert with a more malicious script, such as one that exfiltrates session cookies to an attacker-controlled server.

Monitor network traffic with Burp Suite for any data leaks. Success is indicated by the payload executing in the victim's session.
