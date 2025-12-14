---
id: uuid-3
tags:
  - configure
  - malicious
  - endpoint
  - xss
  - oidc
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.338Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Configure-Malicious-Discovery-Endpoint

## Summary

This procedure sets up a Nextcloud OIDC provider using a malicious discovery endpoint that injects an XSS payload into the authorization_endpoint field, storing the vulnerability for later triggering.

## Description

By controlling the discovery endpoint (e.g., a PHP script returning crafted JSON), the attacker injects a payload like "'\\\" http-equiv=><svg\\/onload=alert(document.domain)>" into the authorization_endpoint. Nextcloud fetches this during configuration and stores it, leading to unescaped inclusion in HTML during Safari logins.

## Requirements

1. Enabled user_oidc app
2. Control over a web server for the endpoint (returns .well-known/openid-configuration JSON)
3. Admin access to Nextcloud

## Defense

Defensive measures and detection strategies:

- Validate and sanitize OIDC discovery responses
- Implement strict allowlists for provider endpoints
- Log and alert on suspicious JSON fields in configs

## Objectives

1. Inject XSS payload via discovery
2. Store malicious config in Nextcloud
3. Enable reflection in login flow

## Instructions

### Step 1: Access OIDC Settings

**Context**: Navigate to provider configuration.

**Instructions**: In Nextcloud admin settings > Authentication > OpenID Connect, click 'Add provider'.

> Expected: Form for identifier, client_id, client_secret, etc.

### Step 2: Enter Malicious Details

**Context**: Fill in fields to point to the controlled endpoint.

**Instructions**: Set identifier (arbitrary), client_id (arbitrary), client_secret (arbitrary), discovery endpoint to https://lhq.at/poc_jkhfdasgfdaskjlfadskhfdas.php. Save.

> The endpoint must return JSON like {"authorization_endpoint": "'\\\" http-equiv=><svg\\/onload=alert(document.domain)>"}. Expected: Config saved, endpoint fetched.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- configure
- malicious
- endpoint
- xss
- oidc
