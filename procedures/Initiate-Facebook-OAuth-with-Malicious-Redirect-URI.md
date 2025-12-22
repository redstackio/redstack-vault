---
tags:
  - oauth
  - misconfig
  - redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-oauth-initiate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:39.151Z'
sub_techniques: []
id: 579f241b-18d2-4bb6-b0cd-54771e7a6a42
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Initiate Facebook OAuth with Malicious Redirect URI

## Summary

This procedure crafts and initiates a Facebook OAuth authorization request using a misconfigured redirect_uri pointing to Uber's auth endpoint, setting up a chain for token theft.

## Description

The attack exploits Uber's Facebook OAuth app misconfiguration, which accepts any redirect_uri matching https://auth.uber.com/login?* without validation. By embedding a next_url parameter, the flow chains to Uber's internal endpoints. The victim is tricked into clicking a phishing link containing this URL, authorizing the app on Facebook, which then redirects to the malicious URI, carrying the OAuth token.

## Requirements

1. Knowledge of Uber's Facebook app ID (publicly discoverable)
2. Victim access to Facebook account linked to Uber
3. Attacker domain for final capture (set up later)

## Defense

Defensive measures and detection strategies:

- Implement strict allowlist for OAuth redirect_uris
- Validate all redirect parameters server-side
- Monitor for anomalous OAuth redirects in logs

## Objectives

1. Start the OAuth flow with chained redirect
2. Preserve OAuth token through initial redirect
3. Position for further chaining to exfiltrate token

## Instructions

### Step 1: Craft the Malicious OAuth URL

**Context**: Build the Facebook OAuth URL with the exploitable redirect_uri.

**Command** ([[commands/curl-oauth-initiate]]):
```bash
curl "https://www.facebook.com/v18.0/dialog/oauth?client_id=UBER_APP_ID&redirect_uri=https://auth.uber.com/login?next_url=https://login.uber.com/logout&scope=public_profile,email&response_type=token" -v
```

> This sends the request; in practice, serve as a link for victim to click. Expected output: HTML of Facebook auth dialog or redirect if automated.

### Step 2: Simulate Victim Authorization

**Context**: Assume victim authorizes; Facebook redirects to redirect_uri with token.

**Command** ([[commands/curl-oauth-initiate]]):
```bash
curl -L "https://www.facebook.com/v18.0/dialog/oauth?..." -c cookies.txt -v
```

> Use -L to follow redirect. Success: Redirect to auth.uber.com with token in URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/curl-oauth-initiate]]

## Tools Used


## Tags

- oauth
- misconfig
- initial-access
