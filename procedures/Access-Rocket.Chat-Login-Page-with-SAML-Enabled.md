---
id: proc-uuid-1
tags:
  - saml
  - rocket-chat
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T17:31:11.241Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Rocket.Chat Login Page with SAML Enabled

## Summary

This procedure involves navigating to the login page of a Rocket.Chat instance configured with SAML authentication using the default provider, setting the stage for further exploitation without requiring any credentials.

## Description

Rocket.Chat's login interface exposes SAML options when enabled. Attackers can access this page publicly to inspect configurations and prepare client-side interactions like Meteor method calls. The target environment is a web-based chat platform running on Meteor.js with SAML integration via meteor-accounts-saml. Prerequisites include public accessibility of the instance; expected outcome is confirmation of SAML enablement for subsequent steps.

## Requirements

1. Web browser with developer tools
2. Public URL to the Rocket.Chat instance
3. SAML authentication enabled on the target

## Defense

Defensive measures and detection strategies:

- Restrict login page access via IP whitelisting or CAPTCHA
- Monitor access logs for anomalous browser user-agents or patterns
- Disable SAML if not required or enforce strict IdP configurations

## Objectives

1. Confirm SAML availability on the login page
2. Establish client-side access for unauthenticated methods
3. Validate default provider 'Default' configuration

## Instructions

### Step 1: Navigate to Login Page

**Context**: Load the target's login interface to verify SAML setup.

**Command** (Browser Navigation):

Navigate to `https://target-rocketchat.com/login` in your browser.

> Inspect the page source or UI for SAML buttons/providers. Look for 'Default' provider indicators.

### Step 2: Verify SAML Enablement

**Context**: Ensure SAML is active to proceed with exploitation.

**Command** (Console Check):
```javascript
console.log(Meteor.isClient);
```

> This confirms client-side environment; check for SAML-related elements in DOM (e.g., via `document.querySelector('[data-saml-provider]')`).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- saml
- rocket-chat
- reconnaissance
