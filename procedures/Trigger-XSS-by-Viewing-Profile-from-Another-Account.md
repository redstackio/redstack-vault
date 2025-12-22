---
tags:
  - xss-trigger
  - session-hijacking
  - client-side-execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.143Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9b15f5f7-eb0e-49cc-97de-1c30c9c14789
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Profile-from-Another-Account

## Summary

This procedure triggers the execution of the stored XSS payload by loading the vulnerable profile page from a separate authenticated session, demonstrating JavaScript execution in the viewer's browser context.

## Description

The profile page at `/people/%email%` inserts the stored name fields into JavaScript without escaping, executing the payload (e.g., `alert(document.domain)`) in the viewer's session. This can lead to session hijacking or data theft. The attack relies on social engineering or legitimate viewing. Prerequisites include the payload being injected and a second account.

## Requirements

1. Second authenticated account to simulate a victim.
2. Knowledge of the target profile URL with the injected payload.
3. Web browser for viewing.

## Defense

Defensive measures and detection strategies:

- Validate and escape all outputs in JavaScript contexts on dynamic pages.
- Use browser security features like XSS auditors or extensions.
- Monitor for unexpected JavaScript alerts or console errors in user sessions.

## Objectives

1. Execute injected JavaScript in a victim context.
2. Confirm payload activation via alert or further exploitation.
3. Demonstrate potential for broader client-side attacks.

## Instructions

### Step 1: Authenticate Second Account

**Context**: Simulate a victim user to avoid same-origin issues.

Log out of the attacker account and log in with a different account on marketplace.informatica.com.

> Ensure a clean session is established.

### Step 2: Load Vulnerable Profile

**Context**: Trigger rendering of the injected profile to execute the payload.

Navigate to `https://marketplace.informatica.com/people/%email%`, replacing `%email%` with the attacker's email address.

> The page loads, and the alert should pop up immediately, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[session-hijacking]]
- [[client-side-execution]]
