---
tags:
  - api-abuse
  - publish
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-publish-broadcast]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.118Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b95a35c7-84d5-4a53-87dd-b0f72f553bc0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Publish Broadcast Using Access Token

## Summary

This procedure publishes the created broadcast to Twitter using the access token, resulting in visible unauthorized content from the victim's account.

## Description

POST to /v1/broadcast/publish with the broadcast_id and tweet_text. This integrates with Twitter API to tweet the broadcast link, confirming full compromise.

## Requirements

1. Access token
2. Broadcast ID from creation step
3. Tweet text
4. curl

## Defense

Defensive measures and detection strategies:

- Confirm publications with user interaction
- Monitor Twitter API usage spikes
- Alert on broadcasts from compromised sessions

## Objectives

1. Make unauthorized content public
2. Demonstrate impact
3. Expose account compromise

## Instructions

### Step 1: Prepare Publish Data

**Context**: Include broadcast_id and text.

broadcast_id: "12345", tweet_text: "Published via CSRF"

### Step 2: Send Publish Request

**Context**: POST to publish endpoint.

Execute [[commands/curl-publish-broadcast]]:

```bash
curl -X POST https://public-api.periscope.tv/v1/broadcast/publish \
  -H "Authorization: Bearer <access_token>" \
  -d "broadcast_id=12345" \
  -d "tweet_text=Published via CSRF"
```

> Expected: Success response with publication confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-publish-broadcast]]

## Tools Used


## Tags

- [[broadcast-publish]]
- [[twitter-integration]]
