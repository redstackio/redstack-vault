---
id: proc-trigger-user-leak-3930
tags:
  - oauth
  - token-theft
  - phabricator
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
  - '[[Steal Application Access Token]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:35.410Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[Drive-by Compromise]]'
---
# Trigger User Interaction for Token Leak

## Summary

This procedure involves providing the chained OAuth link to a user, who authorizes with one click, leading to automatic redirection through Phabricator and token leakage to the attacker site.

## Description

In the scenario, the user clicks the external provider's OAuth link (e.g., Facebook), authorizes the app, and is redirected to the malicious Phabricator URL, which auto-redirects to the attacker, appending the OAuth token or code. This requires minimal interaction and works without Phabricator login. Target is any user of integrated services; outcomes include stolen credentials for account takeover.

## Requirements

1. Crafted chained OAuth URL from prior steps
2. Social engineering to get user click (e.g., phishing link)
3. Attacker site logging redirects

## Defense

Defensive measures and detection strategies:

- Implement OAuth state parameters to prevent CSRF
- Detect and block drive-by redirects in proxies
- User training on verifying OAuth app permissions

## Objectives

1. Obtain user authorization with single click
2. Leak OAuth token/code via redirect chain
3. Enable downstream account compromise

## Instructions

### Step 1: Distribute Chained Link

**Context**: Share the URL via email, site, or message to entice click.

No command; example link: the FB chained URL from previous procedure.

**Expected Output**: User receives and clicks the link.

### Step 2: Monitor Authorization Flow

**Context**: As user authorizes, track the redirects.

Use server logs on attacker site:

```bash
# On attacker site, log incoming requests
tail -f /var/log/nginx/access.log | grep "token"
```

> Filters for token params. Expected: Query string with code or token.

### Step 3: Validate Leak

**Context**: Confirm token receipt and test usability.

Inspect logs or use the token in API calls.

**Expected Output**: Valid OAuth token for provider API access.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- token-theft
- phabricator
