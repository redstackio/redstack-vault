---
type: procedure
description: >-
  Injects a malicious JavaScript payload into a vulnerable web application to
  exfiltrate victim cookies via Burp Collaborator.
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.667205+00:00'
updated_at: '2023-04-10T20:21:29.215332+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/CORS]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Exploit code or POC]]'
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# XSS-Cookie-Theft-Using-Burp-Collaborator

## Summary

This procedure demonstrates a reflected or stored Cross-Site Scripting (XSS) attack where malicious JavaScript is injected into a vulnerable web application. The payload uses the Fetch API to send the victim's cookies to a Burp Collaborator server in a no-CORS mode, allowing the attacker to capture session data for impersonation and unauthorized access.

## Description

Cross-Site Scripting (XSS) exploits insufficient input validation in web applications, enabling attackers to inject and execute arbitrary scripts in users' browsers. In this technique, the attacker identifies an injection point (e.g., a search field, comment section, or URL parameter) and inserts a payload that fetches the document.cookie and POSTs it to their controlled Burp Collaborator endpoint. Burp Collaborator polls for interactions, revealing the stolen cookies. This is effective against applications without HttpOnly flags on cookies or proper CSP. The attack targets public-facing web apps and can lead to session hijacking, especially in environments with weak session management. Prerequisites include a vulnerable input field and access to Burp Suite Professional for Collaborator setup.

## Requirements

1. Access to a vulnerable web application with an XSS injection point (e.g., unescaped user input in HTML).
2. Burp Suite Professional installed with Collaborator server configured.
3. Network access to interact with the target application (no special privileges needed beyond a standard user account).
4. Basic knowledge of web proxies and JavaScript debugging.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, output encoding (e.g., HTML entity encoding), and sanitization on all user inputs using libraries like DOMPurify.
- Set HttpOnly and Secure flags on sensitive cookies to prevent JavaScript access and ensure HTTPS transmission.
- Deploy Content Security Policy (CSP) headers to restrict script sources and block inline scripts (e.g., script-src 'self').
- Monitor for anomalous outbound requests to unknown domains and enable web application firewall (WAF) rules for XSS patterns.
- Use browser security features like XSS Auditor and regular security audits with tools like OWASP ZAP.

## Objectives

1. Identify and exploit an XSS vulnerability in a web application.
2. Exfiltrate victim session cookies to the attacker's Burp Collaborator server.
3. Use stolen cookies to impersonate the victim and access restricted resources.
4. Achieve session hijacking for further persistence or data theft.

## Instructions

### Step 1: Set Up Burp Collaborator

**Context**: Configure Burp Suite to generate a unique Collaborator payload for receiving stolen data. This step ensures the attacker can poll for interactions from the victim's browser.

Launch Burp Suite and navigate to the Collaborator tab. Click "Copy to clipboard" to generate a unique subdomain (e.g., abc123.burpcollaborator.net). Poll for interactions periodically to capture incoming requests.

**Expected Output**: A unique Collaborator URL ready for payload insertion.

### Step 2: Craft and Inject the XSS Payload

**Context**: Replace the session placeholder in the payload with your Collaborator subdomain and inject it into the vulnerable input field. This triggers the script execution in the victim's browser upon page load or interaction.

Use the following code snippet: [[codes/XSS-Cookie-Exfiltration-Script]]

To inject, submit the payload via a form, URL parameter, or other input point (e.g., append to a search query: ?q=<script>...</script>).

**Expected Output**: The payload executes silently in the browser, sending a POST request with cookies to the Collaborator endpoint.

### Step 3: Monitor and Retrieve Stolen Cookies

**Context**: Poll the Burp Collaborator server to confirm the exfiltration and retrieve the cookie data for analysis.

In Burp Suite, go to the Collaborator tab and click "Poll now". Inspect incoming HTTP requests for the POST body containing document.cookie.

If successful, copy the cookies and import them into your browser (e.g., via developer tools or extensions) to hijack the session.

**Expected Output**: Burp Collaborator logs showing an HTTP interaction with the victim's IP, user-agent, and cookie data in the request body.

### Step 4: Validate Session Hijacking

**Context**: Test the stolen cookies by accessing the application as the victim.

Paste the cookies into a browser session (using Burp's Repeater or a cookie editor extension) and navigate to protected pages.

**Expected Output**: Successful access to victim-specific resources without re-authentication.

**Success Indicators**:
- Collaborator receives a POST request with cookie data.
- No CSP or syntax errors block payload execution.
- Session hijacking grants access to victim account.
