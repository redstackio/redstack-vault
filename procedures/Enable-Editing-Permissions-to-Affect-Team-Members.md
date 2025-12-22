---
tags:
  - xss
  - propagation
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9da13d93-270c-4cd3-bde7-896421e1f09e
created_at: '2025-12-13T23:55:38.182Z'
updated_at: '2025-12-13T23:55:38.182Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Enable-Editing-Permissions-to-Affect-Team-Members

## Summary

This procedure configures post sharing with edit permissions to propagate the stored XSS to other team members, who execute the script upon editing and clicking.

## Description

By enabling 'Let others edit this Post', the malicious link persists. Victims editing the post click it in the domain context, leading to arbitrary JS execution affecting multiple users.

## Requirements

1. Ownership of the Slack post
2. Team collaboration access

## Defense

Defensive measures and detection strategies:

- Disable shared editing for sensitive posts
- Audit post permissions regularly
- Train on phishing via shared content

## Objectives

1. Amplify impact to team
2. Achieve execution without direct access
3. Collect data via executed scripts

## Instructions

### Step 1: Configure Permissions

**Context**: Set edit access in post settings.

In Slack, go to post options > Enable 'Let others edit this Post'.

> Expected: Permission updated; post shareable.

### Step 2: Share and Lure

**Context**: Distribute to victims.

Share the post link via channel or DM, encouraging edits.

> Expected: Victim edits, clicks link, triggers XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[propagation]]
