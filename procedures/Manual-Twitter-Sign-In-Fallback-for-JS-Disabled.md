---
tags:
  - manual-auth
  - js-disabled
  - twitter-signin
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Twitter
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:28:12.893Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5c0e78e6-2b5a-4b46-a6aa-24a842c8d7a5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Manual-Twitter-Sign-In-Fallback-for-JS-Disabled

## Summary

Fallback procedure for JavaScript-disabled environments, where the victim manually signs into Twitter and authenticates the malicious app on freefollower.eu, ensuring installation despite automation failure.

## Description

Without JS, the OAuth automation doesn't run, so the page shows a 'Sign in with Twitter' button. Victim manually logs in and approves the app, granting permissions.

## Requirements

1. JS disabled in browser
2. Victim not logged into Twitter
3. Access to freefollower.eu page

## Defense

Defensive measures and detection strategies:

- Avoid signing into Twitter on unknown sites
- Check app requests for excessive permissions
- Block freefollower.eu domain

## Objectives

1. Handle non-JS scenarios
2. Still achieve app installation
3. Maintain attack efficacy

## Instructions

### Step 1: Display Sign-In Button

**Context**: Page loads without JS, showing manual button.

Victim sees 'Sign in with Twitter' on freefollower.eu.

> Expected: No auto-redirect.

### Step 2: Manual Authentication

**Context**: Victim clicks and logs in.

Follow Twitter's sign-in flow and approve app.

> Expected: App installed manually.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[manual-auth]]
- [[js-disabled]]
- [[twitter-signin]]
