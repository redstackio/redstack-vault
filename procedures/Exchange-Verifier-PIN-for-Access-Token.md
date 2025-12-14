---
tags:
  - oauth
  - access-token
type: procedure
tools:
  - '[[tools/tweepy]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/exchange-verifier-for-token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:30:35.525Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 07c9be6f-af1d-497d-be72-22883b23e40a
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Exchange-Verifier-PIN-for-Access-Token

## Summary

This procedure exchanges the user's verifier PIN from the authorization step to obtain access tokens, completing the OAuth flow and granting the attacker valid credentials for the Twitter API.

## Description

After user authorization, the attacker inputs the PIN into the script to retrieve the access_token and access_token_secret via Tweepy. This occurs in the Python environment interacting with Twitter's OAuth endpoint, building on prior setup. Expected outcome is authenticated tokens allowing API calls, including unauthorized DM access.

## Requirements

1. Verifier PIN from user authorization
2. Existing OAuth handler from setup
3. Tweepy library

## Defense

Defensive measures and detection strategies:

- Rate-limit OAuth token exchanges
- Monitor for PIN-based authentications from suspicious IPs
- Revoke tokens on detection of leaked key usage

## Objectives

1. Complete OAuth 1.0a flow
2. Acquire valid access tokens
3. Enable subsequent API access

## Instructions

### Step 1: Prompt for PIN

**Context**: Run the script to input the PIN provided by the user.

**Command** ([[commands/exchange-verifier-for-token]]):
```python
verifier = raw_input('Type in the generated PIN: ').strip()
auth.get_access_token(verifier)
```

> This exchanges the verifier for tokens. Expected output: auth.access_token and auth.access_token_secret populated (e.g., access_token='12345-...', access_token_secret='...').

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used

- [[commands/exchange-verifier-for-token]]

## Tools Used

- [[tools/tweepy]]

## Tags

- oauth
- access-token
