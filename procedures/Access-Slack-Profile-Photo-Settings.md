---
tags:
  - slack
  - profile-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.063Z'
sub_techniques: []
id: 8241d0d8-ac23-4470-ab03-3cb93654fb3c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Slack-Profile-Photo-Settings

## Summary

This procedure navigates to the Slack profile photo settings page, enabling the use of Facebook integration for photo uploads where the vulnerability can be triggered.

## Description

The attacker or victim accesses the account settings in Slack to reach the photo upload interface. This step positions the user to select the Facebook import option, which fetches album data and reflects unsanitized content from Facebook.

## Requirements

1. Valid Slack account credentials
2. Web browser access to Slack workspace
3. Team membership in Slack

## Defense

Defensive measures and detection strategies:

- Require multi-factor authentication for profile changes
- Log access to profile settings and monitor for unusual activity
- Educate users on risks of third-party integrations

## Objectives

1. Reach the photo upload interface in Slack
2. Enable Facebook integration option
3. Set up for payload reflection

## Instructions

### Step 1: Log In to Slack

**Context**: Authenticate to the Slack workspace.

Visit https://app.slack.com and sign in with credentials.

### Step 2: Navigate to Profile

**Context**: Access personal profile settings.

Click the profile picture in the top-right corner, select "View profile", then "Edit profile".

### Step 3: Go to Photo Settings

**Context**: Locate the photo change option.

Click on the current photo or navigate to https://yourteam.slack.com/account/photo to open the upload interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- slack
- profile-access
