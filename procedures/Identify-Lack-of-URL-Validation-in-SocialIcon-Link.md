---
tags:
  - xss
  - url-validation
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-url-scheme]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:38.299Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d4e5dce8-fac7-4ac6-ba44-ebc47bb6182f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Lack of URL Validation in SocialIcon Link

## Summary

This procedure tests the SocialIcon Link input field in Linktree for inadequate URL validation, confirming acceptance of dangerous schemes like 'javascript:' that enable stored XSS.

## Description

In the attack scenario, attackers with basic account access probe the URL input to identify sanitization flaws. The target environment is Linktree's web profile editor. Expected outcomes include confirmation of the vulnerability, setting the stage for payload injection. Prerequisites include a Linktree account and browser access.

## Requirements

1. Valid Linktree user account
2. Browser with developer console (e.g., Chrome DevTools)
3. Network access to linktr.ee

## Defense

Defensive measures and detection strategies:

- Implement strict URL scheme whitelisting (e.g., only http/https)
- Server-side validation of all user inputs
- Content Security Policy (CSP) to block inline JS execution
- Monitor for anomalous API calls to /api/token

## Objectives

1. Verify acceptance of non-standard URL schemes
2. Document the lack of sanitization for reporting
3. Prepare for payload crafting

## Instructions

### Step 1: Access SocialIcon Link Input

**Context**: Log in to Linktree and navigate to the profile editor's SocialIcon section to locate the URL input field.

**Command** ([[commands/test-url-scheme]]):
```javascript
// In browser console or input field, test: javascript:alert(1)
```

> Submit 'javascript:alert(1)' as the URL. If accepted and renders without error, validation is lacking. Expected output: No rejection; potential alert on render.

### Step 2: Test Arbitrary Schemes

**Context**: Expand testing to confirm broad acceptance of schemes.

**Command** ([[commands/test-url-scheme]]):
```javascript
// Test data: URI or file:// schemes
```

> Input variations like 'data:text/html,<script>alert(1)</script>'. Success if stored and rendered without stripping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-url-scheme]]

## Tools Used


## Tags

- [[xss]]
- [[url-validation]]
