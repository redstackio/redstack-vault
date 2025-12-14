---
tags:
  - phishing
  - social-engineering
  - csrf
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
updated_at: '2025-12-14T17:27:57.854Z'
sub_techniques: []
id: 80cf51b5-3b00-484b-9c9c-3be332fc385c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Distribute-Crafted-URL-to-Victim

## Summary

This procedure focuses on delivering the crafted malicious OAuth URL to the target victim through social engineering, prompting them to click and unwittingly authorize the linkage of their external account to the attacker's HackerOne.

## Description

The attacker sends the URL via phishing email, messaging, or other channels, disguising it as a legitimate HackerOne notification or integration request. When clicked, it exploits the CSRF vulnerability to start the OAuth flow tied to the attacker's authentication ID, leading to account linking without proper validation.

## Requirements

1. Crafted URL from previous interception
2. Victim's contact information (email, chat)
3. Social engineering skills to entice click

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Email filters for HackerOne domains
- Browser warnings for cross-site requests

## Objectives

1. Deliver URL without raising suspicion
2. Ensure victim interaction
3. Initiate forged OAuth flow

## Instructions

### Step 1: Prepare Delivery Method

**Context**: Choose a vector to send the link convincingly.

Craft a phishing message, e.g., "Click here to verify your HackerOne GitHub integration: [URL]".

### Step 2: Send the URL

**Context**: Transmit the link to the victim.

Use email or chat to send the crafted URL: https://hackerone.integration-authentication.com/oauth2/auth/<Auth ID>?csrf=<csrf>&scope=read:org%20repo&session=<session>.

### Step 3: Monitor for Interaction

**Context**: Wait for victim click and observe flow progression.

Check HackerOne dashboard for signs of initiation.

**Expected Output**: Victim clicks, triggering redirect or consent prompt.

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
- [[csrf]]
