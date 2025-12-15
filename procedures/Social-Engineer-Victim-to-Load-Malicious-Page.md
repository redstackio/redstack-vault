---
tags:
  - phishing
  - social-engineering
  - web
type: procedure
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
updated_at: '2025-12-14T17:27:15.405Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 051fd6cb-998a-4447-8fd6-e84417699b23
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Social Engineer Victim to Load Malicious Page

## Summary

This procedure involves tricking an authenticated user into visiting a malicious webpage, which then executes the CSRF payload to delete their private messages.

## Description

The attacker distributes the exploit URL via phishing or social lures tailored to the Informatica community context (e.g., "New forum update link"). When the victim, logged in, loads it, the page triggers deletions using their session. Impact: Messages to Trash, auto-deleted daily. Prerequisites: Malicious page ready, victim contact method. Expected outcome: Unintended deletions.

## Requirements

1. Malicious webpage URL
2. Communication channel to victim (email, DM, forum)
3. Knowledge of victim's interest in Informatica
4. Plausible pretext for the link

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Email filters for phishing
- Browser warnings for cross-site requests
- Session timeouts and multi-factor for sensitive actions

## Objectives

1. Deliver the exploit URL convincingly
2. Ensure victim is logged in during visit
3. Confirm deletion via follow-up

## Instructions

### Step 1: Craft Lure Message

**Context**: Create a phishing pretext.

E.g., "Hey, check this Informatica community tip: [exploit URL]".

**Expected Output**: Convincing message.

### Step 2: Distribute to Victim

**Context**: Send via email or forum reply.

Target users active in private messaging.

**Expected Output**: Victim clicks link.

### Step 3: Verify Impact

**Context**: Monitor or ask victim about messages.

If possible, note if they complain of lost messages.

**Expected Output**: Confirmation of deletions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
- [[web]]
