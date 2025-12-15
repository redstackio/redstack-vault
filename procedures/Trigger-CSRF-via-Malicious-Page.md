---
id: p3q4r5s6-t7u8-9012-defg-hi3456789012
name: Trigger CSRF via Malicious Page
tags:
  - csrf
  - exploit
  - social-engineering
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.000Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger CSRF via Malicious Page

## Summary

This procedure delivers the CSRF PoC to the victim, tricking them into loading the malicious page while authenticated, which auto-submits the forged request to delete the pet without their awareness.

## Description

On myroyalcanin.hu, the attacker sends the PoC link via email, SMS, or embeds it in a phishing site. Upon visit, the victim's browser uses their session cookies to authenticate the delete request to /kisallataim/ANIMAL_ID/delete, resulting in data loss. This relies on social engineering for delivery.

## Requirements

1. Hosted PoC page accessible via URL
2. Method to lure victim (e.g., email client)
3. Victim's authentication to the target site

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Implement referrer checks and SameSite=Strict cookies
- Monitor account for sudden data deletions and notify users

## Objectives

1. Successfully deliver and execute the PoC on the victim
2. Achieve unauthorized pet deletion
3. Remain undetected during the process

## Instructions

### Step 1: Distribute the Malicious Link

**Context**: Use social engineering to get the victim to visit the page.

Send an email or message with a link to the hosted PoC, disguised as legitimate content (e.g., "Check this pet care tip").

**Expected Output**: Victim clicks and loads the page.

### Step 2: Verify Exploitation

**Context**: Confirm the deletion occurred post-visit.

Check the victim's account or simulate to ensure the pet is removed.

**Expected Output**: Pet profile gone from the account.

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
- [[exploit]]
- [[social-engineering]]
