---
id: p-concrete-trigger-xss
tags:
  - xss
  - stored-xss
  - execution
  - concrete-cms
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:03.699Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS on Admin Page

## Summary

This procedure involves directing or waiting for the administrator to view the community points actions page, where the injected XSS payload executes in their browser, allowing JavaScript control within the admin context.

## Description

After injection, the unsanitized parameters (upaName, upaHandle) are output raw on pages like `/index.php/dashboard/users/points/actions/action_saved`, triggering the stored XSS. This can lead to alert prompts, cookie theft, or keylogging. Prerequisites: Successful prior injection. Expected outcome: JavaScript execution confirming compromise.

## Requirements

1. Injected malicious action in the CMS
2. Admin access to the points actions page
3. Monitoring for execution (e.g., via payload callback)

## Defense

Defensive measures and detection strategies:

- Output encoding (e.g., htmlspecialchars) for all dynamic content
- Content Security Policy (CSP) to restrict inline scripts
- Browser-based XSS auditors and anomaly detection in session logs

## Objectives

1. Execute the stored payload in admin browser
2. Demonstrate impact (e.g., prompt or data exfil)
3. Enable follow-on attacks like session theft

## Instructions

### Step 1: Direct to Trigger Page

**Context**: Guide the admin to the vulnerable view.

Phish or wait for the admin to navigate to Dashboard > Users > Points > Actions or the saved action detail.

### Step 2: Observe Execution

**Context**: Confirm the payload runs.

The page renders upaHandle as `<sVg/OnLOaD=prompt(1)>`, executing `prompt(1)` onload. Replace with advanced payload for real exfil (e.g., send cookies to attacker server).

### Step 3: Validate Impact

**Context**: Check for successful JavaScript control.

Look for alert box or network request from the payload. If using a beacon, confirm receipt on attacker side.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (XSS trigger)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- javascript
