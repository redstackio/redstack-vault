---
id: proc-uuid-2
tags:
  - social-engineering
  - phishing
  - xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-13T23:55:37.806Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Incorporate-Malicious-Fetish-into-Victim-Profile

## Summary

This procedure involves social engineering to lure a victim into adding the attacker-created malicious fetish to their FetLife profile, thereby associating the stored XSS payload with the victim's account data for later triggering.

## Description

Once the malicious fetish is created, the attacker must entice victims to interact with it. This step relies on platform features where users browse and add fetishes to their profiles. The payload remains inert until added, then becomes part of the victim's editable data. Target environment is FetLife's user profile management. Outcomes include the payload integration, increasing the attack surface for execution.

## Requirements

1. Access to communication channels on or off FetLife (e.g., messages, forums)
2. Knowledge of victim's interests to craft convincing lures
3. Malicious fetish already created from prior procedure

## Defense

Defensive measures and detection strategies:

- User education on verifying fetish sources and avoiding unsolicited additions
- Rate limiting on fetish additions and profile edits to detect abuse
- Anomaly detection for unusual fetish creation/addition patterns

## Objectives

1. Convince victim to add the specific malicious fetish
2. Integrate payload into victim's profile without raising suspicion
3. Position for subsequent XSS trigger

## Instructions

### Step 1: Craft Lure Message

**Context**: Create a persuasive message or post to encourage fetish addition.

Draft a message like: "Check out this new fetish [link to malicious fetish] – perfect for your interests! Add it to your profile."

### Step 2: Deliver and Monitor

**Context**: Send the lure and wait for victim interaction.

Send via FetLife messaging or external channels; monitor profile or infer via platform notifications.

> Expected output: Victim adds the fetish, visible in their profile interests section.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
