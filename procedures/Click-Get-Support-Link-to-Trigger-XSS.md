---
tags:
  - trigger
  - interaction
  - xss
  - shopify
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
updated_at: '2025-12-13T23:52:21.006Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5a1029cb-8796-4c59-9b57-981ecdd30460
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Click-Get-Support-Link-to-Trigger-XSS

## Summary

This procedure triggers the stored XSS by clicking the 'Get support' link in the app page sidebar, causing the unsanitized shop contact email to render and execute the injected JS.

## Description

On an apps.shopify.com app page, the sidebar includes a 'Get support' link tied to the shop's profile. Clicking it loads contact details, including the email field, without HTML escaping. This renders the stored payload, firing the onerror event. Ideal for drive-by style attacks; requires victim interaction but no further attacker input.

## Requirements

1. Loaded app page from prior step
2. Visible sidebar with support link
3. Propagated payload in shop profile

## Defense

Defensive measures and detection strategies:

- Sanitize all user-generated content in UI rendering (e.g., escape HTML entities)
- Implement JS event blocking for third-party content
- Log clicks on support links and scan for anomalous JS execution

## Objectives

1. Render the email field as HTML
2. Trigger payload execution
3. Confirm XSS in victim context

## Instructions

### Step 1: Locate and Click Link

**Context**: Identify the support trigger in the UI.

In the sidebar of the app page, locate and click the 'Get support' link.

**Expected Output**: Support interface opens, displaying shop contact info with injected email.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[trigger]]
- [[interaction]]
- [[xss]]
- [[shopify]]
