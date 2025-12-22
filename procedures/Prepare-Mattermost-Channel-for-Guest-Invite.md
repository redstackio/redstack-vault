---
tags:
  - mattermost
  - setup
  - invite
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8b7fbdc8-7d29-4258-a9c7-cc29b19d3d88
created_at: '2025-12-14T17:33:24.150Z'
updated_at: '2025-12-14T17:33:24.150Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Mattermost-Channel-for-Guest-Invite

## Summary

This procedure sets up a Mattermost channel and initiates the guest invite process to access the vulnerable custom message field for HTML injection.

## Description

In the context of exploiting an HTML injection vulnerability in Mattermost's invite members feature, this procedure involves navigating to the workspace, creating a new channel, and configuring the guest invitation form. It requires an authenticated user session and positions the attacker to input malicious payloads. Expected outcomes include reaching the unsanitized input field without triggering any defenses.

## Requirements

1. Authenticated access to a Mattermost workspace (e.g., via `yourworkspace.cloud.mattermost.com`)
2. Permissions to create channels and send guest invites
3. A test email address under attacker control

## Defense

Defensive measures and detection strategies:

- Enforce role-based access controls to limit invite permissions
- Monitor for unusual channel creation patterns or high-volume invites
- Implement email content scanning for suspicious HTML

## Objectives

1. Establish the attack surface by preparing the invite interface
2. Avoid detection during setup
3. Position for payload injection

## Instructions

### Step 1: Navigate and Authenticate

**Context**: Access the Mattermost instance to begin the attack workflow.

No specific command; use a web browser to visit `yourworkspace.cloud.mattermost.com` and log in with valid credentials.

> Successful login grants access to the workspace dashboard.

### Step 2: Create New Channel

**Context**: Generate a target channel for the guest invite to isolate the attack.

Use the UI: Click the "+" icon next to Channels and select "Create a new channel".

> Channel is created and visible in the sidebar.

### Step 3: Initiate Guest Invite

**Context**: Open the invite interface and configure for guest access.

Click the invite icon in the channel, enter the target email, select "Invite as guest", and add the channel name.

> Form advances to the custom message section.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mattermost]]
- [[setup]]
- [[invite]]
