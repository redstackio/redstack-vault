---
tags:
  - xss
  - reflected-xss
  - web-vulnerability
  - session-hijacking
  - dod
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-Registration-Username]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the Username
  field of a U.S. Department of Defense web application's registration form,
  allowing arbitrary JavaScript execution to steal session data.
skill_level: intermediate
impact_level: high
id: f228c55b-1d55-4ddd-bddd-5dd44a8dfa60
created_at: '2025-12-14T00:11:09.440Z'
updated_at: '2025-12-14T00:11:09.440Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Username Parameter of DoD Registration Form

## Overview

This attack chain demonstrates the exploitation of a reflected Cross-Site Scripting (XSS) vulnerability in the 'Username' parameter of a registration form on a U.S. Department of Defense (DoD) web application hosted at /testweb/aeon.dll/css/Aeon.dll. The vulnerability arises from insufficient input validation, allowing an attacker to inject and execute arbitrary JavaScript in the victim's browser context. Using Burp Suite, the attacker intercepts and modifies requests to inject a payload, leading to potential theft of sensitive data like cookies and session tokens. The attack requires network access to the target web app and is suitable for penetration testing or red teaming scenarios against public-facing web applications.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Intercept Registration Request] --> B[Inject XSS Payload]
    B --> C[Submit Modified Request]
    C --> D[Execute and Verify POC]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with ASP.NET or IIS (DLL-based endpoint)
- Public-facing registration form at /testweb/aeon.dll/css/Aeon.dll
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Network access to the DoD web application
- No prior credentials needed; targets unauthenticated registration endpoint
- Burp Suite proxy configured in browser for interception

## Detailed Attack Procedures

### Step 1: Intercept Initial Registration Request
procedure: [[procedures/Exploit-Reflected-XSS-in-Registration-Username]]

**Objective**: Capture the legitimate GET request to the registration endpoint to understand the request structure and modify it for exploitation.

**Instructions**: Configure your browser to proxy traffic through Burp Suite. Navigate to the registration form and submit a test registration attempt to trigger the GET request to /testweb/aeon.dll/css/Aeon.dll. In Burp Suite's Proxy tab, intercept the request and note the form parameters.

**Expected Output**: Intercepted GET request visible in Burp, showing parameters like Username and other form fields.

**Success Indicators**:
- Request successfully intercepted
- Endpoint path confirmed as /testweb/aeon.dll/css/Aeon.dll

### Step 2: Modify Request and Inject XSS Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-Registration-Username]]

**Objective**: Convert the GET to POST and inject a JavaScript payload into the Username parameter to test for reflection without sanitization.

**Instructions**: In the intercepted request, change the method from GET to POST. Add Content-Type: application/x-www-form-urlencoded header. Set the Username parameter to a payload like 'ghovjnjv"'()%26%25<zzz><ScRiPt>alert(233)</ScRiPt>', which includes encoded characters to bypass basic filters and a script tag to execute alert(233).

**Expected Output**: Modified POST request ready in Burp Repeater tab, with payload in the body.

**Success Indicators**:
- Payload properly encoded and inserted
- Request body length around 597 characters

### Step 3: Submit Modified Request and Observe Execution
procedure: [[procedures/Exploit-Reflected-XSS-in-Registration-Username]]

**Objective**: Send the tampered request and verify JavaScript execution in the response.

**Instructions**: Forward the modified POST request from Burp Suite. Observe the response in the browser or Burp's Inspector; the payload should reflect unsanitized in the HTML, triggering the alert dialog.

**Expected Output**: Browser alert box displaying '233', confirming XSS execution. Response includes reflected payload in the rendered page.

**Success Indicators**:
- Alert executes on submission
- No sanitization errors; payload renders as HTML/JS

### Step 4: Demonstrate POC with HTML Replication
procedure: [[procedures/Exploit-Reflected-XSS-in-Registration-Username]]

**Objective**: Replicate the vulnerability locally using an HTML file to showcase the injection without relying on the live target.

**Instructions**: Create a local HTML file (e.g., poc-dod.html) mimicking the registration form. Submit the form with the same XSS payload in the Username field. Verify the alert triggers upon form submission, simulating the reflected response.

**Expected Output**: Local alert execution matching the target's behavior, as shown in demo videos.

**Success Indicators**:
- POC HTML file triggers identical JS execution
- Vulnerability reproducible offline

## Attack Chain Summary

### Key Achievements

1. Successful interception and modification of registration requests using Burp Suite
2. Injection and execution of arbitrary JavaScript via reflected XSS in Username parameter
3. Demonstration of impact through alert and potential for session theft
4. Local POC creation for verification and reporting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01*
