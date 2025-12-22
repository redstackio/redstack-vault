---
tags:
  - oauth
  - leaked-credentials
type: procedure
tools:
  - '[[tools/tweepy]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/setup-oauth-handler]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:30:35.530Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6abe35ed-7f65-460a-a85a-34af3f957639
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Setup-OAuth-Authentication-with-Leaked-Twitter-Keys

## Summary

This procedure initializes the OAuth authentication flow using leaked official Twitter consumer keys, setting the stage for misleading user authorization that grants full API access including Direct Messages.

## Description

In this attack scenario, an attacker uses publicly leaked consumer keys from official Twitter apps (e.g., iPhone app) to create a custom OAuth handler via the Tweepy library. This allows generation of an authorization URL that displays Twitter's official but misleading permissions screen, tricking users into believing DMs are not accessible. The target environment is the Twitter API over HTTPS, requiring Python and Tweepy. Prerequisites include the leaked keys; expected outcome is a ready OAuth handler for user authorization.

## Requirements

1. Python 2.7+ or 3.x with Tweepy installed (pip install tweepy)
2. Leaked official Twitter consumer keys and secrets (e.g., iPhone: consumer_key='IQKbtAYlXLripLGPWd0HUA', consumer_secret='GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU')
3. Network access to api.twitter.com

## Defense

Defensive measures and detection strategies:

- Monitor for unusual OAuth requests using leaked consumer keys via API logs
- Educate users on verifying app permissions beyond the screen
- Implement key rotation for official consumer keys and restrict their scopes

## Objectives

1. Establish OAuth flow with alternate authentication material
2. Generate authorization URL for user interaction
3. Prepare for token exchange leading to data access

## Instructions

### Step 1: Import Tweepy and Define Keys

**Context**: Begin by importing the library and setting the leaked keys as variables.

No command here; add to script:

import tweepy
consumer_key = 'IQKbtAYlXLripLGPWd0HUA'
consumer_secret = 'GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU'

### Step 2: Initialize OAuth Handler

**Context**: Create the OAuth handler with secure mode enabled to generate the auth URL.

**Command** ([[commands/setup-oauth-handler]]):
```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Visit this URL and authorise the app to use your Twitter account: ' + auth_url
```

> This command sets up the handler and prints the URL. Expected output is the authorization URL, e.g., https://api.twitter.com/oauth/authorize?oauth_token=...

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used

- [[commands/setup-oauth-handler]]

## Tools Used

- [[tools/tweepy]]

## Tags

- oauth
- leaked-credentials
- twitter-api
