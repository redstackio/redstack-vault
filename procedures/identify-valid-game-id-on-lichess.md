---
id: proc-lichess-game-id-001
tags:
  - recon
  - lichess
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:48.394Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Valid Game ID on Lichess

## Summary

This procedure involves locating and extracting a valid game ID from the Lichess platform to serve as a foundation for exploiting the game export API in subsequent SSRF attacks.

## Description

Lichess is an open-source chess platform where games are publicly accessible. By browsing recent or public games, an attacker can obtain a game ID, which is a unique string used in API endpoints. This step requires no authentication and leverages the public nature of the site. The expected outcome is a usable game ID that allows requests to the export API without rejection.

## Requirements

1. Web browser or HTTP client to access lichess.org
2. Internet connectivity
3. Basic familiarity with URL structures

## Defense

Defensive measures and detection strategies:

- Monitor for unusual API request patterns to game export endpoints
- Rate-limit public game access to prevent automated ID harvesting

## Objectives

1. Acquire a valid game identifier for API exploitation
2. Ensure the ID is recent to avoid archival issues
3. Prepare for SSRF payload injection

## Instructions

### Step 1: Browse Lichess Games

**Context**: Navigate to the Lichess website and select a public or recent game to extract its ID from the URL.

No specific command required; manually visit https://lichess.org and click on a game, noting the ID in the URL (e.g., https://lichess.org/abc123def456).

> The game ID is the alphanumeric string in the URL path. Successful extraction yields a string like "abc123def456".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- lichess
