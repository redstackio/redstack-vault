---
id: proc-register-malformed-uri
tags:
  - oauth
  - misconfiguration
  - redirect
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
updated_at: '2025-12-14T17:31:10.791Z'
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
# Register Malformed Redirect URI in OAuth App

## Summary

This procedure registers an OAuth application on Coinbase using a protocol-less redirect URI, exploiting the lack of validation to set up conditions for later malformed redirects and code interception.

## Description

In the Coinbase OAuth system, developers can register redirect URIs without requiring the HTTP/HTTPS protocol. The authorization endpoint then concatenates the base domain 'www.coinbase.com' with the provided URI, creating predictable malformed URLs like 'www.coinbase.comexample.com'. This procedure focuses on the initial app registration step, providing a foundation for token theft by enabling attacker control over the resulting domain.

## Requirements

1. Access to Coinbase developer console (free signup)
2. A domain name for the redirect URI (e.g., prashanthvarma.in)
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Enforce strict validation of redirect URIs to require protocols during app registration
- Monitor for registrations with protocol-less URIs and flag them
- Implement domain whitelisting for allowed redirects

## Objectives

1. Create an OAuth app with invalid URI format to bypass checks
2. Obtain a client_id for use in authorization flows
3. Set up for predictable redirect exploitation

## Instructions

### Step 1: Access Developer Console

**Context**: Log in or sign up to access the OAuth app creation interface.

Navigate to the Coinbase developer portal and select 'Create App' under OAuth applications.

### Step 2: Submit Malformed URI

**Context**: Enter the redirect URI without protocol to test acceptance.

In the 'Redirect URIs' field, input `prashanthvarma.in/code.php` (or similar domain/path). Complete other required fields like app name and description, then submit.

> The system accepts this without error, generating a client_id.

### Step 3: Verify Registration

**Context**: Confirm the app is active and note the client_id.

Check the app dashboard for the generated client_id, such as `3616ab93541ef90540a0c991e113b22c1ccefa96996f70fcdc49a68d900cb761`.

**Expected Output**: App listed with assigned client_id and scopes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- registration
- validation-bypass
