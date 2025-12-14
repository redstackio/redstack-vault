---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Inspect-Web-Application-Cookies-for-XSRF-Tokens
tags:
  - csrf
  - xsrf
  - cookies
  - web-security
  - inspection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.490Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Web-Application-Cookies-for-XSRF-Tokens

## Summary

This procedure involves manually inspecting a web application's cookie handling during authentication and form submissions to detect if XSRF (CSRF) tokens are stored in cookies, which is a secure design violation that can lead to bypass of CSRF protections if cookies are compromised.

## Description

In secure web applications, XSRF tokens should be generated per session and included in POST request bodies or headers for state-changing operations, not stored in cookies. Storing them in cookies allows attackers who compromise cookies (via XSS, MITM, or malware) to extract the tokens and forge requests, performing unauthorized actions like changing user account details. This procedure targets web apps like RelateIQ, where such misconfigurations were identified through browser inspection. Prerequisites include access to the application and basic knowledge of browser developer tools. Expected outcomes: Confirmation of token storage in cookies, enabling further risk assessment or exploitation simulation.

## Requirements

1. Access to the target web application with a user session.
2. Modern web browser with developer tools (e.g., Chrome, Firefox).
3. Network connectivity to the application (typically HTTPS).

## Defense

Defensive measures and detection strategies:

- Implement proper CSRF token isolation: Store tokens in session state, not cookies; validate them in request bodies/headers.
- Use HttpOnly and Secure flags on cookies to mitigate theft via XSS or interception.
- Monitor for anomalous requests lacking proper CSRF validation; employ Web Application Firewalls (WAFs) to detect token mismatches.

## Objectives

1. Identify insecure XSRF token storage in cookies.
2. Assess the potential for CSRF bypass via cookie compromise.
3. Document the vulnerability for remediation or reporting.

## Instructions

### Step 1: Authenticate to the Application

**Context**: Establish a session to trigger cookie setting, as XSRF tokens are typically generated during login.

Navigate to the login page of the target web application (e.g., RelateIQ) and authenticate with valid credentials. Open browser developer tools (F12 or right-click > Inspect) and switch to the Network tab to monitor requests.

**Expected Output**: Successful login with session cookies set, including any XSRF-related cookies.

### Step 2: Inspect Cookies During Form Submission

**Context**: Trigger a state-changing operation (e.g., form submit) to observe XSRF token usage and storage.

Submit a form or perform an action that requires CSRF protection, such as updating profile information. In developer tools, go to the Application tab (Chrome) or Storage tab (Firefox), then expand Cookies under the domain. Examine cookie names and values for embedded XSRF tokens (e.g., look for tokens in 'xsrf_token' or similar cookies).

Alternatively, in the Network tab, select a POST request and check the Request Headers or Cookies section for token presence.

**Expected Output**: Visible XSRF token values within cookie data, confirming improper storage.

### Step 3: Validate Token Exposure Risk

**Context**: Simulate compromise to understand impact.

Copy a cookie value containing the XSRF token. In a new tab or tool, attempt to replay a request using the extracted token (e.g., via curl or Postman, including the cookie). If the request succeeds without additional validation, the flaw is confirmed.

**Expected Output**: Successful forged request using the cookie-extracted token, bypassing expected CSRF checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xsrf]]
- [[cookies]]
- [[web-security]]
