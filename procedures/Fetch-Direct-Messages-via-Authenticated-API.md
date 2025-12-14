---
tags:
  - direct-messages
  - data-collection
  - privacy-violation
type: procedure
tools:
  - '[[tools/tweepy]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/create-authenticated-api]]'
  - '[[commands/fetch-direct-messages]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:30:35.522Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5876ef3d-f7ea-4502-b8ca-42e36eaf9705
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Fetch-Direct-Messages-via-Authenticated-API

## Summary

This procedure creates an authenticated Tweepy API instance using the obtained access tokens and fetches the user's Direct Messages, proving unauthorized access despite the permissions screen's claim.

## Description

With tokens in hand, the attacker sets up a full OAuth handler and API object to call the direct_messages endpoint. This targets the Twitter API, requiring prior token exchange. Expected outcome is retrieval of all DMs, violating privacy and potentially GDPR.

## Requirements

1. Access tokens from previous exchange
2. Leaked consumer keys
3. Tweepy library

## Defense

Defensive measures and detection strategies:

- Scope official consumer keys to exclude DM read access
- Log and alert on DM API calls from third-party apps
- Implement user consent verification for sensitive scopes

## Objectives

1. Authenticate API instance
2. Collect private DM data
3. Demonstrate privacy violation

## Instructions

### Step 1: Create Authenticated API

**Context**: Initialize a new handler with tokens to build the API object.

**Command** ([[commands/create-authenticated-api]]):
```python
full_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
full_auth.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(full_auth)
```

> This creates the API. Expected output: tweepy.API object ready for use.

### Step 2: Retrieve DMs

**Context**: Call the DM endpoint to fetch messages.

**Command** ([[commands/fetch-direct-messages]]):
```python
print api.direct_messages()
```

> This prints DMs. Expected output: List of DirectMessage objects with content, sender, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/create-authenticated-api]]
- [[commands/fetch-direct-messages]]

## Tools Used

- [[tools/tweepy]]

## Tags

- direct-messages
- data-collection
- privacy-violation
