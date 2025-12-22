---
tags:
  - csrf
  - social-engineering
  - weblate
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
detection_risk: medium
sub_techniques: []
id: 0c2519fe-e005-4eb6-8bd5-d329b6711c11
created_at: '2025-12-14T17:27:15.390Z'
updated_at: '2025-12-14T17:27:15.390Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Share-Weblate-Activation-Link

## Summary

This procedure involves preparing the activation link from the attacker's registration and distributing it to the victim via social engineering to enable the CSRF exploit.

## Description

The activation link is a GET request to Weblate's activation endpoint, embedding user details like full name and email. Without CSRF tokens, clicking it while logged in applies these to the session's account. The attacker crafts a pretext (e.g., 'Activate your translation invite') and shares via email or messaging. Expected outcome: Victim clicks, unaware of modification.

## Requirements

1. Extracted activation link from registration email
2. Contact method for victim (email, chat)
3. Social engineering pretext

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links
- Implement link whitelisting or preview in emails
- Log and alert on activation requests from unexpected sources

## Objectives

1. Distribute link without self-activation
2. Trick victim into clicking while authenticated
3. Set up for account data overwrite

## Instructions

### Step 1: Prepare the Link

**Context**: Ensure the link contains attacker data and is not activated.

No command required; inspect the link URL to confirm it includes parameters like user ID and token. Optionally shorten or embed in HTML for phishing.

> Expected: Clean, shareable URL.

### Step 2: Distribute to Victim

**Context**: Use social engineering to send the link.

No command required; compose a message like 'Click here to activate your Weblate collaboration: [link]' and send via email or platform.

> Expected: Victim receives and is enticed to click.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
- [[weblate]]
