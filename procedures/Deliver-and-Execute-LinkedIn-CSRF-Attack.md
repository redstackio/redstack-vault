---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - social-engineering
  - phishing
  - csrf-execution
  - linkedin
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:27:57.346Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Deliver-and-Execute-LinkedIn-CSRF-Attack

## Summary

This procedure involves distributing the crafted CSRF URL to the victim via social engineering and executing the attack when they click it while authenticated, forcing an unauthorized follow on their LinkedIn account.

## Description

Delivery occurs through channels like email or messaging, disguised as a profile recommendation. Upon clicking, the authenticated browser sends the GET request to the vulnerable endpoint, executing the follow action without confirmation due to absent CSRF protections. This enables attackers to add victims to malicious follower lists for spam or phishing. Prerequisites: crafted URL and victim contact; outcomes include immediate account manipulation and potential escalation to broader attacks.

## Requirements

1. Crafted malicious URL from prior step
2. Victim's contact method (email, DM, etc.)
3. Victim must be logged into LinkedIn in their browser

## Defense

Defensive measures and detection strategies:

- Enable CSRF protection on all endpoints
- User training on suspicious links
- Monitor follower additions for anomalies
- Browser extensions for CSRF blocking

## Objectives

1. Trick victim into executing the forged request
2. Achieve unauthorized account modification
3. Enable follow-on social engineering

## Instructions

### Step 1: Prepare Delivery Message

**Context**: Craft a convincing pretext to lure the victim.

Create an email or message like "Check out this recommended connection on LinkedIn: [malicious URL]".

> Ensure the link is shortened or disguised if needed to reduce suspicion.

### Step 2: Send and Monitor Execution

**Context**: Distribute the link and wait for interaction.

Send the message via email, social media, or other channels. When clicked, the browser performs the GET request automatically.

> Verify success by checking the attacker's profile for the new follower; no direct feedback to attacker during execution.

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
- [[csrf-execution]]
- [[linkedin]]
