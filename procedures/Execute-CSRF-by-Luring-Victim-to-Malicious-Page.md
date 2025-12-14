---
id: proc-vk-csrf-execute
tags:
  - csrf
  - social-engineering
  - impersonation
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.723Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute CSRF by Luring Victim to Malicious Page

## Summary

This procedure tricks an authorized user into visiting the crafted CSRF page, causing unauthorized Group IM actions to execute under their session, such as framing them by sending messages.

## Description

With the victim logged into VK.com and having group access, luring them to the malicious page exploits their active session and the shared hash to perform actions like sending messages to a peer_id or deleting dialogs. The timehash lasts ~7 hours, but a static variant allows persistence, ideal for revenge after losing admin access in PHP web environments.

## Requirements

1. Hosted malicious CSRF page URL
2. Social engineering access to the victim (e.g., as fellow group editor)
3. Valid shared hash within its lifespan

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Implement CSRF token rotation and user-binding
- Alert on unexpected IM actions from trusted accounts

## Objectives

1. Induce victim visit without suspicion
2. Confirm action execution from victim's account
3. Achieve impersonation or framing

## Instructions

### Step 1: Prepare Luring Mechanism

**Context**: Choose a pretext to share the URL convincingly.

Craft a message like "Check this update for the group: [malicious URL]" targeted at a fellow editor.

### Step 2: Deliver the Lure

**Context**: Send the URL via email, chat, or in-group communication.

Distribute the link to the victim, ensuring they are logged into VK.com.

### Step 3: Monitor Execution

**Context**: Verify the attack success post-visit.

Check the group IM for the unauthorized action (e.g., sent message) attributed to the victim's account. If using static hash, retest for persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
- [[impersonation]]
