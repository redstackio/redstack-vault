---
tags:
  - phishing
  - social-engineering
  - drive-by
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:29.249Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1aedb884-14de-449c-93a7-d6e0ad136748
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-Victim-into-Visiting-Crafted-URL

## Summary

This procedure uses social engineering to lure the victim into clicking the malicious OAuth completion URL, initiating the CSRF exploit in their browser.

## Description

The attacker distributes the crafted URL through phishing or drive-by methods, exploiting user trust to bypass consent. Once clicked, the victim's browser handles the GET request, completing the OAuth without their knowledge.

## Requirements

1. Crafted URL from previous procedure
2. Communication channel to victim (email, chat, social media)
3. Basic phishing knowledge

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Email filters for Factlink-related phishing
- Browser extensions blocking unverified redirects

## Objectives

1. Convince victim to access the URL
2. Ensure click occurs in victim's browser session
3. Trigger automatic OAuth completion

## Instructions

### Step 1: Prepare Phishing Message

**Context**: Craft a convincing pretext for the link.

**Instructions**: Create an email or message like "Click here to verify your Factlink Twitter connection: [shortened URL]".

> Tailor to victim's context for higher success.

### Step 2: Distribute the URL

**Context**: Send to target victim.

**Instructions**: Email, DM, or post the link where the victim will see it. Monitor for clicks if possible.

> Expected: Victim receives and interacts with message.

### Step 3: Confirm Interaction

**Context**: Verify the exploit triggers.

**Instructions**: If access to victim device, check Factlink session; otherwise, infer from subsequent actions.

> Success: Victim visits URL, flow completes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- social-engineering
