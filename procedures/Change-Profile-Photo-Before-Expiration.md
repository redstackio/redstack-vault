---
tags:
  - twitter
  - profile-manipulation
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:35.423Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 88e6f28c-cbdc-4e0a-97d2-e1f22a9de024
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change Profile Photo Before Expiration

## Summary

This procedure triggers Twitter's profile review by modifying the profile photo one day before subscription expiration, temporarily removing the verified badge and queuing it for restoration.

## Description

The exploit relies on Twitter's review process for profile changes, which removes the badge temporarily. By performing this change just before expiration, the review queue holds the restoration until after cancellation, bypassing subscription checks. This targets the account settings interface on web or iOS app.

## Requirements

1. Active Twitter Blue subscription nearing expiration.
2. Access to profile editing features.
3. New profile image file ready.

## Defense

Defensive measures and detection strategies:

- Validate subscription status before queuing reviews.
- Time-bound review processes to active subscriptions only.

## Objectives

1. Initiate profile review to remove badge.
2. Ensure review timing aligns with expiration.
3. Set up for post-expiration restoration.

## Instructions

### Step 1: Access Profile Settings

**Context**: Navigate to editable profile elements.

Open Twitter app or website, go to Profile > Edit Profile.

> Expected output: Edit interface loads.

### Step 2: Upload New Photo

**Context**: Change the profile photo to trigger review.

Select and upload a new image; save changes.

> Expected output: Badge disappears; profile under review message may appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[twitter]]
- [[profile-manipulation]]
