---
tags:
  - csrf
  - html
  - javascript
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/set-timeout-for-redirect]]'
platforms:
  - Web
techniques:
  - '[[User Execution]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5783950d-d86c-4e8f-9e50-8abe84c6b016
created_at: '2025-12-13T09:01:26.509Z'
updated_at: '2025-12-13T09:01:26.509Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Craft Malicious HTML for Login CSRF

## Summary

This procedure involves creating a malicious HTML page that uses an iframe and JavaScript to initiate a Login CSRF attack on HackerOne's SSO-SAML system, forcing a login without user interaction.

## Description

The attack exploits the lack of anti-CSRF protections in the SAML login flow. By crafting an HTML page with an iframe loading a specific source and a timed redirect to the sign_in endpoint, an attacker can force the victim into a malicious session, enabling further exploits like open redirects or Self-XSS.

## Requirements

1. Ability to host HTML files
2. Knowledge of JavaScript and HTML
3. Browser for testing

## Defense

Defensive measures and detection strategies:

- Implement anti-CSRF tokens in login flows
- Monitor for unexpected redirects and session initiations

## Objectives

1. Create a PoC for Login CSRF
2. Enable forced authentication
3. Prepare for chained exploits

## Instructions

### Step 1: Create HTML Structure

**Context**: Build the base HTML with an iframe.

**Command** ([[commands/set-timeout-for-redirect]]):

```javascript
setTimeout(function(){document.location.href = "https://hackerone.com/users/saml/sign_in?email=████&remember_me=true";}, 5000);
```

> This sets up a 5-second delay before redirecting to the login endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[User Execution]]

### Sub-Techniques



## Commands Used

- [[commands/set-timeout-for-redirect]]

## Tools Used

- [[tools/Browser]]

## Tags

- [[csrf]]
- [[html]]
