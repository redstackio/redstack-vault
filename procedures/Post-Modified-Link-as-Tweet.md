---
id: proc-uuid-4
tags:
  - twitter
  - tweet
  - posting
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
updated_at: '2025-12-14T17:28:13.000Z'
skill_level: beginner
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Post-Modified-Link-as-Tweet

## Summary

Post the URL of the modified Player Card as a tweet to trigger rendering of the embedded iframe on Twitter, distributing the clickjacking payload.

## Description

Sharing the custom URL in a tweet causes Twitter to fetch and expand the Player Card, displaying the iframe. This spreads the attack via timelines or promotions. Prerequisites: Twitter account and hosted URL; outcomes: Live tweet with exploitable card, enabling wormable propagation if victims auto-tweet.

## Requirements

1. Active Twitter account
2. Hosted modified Player Card URL
3. No special permissions beyond posting

## Defense

Defensive measures and detection strategies:

- Scan tweets for suspicious Player Card domains
- Limit embedding in promoted content
- User alerts for expanded cards

## Objectives

1. Publish tweet with malicious card
2. Verify card rendering
3. Enable attack distribution

## Instructions

### Step 1: Compose and Post Tweet

**Context**: Create a tweet including the custom URL to invoke Player Card.

Log into Twitter, compose a new tweet, and paste the URL (e.g., https://whitelisted-domain.com/player). Post it.

> Ensure the tweet is public for visibility.

### Step 2: Verify Rendering

**Context**: Check if the card expands correctly in a test view.

Refresh the timeline or view the tweet; expand the card to confirm custom HTML loads.

> Expected: Iframe content visible without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[tweet]]
