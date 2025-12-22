---
id: proc-uuid-005
tags:
  - oauth
  - twitter
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:35.368Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform Actions on Hijacked Account

## Summary

This procedure utilizes the hijacked access token to execute unauthorized actions on the victim's Twitter account through the third-party application's interface.

## Description

Once logged into the victim's dashboard on the third-party app, the attacker can leverage the app's Twitter API integration to post tweets, manage followers, or perform other actions as if authenticated as the victim. This demonstrates the full impact of the OAuth hijacking, affecting any Twitter-integrated service.

## Requirements

1. Successful hijacking from prior step
2. Third-party app with Twitter action capabilities
3. Victim's account permissions

## Defense

Defensive measures and detection strategies:

- Revoke app permissions promptly on suspicion
- Monitor Twitter API usage for anomalous activity
- Implement rate limiting and logging on third-party apps

## Objectives

1. Execute actions via hijacked access
2. Demonstrate account takeover impact
3. Exfiltrate or manipulate victim data

## Instructions

### Step 1: Access Dashboard

**Context**: Confirm hijacked session.

Review the victim's dashboard on the app (e.g., follower stats for TwitterAccount02).

### Step 2: Execute Actions

**Context**: Use app features to interact with Twitter.

Post a tweet, follow/unfollow users, or view private data using the app's controls, all proxied through the victim's access token.

**Expected Output**: Actions reflected on victim's Twitter account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-takeover
- oauth
