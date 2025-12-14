---
id: proc-configure-malicious-oidc
tags:
  - configuration
  - oidc
  - payload-injection
  - xss
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
updated_at: '2025-12-14T17:29:28.878Z'
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
# Configure-Malicious-OIDC-Discovery-Endpoint

## Summary

This procedure configures the user_oidc app with a malicious discovery endpoint that embeds an XSS payload in the authorization_endpoint field, storing it for later injection during login flows.

## Description

In the Nextcloud admin settings, add an OIDC provider pointing to a controlled endpoint (e.g., a PHP script returning crafted JSON). The JSON includes an injected payload like '<svg/onload=alert(document.domain)>', which evades initial validation and gets stored. When the login initiates on Safari, LoginController.php inserts it unescaped into a meta refresh tag, enabling the stored XSS.

## Requirements

1. Enabled user_oidc app
2. Control over a web server to host the discovery endpoint (returns valid OIDC JSON with payload)
3. Admin access to Nextcloud settings

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all OIDC discovery responses server-side before storage
- Implement URL encoding for all inserted values in response generation (e.g., htmlspecialchars in PHP)
- Monitor admin logs for suspicious provider configurations and audit OIDC endpoints

## Objectives

1. Store the malicious payload in Nextcloud's OIDC configuration
2. Ensure the discovery endpoint returns a valid but injected JSON document
3. Set up for Safari-specific trigger without immediate detection

## Instructions

### Step 1: Access OIDC Settings

**Context**: Navigate to provider configuration.

**Instructions**: In Nextcloud admin settings, go to "External sites" or user_oidc specific config, and add a new provider.

> Expected output: Form fields for identifier, client_id, client_secret, and discovery endpoint.

### Step 2: Input Malicious Endpoint

**Context**: Set the discovery URL to the payload-hosting script.

**Instructions**: Enter identifier: "malicious-provider", client_id: "test", client_secret: "test", discovery endpoint: https://lhq.at/poc_jkhfdasgfdaskjlfadskhfdas.php. Save the configuration. Ensure the endpoint returns: {"issuer":"http:\/\/idp.local:3000", "authorization_endpoint":"'\" http-equiv=><svg\/onload=alert(document.domain)>"}.

> Expected output: Provider saved, Nextcloud fetches and caches the document; no errors if JSON is parsable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[configuration]]
- [[oidc]]
- [[payload-injection]]
- [[xss]]
