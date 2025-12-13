---
tags:
  - saml
  - authentication-bypass
  - meteor
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/meteor-call-add-saml-service]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8a2b8c72-14f5-453e-80da-c89b7d669125
created_at: '2025-12-13T09:01:26.336Z'
updated_at: '2025-12-13T09:01:26.336Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Disable SAML Certificate Validation in Rocket.Chat

## Summary

This procedure exploits an unauthenticated Meteor method in Rocket.Chat to disable SAML signature verification by setting a custom boolean flag, allowing subsequent authentication bypass.

## Description

The vulnerability exists in the 'addSamlProvider' Meteor method, which is exposed to unauthenticated clients. By calling this method with a controlled provider name like 'Default_cert', it creates a setting that sets the certificate validation flag to false, bypassing checks for SAML responses. This is typically performed on the login page of a Rocket.Chat instance with SAML enabled.

## Requirements

1. Access to the Rocket.Chat login page
2. Browser with developer console
3. Target running Rocket.Chat with SAML authentication

## Defense

Defensive measures and detection strategies:

- Restrict unauthenticated access to Meteor methods
- Monitor for unusual Meteor calls in server logs

## Objectives

1. Disable SAML certificate validation
2. Prepare for arbitrary user authentication
3. Achieve initial access bypass

## Instructions

### Step 1: Execute Meteor Method Call

**Context**: Open the browser console on the Rocket.Chat login page and call the method to set the disabling flag.

**Command** ([[commands/meteor-call-add-saml-service]]):
```javascript
Meteor.call("addSamlService", "Default_cert")
```

> This command sets SAML_Custom_Default_cert to false, disabling validation when no certificate is provided.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/meteor-call-add-saml-service]]

## Tools Used



## Tags

- [[saml]]
- [[authentication-bypass]]
- [[meteor]]
