---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - tweet-composition
  - promoted-content
  - twitter
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.735Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Compose-Promoted-Tweet-in-Campaign

## Summary

This procedure involves creating a promoted-only tweet within a Twitter ads campaign, generating a vulnerable HTTP POST request that includes the nullcast_flag parameter for interception and modification.

## Description

In the Ads dashboard, composing a promoted tweet sends a request to /accounts/<id>/tweet_box/create_tweet with nullcast_flag=1 to enforce promotional-only posting. This step prepares the request for proxy interception, exploiting the lack of server-side validation. It requires the Ad Manager role and operates in the web environment of ads.twitter.com.

## Requirements

1. Access to target account's ads dashboard
2. Active campaign or ability to create one
3. Proxy tool like Burp Suite configured for traffic interception

## Defense

Defensive measures and detection strategies:

- Validate all tweet creation requests server-side regardless of flags
- Rate-limit tweet compositions in ads contexts
- Monitor for unusual request patterns from ad roles

## Objectives

1. Trigger the vulnerable tweet creation endpoint
2. Generate interceptable HTTP traffic
3. Confirm promoted-only intent before bypass

## Instructions

### Step 1: Navigate to Tweet Composition

**Context**: Enter the campaign or ads creation flow.

In the dashboard, select or create a campaign and open the tweet box.

> The compose interface appears, ready for content input.

### Step 2: Submit Promoted Tweet

**Context**: Enter tweet text to initiate the POST request.

Enter sample text (e.g., "Test promoted tweet") and submit; intercept with Burp Suite.

> Request body includes nullcast_flag=1 and posts to https://ads.twitter.com/accounts/<redacted>/tweet_box/create_tweet?format=json.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- http-request
- promoted-tweet
- campaign
