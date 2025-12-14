---
id: uuid-2
tags:
  - oauth
  - twitter-api
  - request-token
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:33:34.360Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Generate-OAuth-Request-Token-with-Leaked-Credentials

## Summary

Using extracted Twitter consumer credentials from the Periscope app, generate an OAuth 1.0a request token to initiate the authorization flow with a manipulated callback URL.

## Description

This procedure leverages the leaked consumer key/secret to authenticate with Twitter's OAuth endpoint, requesting a temporary token. The callback URL is set to a partial path vulnerable to traversal. Targets Twitter API; requires HTTP client for signed requests. Outcome: Request token for victim authorization.

## Requirements

1. Valid Twitter consumer key and secret.
2. OAuth 1.0a signing library or manual signature generation.
3. Network access to api.twitter.com.

## Defense

Defensive measures and detection strategies:

- Rotate consumer keys if leaks detected.
- Rate limit API calls from known app credentials.
- Log anomalous request token generations.

## Objectives

1. Obtain request token and secret.
2. Prepare authorization URL for victim.
3. Set up callback for later bypass.

## Instructions

### Step 1: Prepare OAuth Parameters

**Context**: Define base parameters including the traversable callback.

Set `oauth_consumer_key`, `oauth_nonce`, `oauth_signature_method=HMAC-SHA1`, `oauth_timestamp`, `oauth_version=1.0`, and `oauth_callback=a/../../login?redirect_after_login=https://cards.twitter.com/card_id`.

> Use a unique nonce and current timestamp; callback path is key for traversal.

### Step 2: Generate Signature and Request

**Context**: Sign the request and POST to Twitter endpoint.

Base string: `POST&https%3A%2F%2Fapi.twitter.com%2Foauth%2Frequest_token&[percent-encoded params]`. Sign with consumer secret. Send POST request.

> Expected: Response body with `oauth_token=...&oauth_token_secret=...&oauth_callback_confirmed=true`.

### Step 3: Build Authorization URL

**Context**: Construct URL for victim to authorize.

Format: `https://api.twitter.com/oauth/authorize?oauth_token=[token]`.

> This URL will be sent to victim; confirm token works by accessing it.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1078.004]] Cloud Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[oauth]]
- [[twitter-api]]
