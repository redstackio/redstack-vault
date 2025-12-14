---
tags:
  - auth-bypass
  - openid
  - forgery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 47b07e10-408f-4444-a017-8cf17130269d
created_at: '2025-12-14T17:31:42.522Z'
updated_at: '2025-12-14T17:31:42.522Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Complete-Authentication-with-Arbitrary-IDP

## Summary

This procedure uses an arbitrary OpenID 2.0 IDP to forge an authentication response, impersonating an existing Airflow user by crafting identity claims that the backend trusts without validation.

## Description

After redirection to the arbitrary IDP, the attacker controls the response generation. The backend (Flask-AppBuilder) does not verify the IDP's trustworthiness, accepting forged attributes like claimed_id and identity that match an Airflow user. This leads to session creation and unauthorized access. Requires control over the IDP or ability to simulate responses.

## Requirements

1. Control over the arbitrary IDP (e.g., openstackid.org or self-hosted)
2. Knowledge of target user's identity details (username, email)
3. Ongoing proxy session from prior steps

## Defense

Defensive measures and detection strategies:

- Enforce IDP URL validation and certificate pinning
- Implement response signature verification for OpenID claims
- Audit logs for logins from unexpected IDPs

## Objectives

1. Generate forged OpenID response matching target user
2. Trick backend into creating valid session
3. Achieve impersonation without credentials

## Instructions

### Step 1: Handle IDP Redirect

**Context**: Receive and process the authentication request at the IDP.

Upon server redirect, the IDP receives parameters like openid.mode=checkid_setup. Parse these to prepare the response.

> Ensure the IDP is ready to respond with custom claims.

### Step 2: Forge Identity Response

**Context**: Craft OpenID attributes to impersonate the user.

Generate a response with openid.ns=http://specs.openid.net/auth/2.0, openid.mode=id_res, openid.claimed_id=target-user-id, openid.identity=target-user-id, and signed attributes matching the target Airflow account (e.g., email=user@example.com).

> Use tools like OpenID libraries to sign the response if needed.

### Step 3: Send Response Back

**Context**: Redirect the user agent to Airflow with the forged response.

Construct the redirect URL to Airflow's callback (e.g., /login/?openid.mode=id_res&...) including all forged parameters. Ensure the response is trusted by the backend.

> Expected: Backend validates and accepts, creating a session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[openid]]
- [[forgery]]
