---
tags:
  - xss
  - stored-xss
  - payload-injection
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
updated_at: '2025-12-14T03:15:31.452Z'
sub_techniques: []
id: 5c0a5a48-832e-4e3b-a31d-012ae8f6a075
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Asset-in-Veris

## Summary

This procedure injects a stored XSS payload into the asset name field of the Veris application, persisting malicious JavaScript for later execution in associated views.

## Description

The core exploitation step stores unsanitized JavaScript in the asset name, which is later reflected without encoding in the members page. Target: https://sandbox.veris.in/portal/assets/. Prerequisites include member and group setup. Outcome: Payload stored, ready for trigger; impacts include potential JS execution leading to session theft.

## Requirements

1. Authenticated session with asset creation permissions
2. Associated member and group from prior steps
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Sanitize all asset name inputs (e.g., HTML escape < >)
- Validate asset names against script patterns
- WAF rules to block script tags in creation endpoints

## Objectives

1. Persist XSS payload in asset data
2. Associate asset with member/group chain
3. Enable execution in victim context

## Instructions

### Step 1: Inject Payload in Asset Creation

**Context**: Use the assets form to store the malicious name, linking if possible to the setup entities.

No command; direct UI:

- Access https://sandbox.veris.in/portal/assets/
- Initiate 'Create Asset'
- Set Name: `<script>alert(1);</script>`
- Optional: Link to member/group; add description 'Test'
- Submit

> Expected: Asset saved; payload visible in list but inert until triggered. Test with dev tools for storage confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
