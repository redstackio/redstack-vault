---
id: uuid-observe-execution
tags:
  - xss
  - execution
  - cookie-theft
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:15:35.814Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Observe-XSS-Execution-on-Affected-Pages

## Summary

This procedure navigates to pages where the stored payload is reflected, triggering JavaScript execution to demonstrate impact like cookie theft.

## Description

The payload executes in the browser context when pages render the owner's name, such as in account summaries or history views. Affected endpoints include /en/account/easypay/, /en/account/easypay/history/, /en/account/easypay/auto-sms-topup/, and /en/sims/settings/. This can lead to session hijacking.

## Requirements

1. Payload stored successfully
2. Access to the affected account pages

## Defense

Defensive measures and detection strategies:

- Output encode all reflected data (e.g., HTML escape)
- Monitor for JavaScript errors or alerts in client-side logs
- Use browser security features like XSS Auditor

## Objectives

1. Trigger and observe payload execution
2. Verify arbitrary JS capability
3. Assess potential for data exfiltration

## Instructions

### Step 1: Navigate to Affected Pages

**Context**: Load pages that display the stored mandate data.

**Instructions**: Visit URLs like https://mobilevikings.be/en/account/easypay/ or https://mobilevikings.be/en/account/easypay/history/111366/.

> An alert should pop up showing cookies; modify payload for real exfiltration (e.g., send to attacker server).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- cookie-theft
