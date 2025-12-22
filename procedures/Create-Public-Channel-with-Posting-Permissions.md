---
id: proc-001
tags:
  - mattermost
  - channel-setup
  - permissions
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.524Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create Public Channel with Posting Permissions

## Summary

This procedure sets up a public channel in Mattermost and configures initial posting permissions for members and guests, enabling subsequent steps in privilege escalation testing by allowing legitimate access before revocation.

## Description

In the context of testing Mattermost's permission enforcement, an admin or channel owner creates a public channel and explicitly grants posting rights via the System Console. This establishes a baseline where users can post, facilitating request capture. The target environment is a Mattermost instance with System Console access. Expected outcome: A channel ready for permission changes and request interception, highlighting the vulnerability in permission re-validation.

## Requirements

1. Admin access to Mattermost System Console
2. Valid user session in the web interface
3. Network connectivity to the Mattermost server

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) with granular channel permissions
- Monitor System Console changes via audit logs for unauthorized permission modifications
- Enforce server-side validation on all API requests, including session and permission checks

## Objectives

1. Establish a testable public channel
2. Grant temporary posting access for request capture
3. Prepare for permission revocation to simulate read-only enforcement

## Instructions

### Step 1: Access System Console and Create Channel

**Context**: Log in as an admin and navigate to channel management to create the target channel.

**Instructions**: In Mattermost, go to System Console > Channels > Public Channels, click 'Add Channel', name it 'mikefourchannel', set type to public, and save.

> This creates the channel visible to all users.

### Step 2: Configure Posting Permissions

**Context**: Set permissions to allow posting, enabling legitimate user actions.

**Instructions**: In System Console > Permissions > Channels, enable 'Allow guests to post messages' and 'Allow members to post messages' for public channels, then apply to 'mikefourchannel'.

> Permissions are now active, allowing posts from members and guests.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[mattermost]]
- [[channel-setup]]
- [[permissions]]
