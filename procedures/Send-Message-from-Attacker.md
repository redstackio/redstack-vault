---
tags:
  - messaging
  - tumblr
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
updated_at: '2025-12-14T17:26:56.423Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d57cfe5-e61e-4ba6-9111-a288dde4c3c2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Message-from-Attacker

## Summary

This procedure details logging into the attacker account and sending a message to the victim account using Tumblr's web-based messaging feature, establishing the condition for the subsequent DoS trigger.

## Description

Tumblr's messaging system allows direct messages between users. After logging in, the attacker searches for the victim by username and sends a simple text message. This action creates a message thread in the victim's inbox. The message content is irrelevant; any message suffices to link the accounts. Upon sending, the message is stored server-side, and deletion of the sender later causes improper handling, breaking the recipient's interface. This step requires no advanced skills, just standard user interaction.

## Requirements

1. Active attacker and victim Tumblr accounts with messaging enabled
2. Web browser access to tumblr.com
3. Knowledge of the victim's username

## Defense

Defensive measures and detection strategies:

- Rate limit messaging from new accounts to prevent spam
- Scan for anomalous messaging patterns before account deletion
- Educate users on risks of receiving messages from untrusted sources

## Objectives

1. Deliver a message from attacker to victim to create a dependent thread
2. Confirm message receipt in victim's inbox
3. Set up the vulnerability trigger without alerting the platform

## Instructions

### Step 1: Log In to Attacker Account

**Context**: Gain access to the sending account.

Open tumblr.com/login in your browser, enter the attacker credentials, and log in.

> Dashboard loads successfully, confirming authenticated session.

### Step 2: Access Messaging Feature

**Context**: Navigate to the tool for sending direct messages.

Click the envelope icon or go to the messaging section in the sidebar.

> Messaging inbox opens, showing any existing threads (none expected).

### Step 3: Send Message to Victim

**Context**: Target the victim and transmit the message.

Search for the victim's username, select their profile, and compose a simple message (e.g., "Test message"). Click send.

> Message sends successfully; a confirmation or updated sent items list appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[messaging]]
- [[tumblr]]
- [[web]]
