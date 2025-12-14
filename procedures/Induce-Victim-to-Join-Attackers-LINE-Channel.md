---
id: p3b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - social-engineering
  - victim-engagement
  - channel-join
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.541Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Induce-Victim-to-Join-Attackers-LINE-Channel

## Summary

This procedure uses social engineering to get the victim to join the attacker's LINE Channel, thereby linking their account to the Notifications Channel service for later exploitation.

## Description

Joining a LINE Channel registers the user's account in the associated services, including notifications. By tricking the victim into joining, the attacker exposes the victim's notification data to potential cross-channel access via the authentication bug. This step relies on phishing or pretexting over web or app interfaces.

## Requirements

1. Generated channel invite link from the attacker's channel
2. Communication channel with victim (e.g., email, social media)
3. Monitoring access to LINE admin panel

## Defense

Defensive measures and detection strategies:

- Educate users on verifying channel invites and avoiding unsolicited joins
- Implement join confirmation prompts with security warnings
- Log and alert on mass join attempts or suspicious channel activities

## Objectives

1. Get victim to interact with the malicious channel
2. Confirm linkage in the Notifications service
3. Set up for data access without direct victim compromise

## Instructions

### Step 1: Generate Invite Link

**Context**: Create a shareable link for the channel.

In the LINE channel admin panel, navigate to the sharing options and generate a public invite QR code or URL.

### Step 2: Deliver to Victim

**Context**: Use social engineering to prompt the join.

Send the invite via a pretext, such as "Join this exclusive group for updates," through email or messaging, encouraging the victim to scan or click.

### Step 3: Verify Join

**Context**: Confirm the victim's participation.

Check the channel members list in the admin panel to see the victim's account added, indicating linkage to the notification service.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[victim-engagement]]
- [[channel-join]]
