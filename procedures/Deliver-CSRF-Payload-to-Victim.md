---
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
created_at: '2022-04-05'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:50.403Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8d9339a8-cc39-47ac-b8ec-d1cb154f8a22
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-CSRF-Payload-to-Victim

## Summary

This procedure covers the social engineering aspect of CSRF attacks, where the attacker lures an authenticated victim to load the malicious page, triggering the unauthorized email change on TikTok Ads.

## Description

Delivery relies on user interaction, often via phishing emails, malicious links in messages, or compromised sites. The victim's browser, if logged into TikTok Ads, will include session cookies in the cross-site request, bypassing CSRF protections. Success depends on the victim's authentication state and the payload's stealth.

## Requirements

1. Hosted malicious HTML page accessible via URL
2. Communication channel to victim (email, chat, etc.)
3. Social engineering pretext (e.g., fake ad update)

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Email filters for phishing
- Browser extensions blocking cross-site requests

## Objectives

1. Induce victim to visit the payload URL while authenticated
2. Confirm execution via account changes
3. Minimize detection through obfuscation

## Instructions

### Step 1: Prepare Delivery Mechanism

**Context**: Craft a convincing lure to direct the victim to the malicious page.

Create a phishing email: "Urgent: Update your TikTok Ads verification at [malicious-link]." Shorten the URL if needed to hide the domain.

**Expected Output**: Clickable link pointing to the hosted HTML.

### Step 2: Send and Monitor

**Context**: Distribute the lure and observe for success.

Send the email or message to the target. Monitor the TikTok account or use a tracking pixel in the HTML to confirm visit.

**Expected Output**: Victim loads page, request sent, email updated.

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
- [[csrf-delivery]]
