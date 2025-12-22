---
id: uuid-register-oauth-client
tags:
  - oauth
  - client-registration
  - open-redirect
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
updated_at: '2025-12-14T17:24:26.395Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Malicious-OAuth-Client

## Summary

This procedure registers a new OAuth 2.0 client on a target authorization server using an attacker-controlled redirect URI, setting the stage for open redirect exploitation during error responses.

## Description

In OAuth 2.0 flows, clients must be registered with the authorization server, including a redirect_uri. Servers adhering strictly to RFC6749 allow arbitrary URIs during registration without validation. This enables attackers to specify malicious URIs, which are then used in error redirects (e.g., invalid scope) without user consent. The target environment is any RFC6749-compliant OAuth server allowing public client registration. Expected outcome: Obtain a client_id for crafting malicious requests.

## Requirements

1. Access to the OAuth provider's client registration endpoint (public or with basic account)
2. Control over a domain or server for the redirect_uri (e.g., http://attacker.com)
3. Basic knowledge of OAuth parameters

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect_uris during client registration
- Implement error responses that do not redirect to client-specified URIs; instead, show error pages
- Monitor for unusual client registrations with external URIs

## Objectives

1. Register a client to gain a valid client_id
2. Associate the client with an attacker-controlled redirect_uri
3. Prepare for error-triggered redirects

## Instructions

### Step 1: Access Client Registration

**Context**: Navigate to the OAuth provider's developer console or registration API to create a new client.

No specific command; use the web interface or API to submit registration form with:
- Client name: Arbitrary (e.g., "Test App")
- Redirect URI: http://attacker.com
- Grant types: authorization_code

> Submit the form. Expected output: Confirmation page with client_id (e.g., bc88FitX1298KPj2WS259BBMa9_KCfL3).

### Step 2: Verify Registration

**Context**: Confirm the client details to ensure the redirect_uri is accepted.

Access the client dashboard or use an API query to view details.

> Expected output: Client listed with the specified redirect_uri.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[oauth]]
- [[client-registration]]
- [[open-redirect]]
