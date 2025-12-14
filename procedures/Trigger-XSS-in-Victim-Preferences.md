---
tags:
  - xss-trigger
  - cookie-theft
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:29.244Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 70a86467-c76e-4d38-a5ed-5b5c60b9d46f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Victim-Preferences

## Summary

This procedure induces the victim to load their preferences page, causing the injected XSS in the signature field to execute and steal session cookies via alert or exfiltration.

## Description

Direct the victim (user1) to view /settings/preferences, where the unsanitized signature renders as HTML/JS. The onerror handler in the img tag fires, alerting cookies. In production, replace alert with beacon to attacker server. Expected: Immediate execution in victim's browser context.

## Requirements

1. Victim login credentials
2. Injected XSS already in preferences
3. Social engineering to visit page if needed

## Defense

Defensive measures and detection strategies:

- Content Security Policy (CSP) to block inline scripts
- Server-side HTML sanitization for all user inputs
- Monitor for anomalous JS execution in client logs

## Objectives

1. Execute payload for data exfiltration
2. Capture session tokens
3. Enable further lateral movement

## Instructions

### Step 1: Victim Navigation

**Context**: Load the vulnerable page to render injected content.

**Command** (Browser Navigation):

Log in as user1 and visit https://app.outpost.co/settings/preferences.

> Expected: Page loads, XSS triggers alert with cookies.

### Step 2: Observe Execution

**Context**: Verify payload success.

**Command** (Manual Check):

Watch for alert(document.cookie).

> Expected: Cookies displayed; in real attack, sent to attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[xss-trigger]]
- [[cookie-theft]]
