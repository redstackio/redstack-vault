---
id: proc-uuid-2
tags:
  - saml
  - auth-bypass
  - meteor
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/meteor-call-addSamlService]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.238Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Disable SAML Signature Verification via addSamlService

## Summary

This procedure exploits the unauthenticated `addSamlService` (or `addSamlProvider`) Meteor method in Rocket.Chat to set a custom SAML certificate flag to false, effectively disabling signature validation and enabling forged response acceptance.

## Description

The vulnerability stems from the method being exposed client-side without authentication checks, allowing arbitrary setting of `SAML_Custom_${provider}_cert` to falsy values. When executed on the login page with SAML enabled, it modifies backend settings, causing the `verifySignatures` function to skip checks if the certificate is absent or false. This targets Meteor.js-based Rocket.Chat instances with SAML (meteor-accounts-saml). Prerequisites: Access to login page; outcomes include bypassed auth for impersonation.

## Requirements

1. Browser console access on SAML-enabled login page
2. Knowledge of default provider name ('Default')
3. No server-side auth enforcement on Meteor methods

## Defense

Defensive measures and detection strategies:

- Implement server-side authentication for all Meteor methods
- Audit and remove exposed settings endpoints
- Enable logging for Meteor method calls and monitor for anomalous `addSamlService` invocations
- Use certificate pinning and mandatory signature enforcement in SAML config

## Objectives

1. Set SAML certificate validation to disabled
2. Prepare for forged SAML response submission
3. Achieve unauthenticated configuration tampering

## Instructions

### Step 1: Open Browser Console

**Context**: Prepare client-side execution environment on the login page.

Open developer tools (F12) and switch to the Console tab.

> Ensure the page is loaded with SAML options visible.

### Step 2: Execute addSamlService Call

**Context**: Invoke the method to create a falsy certificate setting for the 'Default' provider.

**Command** ([[commands/meteor-call-addSamlService]]):
```javascript
Meteor.call("addSamlService", "Default_cert");
```

> This prefixes the setting as 'SAML_Custom_Default_cert' and sets it to false. Expected output: Silent success or minimal console response; no errors indicate compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/meteor-call-addSamlService]]

## Tools Used


## Tags

- saml
- auth-bypass
- meteor
- javascript
