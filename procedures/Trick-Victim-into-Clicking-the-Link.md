---
tags:
  - phishing
  - social-engineering
  - csrf
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2024-10-01'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:27:57.880Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
id: 6f6f45bd-e257-43b6-bd17-6dc2b979a75b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Trick-Victim-into-Clicking-the-Link

## Summary

This procedure uses social engineering to lure a logged-in Periscope user into clicking the malicious HTML link from their Android browser, resulting in the app executing the unauthorized follow action without consent.

## Description

The victim must have the Periscope app installed and authenticated. The link, disguised in phishing content, triggers the deeplink handler upon click, bypassing any web-like confirmations. Impact is low as victims can unfollow easily, but it demonstrates app-specific CSRF risks. Expected outcome: Successful forced follow, verifiable in the app.

## Requirements

1. Hosted HTML page with deeplink
2. Communication channel to victim (email, social media)
3. Victim's device with Periscope app logged in

## Defense

Defensive measures and detection strategies:

- User training on recognizing phishing links that open apps
- App permissions to prompt before handling custom schemes
- Endpoint detection for anomalous app behaviors post-link click

## Objectives

1. Deliver the malicious link to the victim
2. Ensure click occurs from Android browser
3. Achieve unauthorized follow execution

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create enticing content to include the link.

Compose an email or message: "Check out this cool Periscope demo: [hosted-URL]"

> Personalize to increase click rate, targeting Periscope users.

### Step 2: Deliver and Monitor

**Context**: Send and observe the interaction.

Share via email/SMS/social, then check target's followers list.

> Upon click, app opens and follows without prompt. Verify by seeing new follow in app or web dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- phishing
- social-engineering
- csrf
- android
