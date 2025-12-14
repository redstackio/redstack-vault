---
id: proc-uuid-3
tags:
  - saml
  - impersonation
  - auth-bypass
  - xml
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.233Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit Faked SAML Response for User Impersonation

## Summary

This procedure crafts and submits a forged SAML assertion after disabling verification, allowing login as any targeted user, including administrators, in a Rocket.Chat instance.

## Description

With signature checks bypassed, attackers can generate a custom SAML response XML impersonating a user (e.g., setting NameID to an admin email). This is submitted via the SAML login flow, leveraging the now-falsy certificate setting to skip validation. Targets web-based SAML integrations in Rocket.Chat; requires prior disable step. Outcomes: Full session hijack and privilege escalation.

## Requirements

1. Forged SAML XML (e.g., with arbitrary user attributes)
2. Browser or proxy to intercept/submit POST requests
3. Disabled verification from previous procedure

## Defense

Defensive measures and detection strategies:

- Enforce mandatory certificate validation in SAML settings
- Validate all incoming SAML responses server-side beyond signatures
- Log and alert on login attempts with mismatched or suspicious assertions
- Use multi-factor auth (MFA) post-SAML to add layers

## Objectives

1. Authenticate as arbitrary user via forged response
2. Gain administrative access in Rocket.Chat
3. Demonstrate complete auth bypass chain

## Instructions

### Step 1: Initiate SAML Login Flow

**Context**: Trigger the SAML authentication to capture the submission point.

Click the SAML login button on the page to start the IdP redirect simulation.

> Intercept the POST to the ACS (Assertion Consumer Service) endpoint using dev tools or a proxy.

### Step 2: Craft and Submit Forged Response

**Context**: Replace the legitimate response with a faked one targeting a user.

Modify the SAML XML to include desired user details (e.g., <saml:NameID>admin@target.com</saml:NameID>), then submit via POST to the callback URL.

> Example forged snippet:
```xml
<samlp:Response ...>
  <saml:Assertion ...>
    <saml:Subject>
      <saml:NameID>admin@target.com</saml:NameID>
    </saml:Subject>
  </saml:Assertion>
</samlp:Response>
```
Expected: Redirect to dashboard as impersonated user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- saml
- impersonation
- auth-bypass
- xml
