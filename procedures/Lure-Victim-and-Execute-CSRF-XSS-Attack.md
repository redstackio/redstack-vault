---
id: p3c4d5e6-g7h8-9012-cdef-345678901234
tags:
  - phishing
  - execution
  - csrf
  - xss
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.594Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Lure-Victim-and-Execute-CSRF-XSS-Attack

## Summary

This procedure involves social engineering to deliver a malicious link to an authenticated victim, triggering the CSRF+XSS chain to perform unauthorized actions and steal session data in the DoD web application.

## Description

Once the malicious HTML is hosted, lure the victim (who must be logged in) via email or message. The page exploits the victim's cookies to send the forged POST, injecting XSS that executes in the app's context, enabling cookie theft or setting changes. Discovered via Burp testing.

## Requirements

1. Hosted malicious HTML from prior procedure
2. Victim authentication to target app
3. Delivery channel (email, chat) for phishing link

## Defense

Defensive measures and detection strategies:

- User training on phishing and suspicious links
- Browser extensions for CSRF/XSS blocking (e.g., NoScript)
- Server-side logging of session anomalies and external POSTs

## Objectives

1. Gain execution in victim's authenticated session
2. Steal sensitive data like cookies
3. Perform actions like modifying alerts or settings

## Instructions

### Step 1: Prepare Delivery

**Context**: Craft a phishing message with the link to the malicious site, e.g., disguised as a DoD update.

Example: "Click here for urgent alert: https://k0x.xyz/attack.html"

### Step 2: Monitor and Execute

**Context**: Victim visits link; auto-submit sends POST to /alerts, injecting XSS.

No command; observe via attacker server logs for request receipt and XSS callback (e.g., redirect hit).

### Step 3: Validate Impact

**Context**: Confirm XSS execution leads to alert/redirect and potential data exfil.

Check for victim-side indicators like alert popup; attacker receives any stolen data via the redirect or additional payload.

**Expected Output**: POST request logged, XSS alert in victim browser, session data potentially exfiltrated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[Execution]]
- [[csrf]]
- [[xss]]
