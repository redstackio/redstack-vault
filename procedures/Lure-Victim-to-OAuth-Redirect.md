---
id: proc-lure-victim-redirect
tags:
  - phishing
  - csrf
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.725Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure Victim to Malicious OAuth Redirect URL

## Summary

This procedure crafts a phishing link using the captured OAuth parameters and deceives the victim into visiting it, triggering the server to process the attacker's tokens in the victim's browser context.

## Description

The attacker embeds the state and code into a URL pointing to ThisData's OAuth callback endpoint. This link is sent to the victim, who, upon clicking, submits the parameters via GET request. Due to missing validation, the server treats it as a legitimate callback. This is a classic Login CSRF vector in OAuth flows. Expected outcome is the victim initiating the unauthorized login without suspicion.

## Requirements

1. Captured state and code from prior steps
2. Method to deliver link (email, messaging app)
3. Victim interaction with the target domain

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to OAuth endpoints
- Educate users on suspicious links
- Rate-limit OAuth callbacks per IP/session

## Objectives

1. Deceive victim into GET request with attacker parameters
2. Exploit drive-by nature for automatic processing
3. Bridge to authentication hijack

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the lure link with parameters.

Format the URL as `https://thisdata.com/oauth/redirect?state={captured_state}&code={captured_code}`. Ensure it mimics a legitimate ThisData link.

### Step 2: Deliver to Victim

**Context**: Use social engineering to prompt visit.

Send the URL via phishing email or chat, e.g., "Click here to verify your ThisData account: [malicious URL]". Victim clicks and browser navigates to the endpoint.

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
- [[csrf]]
- [[social-engineering]]
