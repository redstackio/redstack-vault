---
id: proc-632017-03
tags:
  - oauth
  - token-capture
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:27:49.961Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture-Login-Tokens-via-Proxy

## Summary

This procedure intercepts OAuth login requests using a proxy to capture Facebook authentication tokens for later CSRF reuse.

## Description

During Facebook login to the target site, proxy traffic to extract authResponse from POST to /php/asyncLogin.php. Tokens include accessToken, userID, signedRequest. Prerequisites: Proxy setup (e.g., Burp); perform login as attacker. Outcome: Tokens saved for malicious page.

## Requirements

1. Proxy tool like Burp Suite configured as system proxy
2. Attacker's Facebook account linked to target site
3. Browser traffic routed through proxy

## Defense

Defensive measures and detection strategies:

- Use short-lived tokens and validate on server
- Implement proxy detection (e.g., via headers)
- Log anomalous login patterns
- Enforce HTTPS and token binding

## Objectives

1. Intercept authResponse during OAuth flow
2. Extract usable tokens
3. Prepare for credential reuse

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for HTTPS traffic.

**Command** (Burp config):

> In Burp, enable invisible proxying; install CA cert in browser.

### Step 2: Perform Login and Capture

**Context**: Initiate Facebook login to trigger request.

**Command** (Browser action via proxy):

> Login to https://www.zomato.com; intercept POST /php/asyncLogin.php?access_token=... Capture body: authResponse[accessToken]=..., authResponse[userID]=..., etc.

> Expected: Full authResponse object in request history.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[oauth]]
- [[token-capture]]
- [[proxy]]
