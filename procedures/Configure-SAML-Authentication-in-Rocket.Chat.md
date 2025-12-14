---
tags:
  - saml
  - configuration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ec9cf885-4de5-4c07-b252-bd0f7d32257f
created_at: '2025-12-14T17:31:19.345Z'
updated_at: '2025-12-14T17:31:19.345Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Configure SAML Authentication in Rocket.Chat

## Summary

This procedure sets up SAML as the authentication provider in Rocket.Chat, enabling the vulnerable login flow that can be exploited for authentication bypass.

## Description

Rocket.Chat supports SAML for single sign-on. Configuration involves entering IdP metadata like entity ID, SSO URL, public certificate, and private key path. Once enabled, login attempts redirect to the IdP, posting the SAMLResponse back to Rocket.Chat's /auth/saml endpoint. This setup is prerequisite for intercepting and modifying responses. The target environment is a self-hosted Rocket.Chat instance with admin access.

## Requirements

1. Administrative access to Rocket.Chat settings
2. Valid IdP configuration details (e.g., from Okta, Azure AD)
3. Rocket.Chat version vulnerable to the SAML flaw (pre-patch)

## Defense

Defensive measures and detection strategies:

- Use patched Rocket.Chat versions with proper SAML validation
- Monitor SAML login attempts for anomalous XML structures
- Implement XML signature canonicalization and strict parsing

## Objectives

1. Enable SAML authentication to initiate the exploitable flow
2. Verify configuration allows IdP redirects
3. Prepare for request interception

## Instructions

### Step 1: Access Administration Panel

**Context**: Log in as admin and navigate to authentication settings.

No command required; use the web UI to go to Administration > Workspace > Settings > Authentication > SAML.

> Enter IdP details: Enable SAML, set URL, entity ID, and upload certificate.

### Step 2: Save and Test Configuration

**Context**: Apply changes and initiate a test login.

No command; click Save Changes, then attempt login to confirm redirect to IdP.

> Successful test shows SAMLResponse POST after IdP authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[saml]]
- [[configuration]]
