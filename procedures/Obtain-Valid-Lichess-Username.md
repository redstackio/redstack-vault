---
id: proc-lichess-username-obtain
tags:
  - recon
  - username
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:31:52.597Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Obtain-Valid-Lichess-Username

## Summary

This procedure gathers publicly available usernames from Lichess to target for authentication abuse, enabling subsequent denial-of-service attacks without requiring privileged access.

## Description

Lichess exposes user information through public features like leaderboards and player directories. Attackers can enumerate valid usernames to exploit throttling vulnerabilities. This step is reconnaissance-focused and leverages the platform's open nature, with no rate limits on public queries. Expected outcome: A list of targetable usernames for lockout attempts.

## Requirements

1. Internet access to lichess.org
2. Web browser or HTTP client
3. No credentials or special tools needed

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on public search features to deter automated enumeration
- Monitor for unusual query patterns on user directories
- Limit public exposure of usernames where possible

## Objectives

1. Identify valid usernames for targeting
2. Build a list for potential DoS attacks
3. Confirm public accessibility without authentication

## Instructions

### Step 1: Browse Public User Features

**Context**: Access Lichess public pages to discover usernames.

Visit the player directory at https://lichess.org/player or leaderboard at https://lichess.org/rating. Scroll or search for users and note usernames like "exampleuser".

> This manual browsing yields dozens of usernames quickly. Expected output: Screenshots or notes of valid usernames.

### Step 2: Verify Username Validity

**Context**: Confirm the username exists by accessing its profile.

Navigate to https://lichess.org/@/username (replace with noted username). If the profile loads, it's valid.

> Successful verification shows user stats and games. No login required.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
