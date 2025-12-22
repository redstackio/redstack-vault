---
tags:
  - xss
  - execution
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.363Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 31cb9722-4ec3-4fc8-9fe4-9731fbfdb169
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-for-JavaScript-Execution

## Summary

This procedure outlines how to trigger the stored XSS payload in MercadoPago by accessing the vulnerable page, causing the malicious JavaScript to execute in the browser and perform actions like data exfiltration.

## Description

After injection, the stored script executes whenever a user loads the affected page on mercadopago.com.ar. This can lead to stealing session cookies, redirecting users, or sending keystrokes to an attacker. The attack relies on social engineering to lure victims or natural user interaction. No special tools beyond a browser are needed for triggering, but proxies help in monitoring.

## Requirements

1. Access to the stored content page
2. Victim browser session (own or induced)
3. Attacker-controlled server for receiving exfiltrated data

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and HttpOnly/Secure flags on cookies
- Implement client-side CSP headers
- Log and alert on unexpected outbound requests from web pages

## Objectives

1. Execute the injected script in browser context
2. Capture sensitive data like cookies
3. Confirm impact via attacker logs

## Instructions

### Step 1: Access Affected Page

**Context**: Navigate to the page displaying the stored input, such as a user profile or comment thread.

Log in as a test victim or share the URL. Use [[tools/Burp-Suite]] to monitor network traffic.

### Step 2: Observe Execution

**Context**: Load the page to trigger the script; watch for execution indicators.

In the browser console, look for errors or alerts. If using an exfiltration payload, check your server logs for incoming requests with stolen data.

### Step 3: Validate Impact

**Context**: Confirm the attack's success by reviewing exfiltrated information.

Expected: Network requests to attacker.com with cookie data, or visible alert('XSS executed').

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[JavaScript]]
