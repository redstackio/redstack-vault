---
tags:
  - xss-execution
  - payload-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.747Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d60477ee-4e1e-4f30-8d5e-d0d0890cbde5
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Verify-XSS-Payload-Execution

## Summary

This procedure verifies the execution of the injected XSS payload after social login on Avito.ru, confirming arbitrary JavaScript runs in the authenticated context for potential session hijacking or phishing.

## Description

Post-authentication, Avito.ru's redirect to the unsanitized 'next' parameter executes the javascript: URI, popping an alert or running custom JS. In the attack, this occurs automatically in the victim's browser, allowing theft of session cookies via document.cookie. The web platform is the target; prerequisites include a completed login. Outcomes: Visible alert confirming success, with escalation to exfiltrate data to attacker-controlled servers.

## Requirements

1. Successful social login from prior procedure
2. Browser developer tools for inspection
3. Payload designed for verification (e.g., alert())

## Defense

Defensive measures and detection strategies:

- Sanitize all redirect parameters to whitelist HTTP/HTTPS schemes only
- Implement JS execution monitoring via browser extensions or WAF
- Analyze client-side errors for javascript: scheme attempts

## Objectives

1. Automatic payload execution on redirect
2. Verify JS context (authenticated session)
3. Demonstrate impact like cookie access

## Instructions

### Step 1: Complete Redirect

**Context**: After social auth, observe the automatic redirect.

**Instructions**: Allow the browser to follow the post-login redirect to the 'next' value.

> Payload should execute immediately.

### Step 2: Observe Execution

**Context**: Look for signs of JS running, like alert box.

**Instructions**: Note the alert displaying document.cookie or custom message.

> If no alert, check browser console for errors.

### Step 3: Verify Impact

**Context**: Confirm execution in authenticated session.

**Instructions**: Use dev tools (F12) to inspect if session cookies are accessible via JS.

> Success if alert shows auth tokens; extend to fetch() for exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[js-execution]]
- [[session-hijack]]
