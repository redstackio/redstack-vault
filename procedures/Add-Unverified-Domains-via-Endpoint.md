---
tags:
  - domain-takeover
  - business-logic
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.188Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2d41d9ee-e2af-4bb5-89f1-fb22da3d67f5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Unverified-Domains-via-Endpoint

## Summary

This procedure exploits a business logic error in Shopify's domain addition process to register owned domains like myshopify.com without DNS verification, achieving domain takeover.

## Description

By submitting domains directly to the final endpoint in the addition flow, verification steps are bypassed. The domain appears 'Not connected' but controls traffic redirection to the attacker's store, preventing legitimate registration.

## Requirements

1. Active trial store
2. Burp Suite for request manipulation
3. Target domain (e.g., myshopify.com)

## Defense

Defensive measures and detection strategies:

- Enforce verification at all addition endpoints
- Validate domain ownership pre-registration
- Audit domain claims for owned subdomains

## Objectives

1. Register unverified owned domain
2. Redirect traffic to attacker store
3. Block legitimate domain usage

## Instructions

### Step 1: Initiate Domain Addition

**Context**: Start the domain setup process.

Navigate to store settings and begin adding a custom domain.

> Expected: Multi-step form with verification prompts.

### Step 2: Intercept Final Endpoint

**Context**: Capture and modify the submission request.

Use [[tools/Burp-Suite]] to intercept the last API call (e.g., POST to domain creation endpoint).

### Step 3: Submit Target Domain

**Context**: Bypass verification by direct submission.

In Burp Repeater, set domain to `myshopify.com` and forward without DNS steps.

> Expected: Domain added, traffic redirects to store.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[domain-takeover]]
- [[business-logic]]
