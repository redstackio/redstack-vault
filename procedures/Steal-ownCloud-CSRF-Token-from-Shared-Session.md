---
tags:
  - csrf
  - token-theft
  - shared-session
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:03.071Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b979c6db-b88f-4272-9c24-8b8ab9f1b841
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Steal-ownCloud-CSRF-Token-from-Shared-Session

## Summary

This procedure involves extracting the static CSRF authenticity token from an active ownCloud session on a shared workstation, enabling its reuse for subsequent attacks.

## Description

In ownCloud, the CSRF token does not regenerate after login, remaining static across sessions on the same device. An attacker with physical access can inspect the browser to copy this token, which serves as the primary CSRF protection. This allows forging requests that appear legitimate when a victim logs in later on the same machine. The attack relies on shared physical access and targets web-based file sharing actions.

## Requirements

1. Physical access to a shared workstation with an active ownCloud login
2. Browser developer tools access (e.g., Chrome DevTools)
3. Knowledge of ownCloud's session structure

## Defense

Defensive measures and detection strategies:

- Regenerate CSRF tokens on login and per session
- Implement device binding or IP checks for tokens
- Monitor for unusual physical access to shared devices
- Use multi-factor authentication to limit session persistence

## Objectives

1. Obtain the static CSRF token value
2. Verify token reusability without session invalidation
3. Prepare for crafting forged requests

## Instructions

### Step 1: Access Shared Session

**Context**: Gain temporary control of the workstation with an ongoing ownCloud session to inspect elements without logging out.

No specific command required; use browser interface to open Developer Tools (F12) and navigate to the ownCloud dashboard.

> Locate the token in network requests, form elements, or local storage under keys like 'requesttoken'.

### Step 2: Extract Token

**Context**: Copy the token value for reuse, confirming it remains unchanged.

Inspect the page source or use console to query the token:

```javascript
console.log(document.querySelector('input[name="requesttoken"]').value);
```

> Expected output: A static string like 'abc123def456...', which does not change on page refresh or actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-theft]]
