---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - information-disclosure
  - privacy-misconfiguration
  - wakatime
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Employee Names]]'
updated_at: '2025-12-14T17:30:35.746Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Employee Names]]'
---
# Create-WakaTime-Private-Leaderboard

## Summary

This procedure outlines how to create a private leaderboard on WakaTime, serving as the initial setup for exploiting the privacy misconfiguration that discloses private emails to members.

## Description

In the context of WakaTime's platform, private leaderboards are intended to limit visibility to invited members only. However, due to a misconfiguration, joining such a leaderboard exposes private user details like emails without respecting privacy settings. This step requires a WakaTime account and access to the web dashboard. The outcome is a controlled leaderboard ready for invitations, enabling subsequent steps in the disclosure attack.

## Requirements

1. Active WakaTime account with dashboard access
2. Web browser with JavaScript enabled
3. Internet connectivity to wakatime.com

## Defense

Defensive measures and detection strategies:

- Implement strict privacy checks in backend API responses for member data
- Audit leaderboard invitation flows for PII exposure
- Monitor for anomalous leaderboard creations and joins via logging

## Objectives

1. Establish a private leaderboard to control the attack environment
2. Prepare for targeted invitations to specific users
3. Validate leaderboard functionality without triggering alerts

## Instructions

### Step 1: Access WakaTime Dashboard

**Context**: Log in to initiate the leaderboard creation process.

Navigate to wakatime.com, sign in with your credentials, and go to the main dashboard where productivity tracking features are listed.

### Step 2: Initiate Leaderboard Creation

**Context**: Use the UI to set up a new private instance.

Locate the 'Leaderboards' section, click 'Create New Leaderboard', select 'Private' visibility, provide a name and description, then submit the form.

### Step 3: Confirm Creation

**Context**: Verify the leaderboard is active and private.

Check the dashboard for the new leaderboard entry, note its URL, and ensure no public sharing options are enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Employee Names]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[privacy-misconfiguration]]
