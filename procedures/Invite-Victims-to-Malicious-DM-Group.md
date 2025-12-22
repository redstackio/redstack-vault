---
id: proc-invite-victims-dm
tags:
  - social-engineering
  - victim-invite
  - twitter-dm
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:07.993Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Invite-Victims-to-Malicious-DM-Group

## Summary

This procedure invites targeted victims to a Twitter DM group containing a malicious XSS payload in the name, exposing them to the vulnerability when they access TweetDeck.

## Description

Once the malicious DM group is created, any member can invite others using Twitter's DM features. Invitations can be sent directly or via group sharing, allowing the attacker to add 100-200 victims efficiently. This step propagates the persistent XSS, as the unsanitized group name will be fetched and rendered in TweetDeck for all members. It requires no special access beyond a standard Twitter account and relies on social engineering to encourage victims to join and use TweetDeck.

## Requirements

1. Existing malicious DM group with XSS payload.
2. List of target usernames or emails for invitation.
3. Twitter account with invite permissions in the group.

## Defense

Defensive measures and detection strategies:

- Limit DM group invite capabilities or require approval for large-scale additions.
- Alert users to suspicious group names containing script-like content.
- Rate-limit DM invitations to prevent mass targeting.

## Objectives

1. Expose multiple victims to the malicious group name.
2. Increase the attack surface for XSS triggering.
3. Facilitate widespread payload execution.

## Instructions

### Step 1: Open the Malicious Group

**Context**: Access the group to initiate invitations.

Log into twitter.com, navigate to Messages, and open the malicious DM group.

### Step 2: Add Victims via Invite

**Context**: Use Twitter's invite interface to add targets.

Click the group info or members icon, then select 'Add people' or send direct invites. Enter usernames (e.g., @victim1, @victim2) and confirm up to 100-200 additions in batches if needed.

### Step 3: Confirm Invitations

**Context**: Verify victims have joined.

Monitor the group member list for new additions. Victims will see the group in their DMs upon acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[victim-invite]]
- [[twitter-dm]]
- [[propagation]]
