---
id: proc-uuid-3
tags:
  - xss
  - trigger
  - execution
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.575Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger XSS on Alerts Page

## Summary

This procedure redirects the victim to the DoD alerts page, triggering an error that displays the stored XSS payload and executes JavaScript in the victim's authenticated context.

## Description

After injection, navigating to /alerts/ or /member/options causes the system to check ID ownership, resulting in an error dialog that unsafely renders the stored malicious ID. This executes the payload, allowing actions like cookie theft or keylogging within the DoD session.

## Requirements

1. Previously injected payload stored on DoD server
2. Victim's active DoD session
3. JavaScript on attacker.com for seamless redirect

## Defense

Defensive measures and detection strategies:

- Output encoding for all dynamic content in error messages
- Monitoring for anomalous redirects or error rates
- Session validation to prevent cross-site actions

## Objectives

1. Cause error reflection of stored payload
2. Execute JavaScript in victim browser
3. Achieve data exfiltration or session compromise

## Instructions

### Step 1: Initiate Redirect

**Context**: From attacker.com, redirect to trigger the error.

Use JavaScript: `window.location.href = 'https://www.dod.mil/alerts/';`

> Expected: Browser navigates to DoD page.

### Step 2: Verify Execution

**Context**: Observe payload activation via alert or network request.

Monitor attacker.com logs for exfiltrated data (e.g., cookies sent to /steal endpoint).

> Expected: Payload fires, e.g., alert('XSS') or POST to attacker.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]

