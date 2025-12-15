---
tags:
  - oauth
  - twitter
  - redirect-chain
  - randomization
type: procedure
tools:
  - '[[tools/VPN]]'
  - '[[tools/Clean-Browser-Instance]]'
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Twitter
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T17:28:12.904Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f1ac3ba4-3fd4-4f0c-a035-252b5025d2d0
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Pass the Hash]]'
---
# Redirect-to-Randomized-Malicious-Twitter-OAuth

## Summary

This procedure chains redirects from a follower site to randomized malicious Twitter OAuth endpoints, evading detection by varying app targets and installing unauthorized apps on victim accounts.

## Description

From getmorefollowers.biz, redirect to freefollower.eu/redirect.php, which selects one of 10+ malicious Twitter apps via randomized oauth_token (e.g., Eqx8ggAAAAAA_RPwAAABa-oLM2U). Test with VPNs from locations like France, UAE to observe randomization in clean browsers.

## Requirements

1. Controlled redirect domains (getmorefollowers.biz, freefollower.eu)
2. Multiple malicious Twitter apps with broad DM permissions
3. VPN for geographic testing of randomization

## Defense

Defensive measures and detection strategies:

- Review and revoke suspicious third-party Twitter apps
- Block known malicious domains in redirects
- Monitor OAuth requests for unusual patterns

## Objectives

1. Obfuscate app installation via randomization
2. Direct to Twitter authenticate endpoint
3. Install app for DM automation

## Instructions

### Step 1: Initial Redirect from Follower Site

**Context**: Post-credential capture, redirect to freefollower.eu.

Implement server-side redirect on getmorefollowers.biz.

> Expected: Browser hits freefollower.eu/redirect.php.

### Step 2: Randomize and Redirect to OAuth

**Context**: Use geo-IP or random logic to select malicious app token.

In redirect.php, generate varying oauth_token and forward to api.twitter.com/oauth/authenticate.

> Expected: Twitter OAuth screen loads with randomized app.

### Step 3: Test with VPN and Clean Browser

**Context**: Verify chain evasion.

Use VPN to locations (e.g., Japan) and clean browser to follow chain.

> Expected: Different apps selected per test.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Pass the Hash]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/VPN]]
- [[tools/Clean-Browser-Instance]]

## Tags

- [[oauth]]
- [[twitter]]
- [[redirect-chain]]
- [[randomization]]
