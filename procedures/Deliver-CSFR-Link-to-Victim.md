---
id: p-snapchat-deliver-link
tags:
  - csrf
  - snapchat
  - phishing
  - delivery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.589Z'
skill_level: low
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver CSRF Link to Victim

## Summary

This procedure involves sending the crafted CSRF link to a victim via common channels, tricking them into opening it and triggering the unauthorized lens installation in Snapchat.

## Description

Delivery relies on social engineering, embedding the link in messages or shares disguised as legitimate content. Once clicked, the lack of CSRF protection allows the forceful action, leading to unwanted lens persistence (e.g., 48 hours) and manual removal needs. This inflates lens popularity metrics maliciously.

## Requirements

1. Crafted URL or deeplink from prior steps
2. Communication channel (e.g., SMS, email, social media)
3. Victim with Snapchat installed

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- App-level warnings for auto-installs
- Rate limiting on unlock endpoints

## Objectives

1. Induce victim to open the link
2. Achieve unauthorized lens add
3. Observe persistence and removal

## Instructions

### Step 1: Embed Link in Message

**Context**: Disguise the exploit as a fun lens share.

**Instructions**: Create a message like "Check out this cool lens: [crafted URL]" and send via messaging app or email.

### Step 2: Monitor Impact

**Context**: Verify exploitation success.

**Instructions**: If possible, confirm via victim feedback or developer metrics that the lens was installed. The lens remains for ~48 hours, requiring manual deletion.

> Expected: Victim's account shows the lens; no consent given.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
