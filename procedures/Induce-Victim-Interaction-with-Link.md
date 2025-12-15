---
tags:
  - phishing
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
id: 7df2e91f-455c-40bc-94fd-dd436401bd29
created_at: '2025-12-14T17:33:34.309Z'
updated_at: '2025-12-14T17:33:34.309Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Victim-Interaction-with-Link

## Summary

This procedure describes social engineering techniques to lure a victim into clicking a malicious CSRF link while authenticated to Rockstar Social Club, triggering the unauthorized account linking.

## Description

The attack relies on the victim being in an active session. The link is disguised as a game update, friend invite, or support notification. Delivery via email, Discord, or forums targets Rockstar users. Success depends on the victim's trust and session state; no technical exploits beyond the link itself.

## Requirements

1. Crafted malicious link from prior procedure
2. Victim's contact information or social presence
3. Plausible pretext related to gaming

## Defense

Defensive measures and detection strategies:

- Educate users on link verification
- Implement link scanning in email gateways
- Rate-limit linking requests per IP

## Objectives

1. Ensure victim clicks link during active session
2. Trigger cross-site request forgery
3. Confirm linking initiation

## Instructions

### Step 1: Prepare Delivery Message

**Context**: Create a convincing message embedding the link.

Example: "Hey, check out this new Rockstar beta invite: [malicious-link]"

> Use gaming lingo to build trust.

### Step 2: Distribute the Link

**Context**: Send via appropriate channel to reach the victim.

Email or message the pretext with the shortened or disguised URL.

> Expected: Victim receives and potentially clicks.

### Step 3: Monitor for Interaction

**Context**: Watch for signs of click, such as third-party account notifications.

Check the attacker's third-party dashboard for incoming link requests.

> Success if linking attempt appears.

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
- [[csrf]]
