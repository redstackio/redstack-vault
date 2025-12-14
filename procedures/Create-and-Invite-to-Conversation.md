---
tags:
  - conversation-setup
  - xss-delivery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.388Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c1798f51-f7e1-4a9c-a644-0796aea7b705
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-and-Invite-to-Conversation

## Summary

This procedure sets up a new conversation in Nextcloud Talk and invites the victim, creating the context for adding the malicious project.

## Description

The Talk/Spreed app allows conversations with integrated projects, where files can be linked. Creating a dedicated conversation ensures the victim engages with the projects tab, triggering the filename display vulnerability.

## Requirements

1. Access to Nextcloud Talk app
2. Victim user added as a contact or searchable
3. Attacker permissions to create conversations

## Defense

Defensive measures and detection strategies:

- Limit conversation invites to trusted users
- Audit new conversations and participants
- Train users to avoid unknown shared conversations

## Objectives

1. Establish a shared communication channel
2. Include the victim without raising suspicion
3. Enable project linking in the conversation

## Instructions

### Step 1: Create New Conversation

**Context**: Initiate a new group or direct conversation.

Open the Talk app, click '+ New conversation', and enter a neutral name like 'Project Discussion'.

### Step 2: Invite Victim

**Context**: Add the victim to ensure they can view projects.

In the conversation settings, go to Participants > Add participant, search for the victim, and invite them.

**Expected Output**: Conversation created; victim receives invite and can join.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[talk-app]]
- [[invitation]]
