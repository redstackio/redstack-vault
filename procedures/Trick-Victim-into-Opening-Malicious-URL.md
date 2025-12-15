---
tags:
  - social-engineering
  - url-delivery
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:33:11.984Z'
sub_techniques: []
id: ac5db59d-017d-41e0-a405-5aac3a64b9ea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Trick-Victim-into-Opening-Malicious-URL

## Summary

This procedure delivers the token-embedded URL to the victim via social engineering, ensuring they open it while logged into their Badoo account to initiate the CSRF exploit in their session.

## Description

The attack relies on the victim navigating to the malicious URL in an authenticated Badoo session, which triggers the photo import process using the attacker's token. Common delivery methods include phishing links disguised as photo sharing or app updates. The victim's browser executes the request cross-origin, bypassing origin checks due to the vulnerability.

## Requirements

1. Victim's contact info (email, chat ID) for delivery
2. Separate browser session for victim simulation during testing
3. Crafted pretext (e.g., 'Check out these photos!')

## Defense

Defensive measures and detection strategies:

- Warn users against clicking unsolicited links in social apps
- Implement referrer checks and same-site cookies for sensitive actions
- Use email filters to block suspicious Badoo-related links

## Objectives

1. Get victim to load the URL in their authenticated session
2. Trigger the import dialog without alerting the user
3. Maintain stealth to proceed to hijack

## Instructions

### Step 1: Prepare Delivery Message

**Context**: Create a convincing lure.

Draft a message like 'Hey, import these FB photos to your Badoo: [shortened URL]' using a URL shortener if needed.

### Step 2: Send to Victim

**Context**: Deliver via preferred channel.

Send the message via email, SMS, or in-app chat, ensuring it prompts clicking.

### Step 3: Simulate Victim Session

**Context**: For testing, open in victim browser.

Log in as victim on m.badoo.com in a new browser, then paste and navigate to the URL.

### Step 4: Confirm Dialog Appearance

**Context**: Verify exploit initiation.

Ensure the Facebook import prompt loads, indicating the token is processed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[url-delivery]]
