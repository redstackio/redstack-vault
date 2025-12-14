---
id: proc-twitter-protect-web-001
tags:
  - twitter
  - mobile-web
  - privacy-settings
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Mobile Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:24:42.554Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
---
# Set-Protected-Tweets-via-Mobile-Web

## Summary

This procedure enables the 'Protect your Tweets' setting on Twitter using the mobile web interface, limiting tweet visibility to approved followers only. It sets up the condition for demonstrating the Android app override vulnerability.

## Description

In the context of the Twitter privacy vulnerability, this step involves logging into mobile.twitter.com and toggling the protection setting. This action protects tweets but can be unexpectedly overridden by the Android app. Prerequisites include a Twitter account with public tweets and a mobile browser. Expected outcome: Tweets become private, verifiable by non-follower access denial.

## Requirements

1. Valid Twitter account credentials
2. Mobile browser (e.g., Chrome on mobile) with internet access
3. Account initially having unprotected tweets

## Defense

Defensive measures and detection strategies:

- Regularly verify privacy settings across all Twitter interfaces (app and web)
- Avoid changing DM settings in the app if tweets are protected; use web for all changes
- Monitor account activity for unexpected visibility changes via Twitter's login history

## Objectives

1. Secure tweets by restricting visibility to followers
2. Establish baseline for vulnerability testing
3. Ensure protection is active before app interaction

## Instructions

### Step 1: Access Mobile Web Interface

**Context**: Log in to Twitter's mobile-optimized site to reach privacy settings.

Navigate to mobile.twitter.com in your mobile browser and log in with your credentials.

> Successful login displays the Twitter home timeline.

### Step 2: Navigate to Privacy Settings

**Context**: Locate and enable the tweet protection option.

Tap your profile icon, select Settings and privacy > Privacy and safety > Audience and tagging, then toggle 'Protect your Tweets' to on.

> A confirmation may appear; tweets are now protected, and new posts require follower approval.

### Step 3: Log Out and Verify

**Context**: Confirm the change took effect.

Log out, then log back in or check from another account to ensure tweets are hidden from non-followers.

> Non-followers see a 'These tweets are protected' message.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[privacy-settings]]
