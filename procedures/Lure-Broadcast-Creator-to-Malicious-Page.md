---
id: proc-lure-victim-001
tags:
  - phishing
  - social-engineering
  - lure
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
updated_at: '2025-12-14T17:27:35.489Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure-Broadcast-Creator-to-Malicious-Page

## Summary

This procedure uses social engineering techniques to trick the Steam broadcast creator into visiting the hosted malicious HTML page, triggering the CSRF exploit without their awareness.

## Description

Delivery relies on phishing or pretexting, such as sending a fake Steam update link or community invite. The victim must be authenticated in Steam for the POST to succeed as the issuer. Prerequisites: Hosted malicious page and victim contact info; outcomes: Victim visit leading to automatic payload execution.

## Requirements

1. Communication channel with victim (e.g., email, Discord, Steam chat)
2. Crafted pretext story related to Steam/broadcast
3. Hosted URL from previous procedure

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition and URL verification
- Implement email filters for suspicious Steam-related links
- Monitor login sessions for unexpected cross-site activity

## Objectives

1. Convince victim to click and visit the malicious URL
2. Ensure visit occurs while victim is authenticated in Steam
3. Minimize suspicion to avoid detection

## Instructions

### Step 1: Prepare the Lure Message

**Context**: Create a convincing pretext to direct the victim to the page.

Draft a message like: "Hey, check out this cool Steam broadcast tip: [malicious URL]" or impersonate a Steam support link.

### Step 2: Deliver the Lure

**Context**: Send the message via appropriate channel.

Use email, chat, or social media to send the link, timing it during the victim's active broadcast session.

> Track clicks via URL shorteners or server logs if possible.

**Expected Output**: Victim navigates to the URL, loading the page.

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
- [[lure]]
