---
id: proc-algolia-trigger-display-001
tags:
  - xss
  - stored-xss
  - algolia
  - execution
type: procedure
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.219Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-XSS-on-Display-Settings-Save

## Summary

This procedure triggers the Stored XSS payload execution directly on the Algolia admin Display settings page upon saving the faceting configuration.

## Description

After selecting the malicious attribute, saving the display settings causes the UI to re-render the attribute list in HTML without sanitization, executing the JavaScript payload multiple times. This affects authenticated admins, potentially leading to session compromise. Builds on prior injection and config steps. Outcomes: Immediate JS execution in a privileged context.

## Requirements

1. Faceting configured with malicious attribute
2. Authenticated admin session
3. Display settings page access

## Defense

Defensive measures and detection strategies:

- Implement client-side escaping for all dynamic attribute renders
- Use Content Security Policy (CSP) to block inline scripts
- Log and alert on JS errors or alerts in admin panels

## Objectives

1. Execute payload in admin context
2. Confirm vulnerability in privileged UI
3. Demonstrate multi-execution impact

## Instructions

### Step 1: Save and View Display Settings

**Context**: Force rendering to trigger the payload.

After adding to faceting, click Save on the Display page, then refresh or revisit it.

> The onerror in the img tag executes, popping alerts for document.domain. Multiple renders (e.g., list items) cause repeated executions. Verify via browser console for errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[algolia]]
