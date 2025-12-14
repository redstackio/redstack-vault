---
id: proc-uuid-1
tags:
  - xss
  - initial-access
  - hackerone
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:47.607Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Victims-HackerOne-Session

## Summary

This procedure outlines delivering and executing an XSS payload in a victim's authenticated HackerOne session to enable further exploitation of sensitive DOM elements.

## Description

In the context of HackerOne's web application, an XSS vulnerability allows arbitrary JavaScript execution in the victim's browser while authenticated. The attacker tricks the victim into interacting with malicious content (e.g., a phishing link) that injects a script into the HackerOne domain. This grants access to session-bound pages like the authentication edit form without additional credentials. Prerequisites include identifying an XSS vector in HackerOne and victim interaction.

## Requirements

1. Identified XSS vulnerability in HackerOne domain
2. Victim's authenticated session (e.g., via phishing to maintain cookies)
3. Attacker-controlled server for payload hosting

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution in browser logs
- Use XSS auditors like DOMPurifier in Ruby on Rails

## Objectives

1. Execute JavaScript in victim's HackerOne session
2. Maintain session integrity for subsequent steps
3. Avoid detection by not altering page behavior noticeably

## Instructions

### Step 1: Deliver XSS Payload

**Context**: Host or inject the payload to target the victim's interaction with HackerOne.

No specific command; use social engineering to direct victim to a malicious URL that reflects/executes XSS on https://hackerone.com.

> Example: Embed <script>alert(1)</script> in a user-controlled input that renders on HackerOne pages.

### Step 2: Verify Execution

**Context**: Confirm script runs in the correct domain and session.

Open browser dev tools and check console for payload output.

> Expected: Console logs or alerts confirming execution without logout.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[initial-access]]
