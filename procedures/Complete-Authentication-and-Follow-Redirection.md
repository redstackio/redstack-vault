---
tags:
  - token-theft
  - redirection
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:23.043Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b11d3754-58e5-4a2b-aa23-69dab7e7c4c8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Unsecured Credentials]]'
---
# Complete-Authentication-and-Follow-Redirection

## Summary

This procedure finalizes the OAuth authentication and observes the malicious redirection, allowing the attacker to capture the Disqus access token on the controlled site.

## Description

After approving on the OAuth provider, Phabricator processes the callback but fails to validate the redirect due to the backslash manipulation, sending the user (and token) to the attacker's site. This enables theft of Disqus tokens for further abuse, though Facebook tokens remain secure due to provider restrictions.

## Requirements

1. OAuth provider login credentials
2. Prior steps completed (URL loaded, provider selected)
3. Attacker-controlled site ready to intercept tokens

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all redirect URIs in OAuth callbacks, rejecting non-standard characters like backslashes
- Use token binding or short-lived access tokens
- Monitor for unexpected redirects in OAuth logs and alert on token exfiltration attempts

## Objectives

1. Authorize the Phabricator app on the provider
2. Trigger and confirm the open redirect
3. Intercept the access token on the malicious endpoint

## Instructions

### Step 1: Authenticate and Approve

**Context**: This completes the flow, exploiting the vulnerability to redirect post-auth.

No command required; enter credentials on the provider site, then click "Authorize" or "Allow" for Phabricator access.

> Expected output: After approval, the browser redirects to the malicious site (e.g., attacker.com/callback?token=...), where the Disqus token is exposed in the URL or query parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- token-theft
- malicious-redirect
