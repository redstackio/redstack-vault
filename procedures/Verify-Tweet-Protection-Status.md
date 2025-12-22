---
id: proc-twitter-verify-protection-001
tags:
  - twitter
  - verification
  - privacy-status
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:24:42.540Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
---
# Verify-Tweet-Protection-Status

## Summary

This procedure checks whether a Twitter account's tweets are protected or public by testing visibility from different access points, crucial for validating the privacy override vulnerability.

## Description

Post-setting changes, verify status by attempting access from non-follower accounts or incognito sessions. Applies to both Android app and mobile web. Prerequisites: Test account (non-follower), main account credentials. Expected outcome: Confirmation of protected (hidden) or unprotected (visible) state.

## Requirements

1. Main Twitter account with known status
2. Secondary non-follower account for testing
3. Access to app and/or web interfaces

## Defense

Defensive measures and detection strategies:

- Periodically self-verify protection status after any setting changes
- Use Twitter's 'Your Twitter data' download to audit visibility
- Enable two-factor authentication to prevent unauthorized changes

## Objectives

1. Validate current privacy level
2. Detect unintended exposure from app bugs
3. Ensure settings sync correctly across platforms

## Instructions

### Step 1: Check from Main Account

**Context**: View profile on the account itself to see indicator.

In the app or web, go to your profile; look for 'Protect your Tweets' label or lock icon.

> Protected status shows if enabled.

### Step 2: Test from Non-Follower Account

**Context**: Simulate public access to confirm visibility.

Log in to a secondary account not following the target, search for the username, and view recent tweets.

> If protected, see 'These tweets are protected'; if not, tweets load publicly.

### Step 3: Use Incognito or Logout Mode

**Context**: Additional check without credentials.

Open an incognito browser tab to mobile.twitter.com, search the username without logging in.

> Unprotected tweets appear; protected ones do not.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[privacy-status]]
