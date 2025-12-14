---
tags:
  - xss-trigger
  - csp-block
  - execution-attempt
type: procedure
tools:
  - '[[tools/Custom-Links-App]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6e5fb7d1-00d6-4a76-9e69-a374e5121175
created_at: '2025-12-13T23:56:03.571Z'
updated_at: '2025-12-13T23:56:03.571Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Custom-Link-for-XSS

## Summary

This procedure triggers the stored malicious link in the Stripe dashboard to attempt JavaScript execution, revealing CSP protections.

## Description

After creating the custom link with a javascript: payload, clicking it simulates how a team member might interact, attempting to run the alert(1) script. The browser navigates to the URI, but Stripe's CSP prevents inline execution, resulting in a safe failure. This tests the stored XSS vector's viability and underscores the need for scheme validation. Requires the link to be created and visible in the dashboard.

## Requirements

1. Malicious custom link already created in products
2. Browser session in Stripe dashboard
3. No special permissions beyond view access

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers blocking javascript: and unsafe-inline
- Log and alert on failed script executions in dashboard
- Educate users on verifying links before clicking

## Objectives

1. Initiate payload execution via link click
2. Observe CSP intervention
3. Confirm no code runs in the victim context

## Instructions

### Step 1: Locate the Link

**Context**: Find the stored custom link in the products interface.

No command required; scroll to the product with the custom link.

> The link appears as a clickable element with the injected URL.

### Step 2: Click to Trigger

**Context**: Simulate victim interaction by clicking the link.

No command required; click the custom link.

> Browser attempts execution but shows CSP refusal; no alert pops up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Links-App]]

## Tags

- [[xss-trigger]]
- [[csp-block]]
- [[execution-attempt]]
