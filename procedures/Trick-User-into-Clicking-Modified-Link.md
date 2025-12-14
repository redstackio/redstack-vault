---
tags:
  - phishing
  - spearphishing-link
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:33:12.483Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 5d7b058e-fc3e-4f47-b9f4-1b8efdd73e04
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Trick-User-into-Clicking-Modified-Link

## Summary

This procedure involves social engineering to deliver the modified reset link to the victim, prompting them to click it and trigger the malicious redirect.

## Description

Using phishing techniques, the attacker sends the tampered link disguised as an official Mars communication. When clicked, the open redirect exposes the token. This targets user trust in password reset emails and requires crafting convincing messages. Outcome is victim interaction leading to token exposure.

## Requirements

1. Modified reset link
2. Communication channel to victim (email, messaging app)
3. Social engineering skills to mimic legitimate notifications

## Defense

Defensive measures and detection strategies:

- Educate users on verifying reset links (e.g., type URL manually)
- Implement link shortening detection or URL scanners in email clients
- Monitor for phishing campaigns targeting reset flows

## Objectives

1. Induce victim to click the link
2. Ensure the phishing vector evades basic filters
3. Observe redirect initiation

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create a believable pretext for the link.

Compose an email or message: "Your Mars password reset has been requested. Click here to proceed: [modified link]. If not you, ignore this."

> Use spoofed sender if possible to appear from Mars support.

### Step 2: Deliver and Monitor

**Context**: Send the message and wait for interaction.

Send via email/SMS. Monitor attacker server for incoming requests from the redirect.

> Success if traffic hits the controlled domain shortly after delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[spearphishing-link]]
