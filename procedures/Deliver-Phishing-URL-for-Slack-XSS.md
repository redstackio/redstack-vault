---
tags:
  - phishing
  - social-engineering
  - url-delivery
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
id: e9beee68-271a-4cb9-9953-40088f2f9a31
created_at: '2025-12-13T23:52:49.400Z'
updated_at: '2025-12-13T23:52:49.400Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-Phishing-URL-for-Slack-XSS

## Summary

This procedure describes sending the crafted malicious URL to victims via phishing or social engineering, leveraging guessable Slack team names to target multiple workspaces and trigger the reflected XSS upon visit.

## Description

Delivery exploits human trust by presenting the URL as a benign Slack link (e.g., 'Check out this new emoji!'). When the victim visits, the payload reflects in the flash message on the custom emoji page, executing in browsers lacking XSS filters like Firefox or iOS Safari. Cross-team attacks are feasible since team names are easily enumerated or guessed.

## Requirements

1. Crafted malicious URL from prior procedure
2. Access to communication channels (email, chat apps)
3. List of potential victim teams or users

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition
- Use URL scanners in email gateways
- Monitor for anomalous Slack access patterns

## Objectives

1. Induce victim to click and visit the URL
2. Ensure reflection occurs without browser intervention
3. Enable payload execution for follow-on exploitation

## Instructions

### Step 1: Prepare Phishing Message

**Context**: Craft a convincing lure message to accompany the URL.

Example message: 'Hey, added a fun emoji to our Slack team - check it out: [malicious URL]'.

> Expected: Message appears legitimate to the recipient.

### Step 2: Select Delivery Vector

**Context**: Choose a method to send the URL, targeting users in specific or guessed teams.

Send via email, SMS, or external chat; for cross-team, enumerate teams via public sources (e.g., company websites).

> Expected: URL delivered without immediate suspicion.

### Step 3: Monitor for Access

**Context**: Track if the victim visits the URL, potentially via URL shortener logs or beacon in payload.

No command; observe indirect indicators like payload execution callbacks.

> Expected: Victim lands on `/customize/emoji` page, triggering reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
