---
id: uuid-for-proc1
tags:
  - recon
  - oauth
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:43.092Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Extract-Google-Client-ID-from-Site

## Summary

This procedure involves inspecting the target WordPress site's frontend JavaScript to extract the Google Client ID used for OAuth authentication, which is necessary for crafting valid-looking JWT payloads in subsequent exploitation steps.

## Description

In the context of exploiting the Newspack Extended Access plugin, attackers need the site's Google App ID to populate the `azp` claim in a forged JWT. This is obtained by analyzing the site's authentication scripts without requiring any privileged access. The process targets public-facing resources and sets the stage for authentication bypass by mimicking legitimate Google OAuth responses.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Public access to the target WordPress site
3. Basic knowledge of JavaScript inspection

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove client IDs from client-side JavaScript
- Monitor for unusual traffic to authentication endpoints
- Implement client-side integrity checks

## Objectives

1. Retrieve the Google Client ID for JWT crafting
2. Enable payload construction for auth bypass
3. Prepare for unsigned JWT submission

## Instructions

### Step 1: Inspect Site Scripts

**Context**: Navigate to the site's login/registration page and examine loaded JavaScript for authentication configurations.

**Command** (Browser Console):
```javascript
// No command needed; use DevTools Elements tab to search for 'googleClientApiID'
```

> Open DevTools (F12), go to Sources or Network tab, search for `authenticationSettings.googleClientApiID`. Expected output: Value like `12345-abcdef.apps.googleusercontent.com`.

### Step 2: Verify Client ID

**Context**: Confirm the extracted ID is valid by checking its format.

**Command** (Browser Console):
```javascript
console.log('Extracted ID: ' + document.querySelector('script').innerHTML.match(/googleClientApiID['"]([^'"]+)['"]/)[1]);
```

> This logs the ID. Success if it matches Google's app ID pattern.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[oauth]]
