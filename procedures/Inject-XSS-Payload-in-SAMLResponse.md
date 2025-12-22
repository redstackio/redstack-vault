---
tags:
  - xss
  - reflected-xss
  - payload-injection
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.999Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9ad12d07-eec3-47b1-af8e-71c594d137d3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-SAMLResponse

## Summary

This procedure exploits a reflected XSS vulnerability in the SAMLResponse parameter of a Cisco ASA web services interface by intercepting and modifying the POST request, leading to arbitrary JavaScript execution in the victim's browser.

## Description

Targeting CVE-2020-3580, the procedure uses a proxy tool to intercept the SAML POST request during VPN login. The SAMLResponse parameter is modified to inject HTML/JavaScript payload, which is reflected unsanitized in the server's response. This executes in the browser context, potentially allowing theft of session cookies, keystrokes, or other sensitive data. Prerequisites include proxy setup and access to the login flow; outcomes confirm exploitation via alert popup or console logs.

## Requirements

1. Proxy tool like [[tools/Burp-Suite]] installed and configured as browser proxy
2. Access to the SAML endpoint POST request from the login flow
3. Knowledge of basic HTTP request manipulation

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs in SAML parameters on the server side
- Deploy content security policy (CSP) headers to restrict script execution
- Monitor for unusual JavaScript payloads in web traffic logs and block via IDS/IPS

## Objectives

1. Inject and reflect malicious JavaScript via SAMLResponse
2. Execute arbitrary code in the web interface context
3. Demonstrate potential for session hijacking or data exfiltration

## Instructions

### Step 1: Intercept POST Request

**Context**: Capture the SAML POST request using a proxy to prepare for modification.

Configure [[tools/Burp-Suite]] proxy (default: 127.0.0.1:8080) in browser settings. Replay the login to intercept the request to `/+CSCOE+/saml/sp/acs?tgname=a`.

> The intercepted request body will contain `SAMLResponse=[base64_encoded_value]`. Do not forward yet.

### Step 2: Modify SAMLResponse with Payload

**Context**: Inject the XSS payload to break out of the expected HTML context.

Edit the request body to: `SAMLResponse="><svg/onload=alert('Renzi')>[original_base64_value]`. Forward the request.

> The payload `"><svg/onload=alert('Renzi')>` closes any open tags and injects an SVG element that executes JavaScript on load.

### Step 3: Verify Execution

**Context**: Confirm the reflection and execution in the response.

Observe the server's HTML response for the unencoded payload, triggering the alert.

> Successful execution shows a browser alert with 'Renzi'. Inspect response source to verify reflection without HTML entity encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[reflected-xss]]
- [[payload-injection]]
- [[JavaScript]]
