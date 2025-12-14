---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - redirect-manipulation
  - oauth-misconfig
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.637Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-OAuth-successRedirectUrl

## Summary

This procedure intercepts and modifies the successRedirectUrl parameter in the OAuth flow of admin.8x8.vc to direct the post-authentication redirect to an attacker-controlled domain, enabling code leakage.

## Description

The vulnerability stems from lack of validation on the redirect URI during OAuth negotiation. By tampering with the parameter using browser tools or a proxy, an attacker can set it to a malicious endpoint. This occurs in the web-based admin addition process targeting Gmail OAuth. Prerequisites: Active OAuth flow and a registered attacker domain.

## Requirements

1. Proxy tool or browser dev tools for interception
2. Attacker-controlled domain (e.g., evil.com) with a callback endpoint
3. Ongoing session in the target application

## Defense

Defensive measures and detection strategies:

- Enforce strict whitelist for allowed redirect URIs in OAuth config
- Log and alert on anomalous redirect parameters
- Use state parameters to prevent tampering

## Objectives

1. Bypass redirect validation
2. Set arbitrary domain for code reception
3. Maintain flow integrity for victim authentication

## Instructions

### Step 1: Intercept the OAuth Request

**Context**: Capture the request containing the successRedirectUrl during flow initiation.

Use browser developer tools (F12 > Network tab) or a proxy to monitor requests. When the add account button is clicked, intercept the GET/POST to the OAuth authorize endpoint.

> Look for the URL parameter like successRedirectUrl=https://admin.8x8.vc/callback.

### Step 2: Modify the Parameter

**Context**: Change the redirect to attacker domain and forward the request.

Edit the successRedirectUrl to https://attacker.com/callback?state=xyz. Drop or forward the modified request to proceed to Gmail.

> Ensure the client_id and other params remain intact to avoid errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[redirect-uri]]
- [[parameter-tampering]]
