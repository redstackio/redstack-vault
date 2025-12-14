---
id: p2b2c3d4-e5f6-7890-abcd-ef1234567890
name: Deliver-CSRF-PoC-to-Victim
tags:
  - csrf
  - phishing
  - social-engineering
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.042Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deliver-CSRF-PoC-to-Victim

## Summary

This procedure involves delivering the crafted CSRF proof-of-concept page to the victim through social engineering tactics, ensuring they load it while authenticated to VK.com to trigger the email binding change.

## Description

Delivery can occur via email links, malicious ads, or embedded iframes on compromised sites. The goal is to get the victim to visit the hosted PoC URL without suspicion. No direct interaction is needed beyond the visit, making it stealthy. Target is web users of VK.com.

## Requirements

1. Hosted PoC page accessible publicly
2. Victim's contact info (email, social media)
3. Social engineering pretext (e.g., fake VK update)

## Defense

Defensive measures and detection strategies:

- User training on link verification
- Browser extensions blocking auto-submits
- WAF rules detecting cross-origin POSTs to sensitive endpoints
- Email filtering for suspicious links

## Objectives

1. Induce victim to load the malicious page
2. Trigger CSRF request during authenticated session
3. Confirm email change post-delivery

## Instructions

### Step 1: Host PoC Publicly

**Context**: Make the HTML accessible via a URL the victim can reach.

Upload to a free hosting service or use ngrok for tunneling: `ngrok http 8000` to get a public URL like https://abc123.ngrok.io/csrf-poc.html.

### Step 2: Craft Delivery Message

**Context**: Create a convincing lure.

Send an email: "VK Security Update: Click here to verify your account - https://abc123.ngrok.io/csrf-poc.html"

### Step 3: Monitor and Verify

**Context**: Check if the attack succeeded.

After victim visits, log into VK.com with attacker's email or check account settings for changes.

**Expected Output**: Email bound successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
- [[social-engineering]]
