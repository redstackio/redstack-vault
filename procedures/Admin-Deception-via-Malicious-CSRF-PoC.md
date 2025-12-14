---
id: proc-004
tags:
  - phishing
  - csrf
  - deception
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.144Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Admin-Deception-via-Malicious-CSRF-PoC

## Summary

This procedure delivers the CSRF PoC to a tricked admin, leveraging their authenticated session to execute unauthorized actions like creating discounts or products in express-cart.

## Description

The PoC is hosted or emailed as a malicious link/page. When loaded by an authenticated admin, it auto-submits forged POST data to admin endpoints, bypassing protections due to session-only auth.

## Requirements

1. Generated PoC HTML file
2. Delivery method (e.g., email, phishing site)
3. Victim with active admin session

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition
- Block auto-submitting forms via browser policies
- Log and alert on admin actions from suspicious IPs

## Objectives

1. Induce victim interaction with PoC
2. Trigger forged request submission
3. Achieve unauthorized admin execution

## Instructions

### Step 1: Host or Deliver PoC

**Context**: Make the HTML accessible to the target admin.

**Command** (Hosting Example):
Use a simple HTTP server or email attachment.

> Send link to http://attacker.com/csrf-poc.html. Expected output: Victim receives and clicks.

### Step 2: Monitor Submission

**Context**: Verify the form posts from victim's browser.

**Command** (Network Inspection):
Use Burp or browser dev tools on victim side.

> Observe POST to /admin/settings/discount/create with demo params. Expected output: 200 OK response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- csrf
- deception
