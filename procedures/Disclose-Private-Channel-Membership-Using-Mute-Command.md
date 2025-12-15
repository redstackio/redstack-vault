---
tags:
  - information-disclosure
  - rocket-chat
  - channel-enumeration
  - membership-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:51.864Z'
sub_techniques: []
id: 4e0b120c-651e-4e71-b655-f92b74feabcd
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Disclose Private Channel Membership Using Mute Command

## Summary

This procedure exploits a vulnerability in Rocket.Chat's /mute slash command (CVE-2023-28357) where the system checks target user membership in a channel before applying access control lists (ACLs), allowing authenticated users to infer if a specific username is part of a private channel they cannot access. It enables systematic enumeration of private channel members for reconnaissance purposes.

## Description

In Rocket.Chat, the /mute command is intended to mute users within a channel, but due to flawed permission checks, it first verifies if the target user exists in the channel context before enforcing ACLs. An attacker with a valid account can send /mute commands targeting arbitrary usernames in channels they have partial or no access to, observing responses that leak membership status. This information disclosure has medium severity as it compromises privacy in private channels without granting full access. The attack requires only authentication and works over the web interface, making it stealthy and low-effort.

## Requirements

1. Valid authenticated session in the Rocket.Chat instance
2. Knowledge of suspected usernames to probe
3. Access to a channel from which to execute the command (can be any accessible channel)

## Defense

Defensive measures and detection strategies:

- Implement strict ACL checks before any membership queries in slash commands
- Monitor for anomalous /mute command usage patterns, such as high-volume probes against non-members
- Enable logging of slash command executions and review for membership leak indicators
- Update to patched versions of Rocket.Chat that fix CVE-2023-28357

## Objectives

1. Confirm presence of target users in private channels without authorization
2. Enumerate full membership lists of restricted channels
3. Gather intelligence on user groupings for further attacks

## Instructions

### Step 1: Authenticate to Rocket.Chat

**Context**: Establish a session to interact with the chat interface.

Log in via the web browser to your Rocket.Chat account at the target instance URL.

> Successful login grants access to the chat rooms and slash command functionality.

### Step 2: Select or Create a Channel for Probing

**Context**: Choose a starting point to execute the /mute command; this can be any channel you have access to, as the leak occurs during membership check.

Navigate to an existing private channel or create a new one via the UI.

> The channel selection is arbitrary; the vulnerability triggers on the target user's channel membership check.

### Step 3: Execute /mute Command on Target Username

**Context**: Probe a specific username to disclose its membership in a private channel you lack access to.

In the message input field of the selected channel, type and submit: `/mute @targetusername`, replacing `targetusername` with the username to check.

> If the target is a member of the private channel, the response may confirm membership (e.g., "User muted" or similar) before ACL denial. If not, a different error occurs. Repeat for multiple usernames to enumerate.

### Step 4: Analyze Responses for Enumeration

**Context**: Interpret command outputs to build a membership map.

Collect responses: Positive membership indicators (e.g., pre-ACL confirmation) reveal members; negative ones exclude them.

> Systematic probing (e.g., against a list of known users) allows full enumeration without alerting admins.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- rocket-chat
- channel-enumeration
- membership-leak
