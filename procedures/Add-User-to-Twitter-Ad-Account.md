---
id: proc-add-user-twitter-ad
tags:
  - access-grant
  - lateral-movement
  - twitter-ads
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T03:16:25.364Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Add-User-to-Twitter-Ad-Account

## Summary

This procedure grants a target user (victim) access to a Twitter ad account, allowing them to view the tweets page and trigger the stored XSS payload.

## Description

As part of the XSS attack chain, adding a victim to the ad account exposes them to the vulnerable tweets page where the injected payload executes. This uses the platform's account management features to invite users via email or username and assign tweet-viewing permissions. The process requires owner-level access to the ad account. Expected outcomes include the victim gaining login access, leading to JS execution upon visiting the page.

## Requirements

1. Owner or admin permissions on the ad account.
2. Victim's Twitter username or email.
3. Active session on ads.twitter.com.

## Defense

Defensive measures and detection strategies:

- Require approval workflows for adding users to ad accounts.
- Audit account access changes and notify owners of new grants.
- Limit permissions to least privilege (e.g., view-only without tweet access).

## Objectives

1. Expose the victim to the vulnerable tweets interface.
2. Enable payload trigger without direct attacker involvement.
3. Facilitate targeted compromise of authorized users.

## Instructions

### Step 1: Navigate to Account Settings

**Context**: Access the management section for user permissions.

From the ad account dashboard, go to 'Settings' or 'People' tab in the ad account menu.

> The user management interface loads, showing current members.

### Step 2: Invite and Assign Permissions

**Context**: Add the victim and grant necessary access for XSS exposure.

Enter the victim's Twitter username or email, select permissions (e.g., 'Tweets' access), and send the invitation.

> Invitation sent; victim can accept and log in to view tweets.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-grant
- twitter-ads
