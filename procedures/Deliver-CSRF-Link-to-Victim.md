---
tags:
  - phishing
  - delivery
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.152Z'
sub_techniques: []
id: c3dcf1e7-291d-4e5c-ac5a-a945e3bd1793
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deliver-CSRF-Link-to-Victim

## Summary

This procedure involves sending the malicious CSRF page link to the victim to trigger the account update when clicked while authenticated.

## Description

Social engineering is used to deliver the link, such as via email or message, disguised as a relevant action (e.g., "Update your profile"). The victim must be logged in for the CSRF to work. Target: Any communication channel with the victim. Outcome: Victim visits the page, submitting the forged request.

## Requirements

1. Contact method with victim (email, social media)
2. Crafted pretext for the link
3. Hosted CSRF page URL

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Email filters for phishing
- Browser warnings for auto-submits

## Objectives

1. Induce victim to load the malicious page
2. Leverage active session for CSRF
3. Initiate unauthorized update

## Instructions

### Step 1: Craft Delivery Message

**Context**: Create a convincing lure.

Compose message: "Please review this important account update: http://attacker-server.com/csrf.html"

> Ensure link appears legitimate.

### Step 2: Send the Link

**Context**: Transmit to victim.

Send via email or chat.

> Victim receives and potentially clicks.

### Step 3: Monitor Delivery

**Context**: Confirm access.

Check server logs for victim's IP or user-agent.

> Access logged indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[csrf]]
