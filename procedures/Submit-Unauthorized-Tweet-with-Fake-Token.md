---
tags:
  - csrf-bypass
  - tweet-posting
  - unauthorized-action
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:23.690Z'
sub_techniques: []
id: 4a27286c-4257-4fff-ac1c-a366f879eca9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Submit Unauthorized Tweet with Fake Token

## Summary

This procedure submits a tweet composition form on mobile.twitter.com using the forged m5_csrf_tkn=x, bypassing CSRF protection and posting content on behalf of the user.

## Description

With the fake token parsed as valid, the form POST to tweet creation endpoint succeeds without proper CSRF verification. This allows arbitrary state-changing actions, demonstrated by posting 'wut -.-' via a PoC page.

## Requirements

1. Forged CSRF token from cookie parsing
2. Access to compose tweet form on mobile.twitter.com
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Double-submit CSRF tokens with additional headers
- Log and alert on anomalous token values
- Rate-limit form submissions

## Objectives

1. Post unauthorized tweet
2. Demonstrate full bypass impact
3. Exfiltrate or manipulate user data

## Instructions

### Step 1: Access Compose Form

**Context**: Navigate to tweet composition interface.

Visit the tweet compose page on mobile.twitter.com.

> Form loads with fake token in hidden field or header.

### Step 2: Submit Form with Payload

**Context**: Fill and POST the form using the fake token.

Use PoC at http://blackfan.ru/twitterbugbounty/485d0a1204ff970e702aabb5f0379d73_tweet.html or manual submission with body including status='wut -.-' and m5_csrf_tkn=x.

> Server accepts POST, tweet is created and visible in timeline.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- submission
- bypass
