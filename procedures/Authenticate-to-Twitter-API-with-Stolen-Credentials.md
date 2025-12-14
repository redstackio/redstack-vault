---
id: proc-uuid-2
tags:
  - twitter-api
  - oauth
  - valid-accounts
  - api-auth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/twitter-oauth2-client-credentials-grant]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.568Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Twitter-API-with-Stolen-Credentials

## Summary

This procedure uses stolen Twitter consumer key and secret (extracted from an app like Reddit's APK) to perform OAuth2 client credentials grant authentication, obtaining a bearer token for unauthorized API access as the app's identity.

## Description

After extracting credentials from hardcoded app resources, attackers can authenticate to Twitter's OAuth2 token endpoint using basic auth with the consumer key:secret pair. This grants application-only access, allowing API calls that may be attributed to the legitimate app owner (e.g., Reddit). The target environment is any system with curl and internet access; prerequisites include valid extracted credentials. Outcomes include successful token issuance, enabling further API interactions like tweeting or data retrieval on behalf of the app.

## Requirements

1. Extracted Twitter consumer key and secret
2. curl installed (standard on most systems)
3. Internet access to api.twitter.com

## Defense

Defensive measures and detection strategies:

- Rotate compromised API keys immediately
- Implement rate limiting and IP whitelisting on API endpoints
- Monitor for unusual OAuth token requests from non-app sources
- Use short-lived tokens and require additional app verification

## Objectives

1. Authenticate using stolen consumer credentials
2. Obtain bearer token for Twitter API access
3. Demonstrate potential for action misattribution

## Instructions

### Step 1: Prepare Credentials

**Context**: Format the extracted key and secret for basic auth (key:secret).

No command; note the values (e.g., key=abc123, secret=def456).

### Step 2: Request Bearer Token

**Context**: Send a POST to Twitter's OAuth2 endpoint with client credentials grant.

**Command** ([[commands/twitter-oauth2-client-credentials-grant]]):
```bash
curl --user "actual_consumer_key:actual_consumer_secret" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token'
```

> This performs basic authentication and requests an app-only bearer token. Expected output: `{"token_type":"bearer","access_token":"actual_token"}`, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/twitter-oauth2-client-credentials-grant]]

## Tools Used

- None

## Tags

- [[twitter-api]]
- [[oauth]]
- [[valid-accounts]]
