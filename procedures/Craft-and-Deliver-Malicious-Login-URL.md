---
id: bdb34acf-9940-4325-a629-6f02d32752c1
name: Craft-and-Deliver-Malicious-Login-URL
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.344Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - phishing
  - url-crafting
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Craft-and-Deliver-Malicious-Login-URL

## Summary

This procedure constructs a phishing URL embedding the preserved oauth_token and delivers it to the victim to initiate the unauthorized login.

## Description

Using the token, the attacker crafts a Gratipay login URL that, when accessed by the victim, completes the OAuth flow without validation. Delivery can occur via social engineering tactics.

## Requirements

1. Preserved oauth_token
2. Victim contact method (email, messaging)
3. Gratipay base URL knowledge

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links
- Implement URL scanning in email gateways
- Validate all OAuth callbacks for origin

## Objectives

1. Embed token in a clickable URL
2. Deceive victim into access
3. Trigger OAuth completion on victim's browser

## Instructions

### Step 1: Construct URL

**Context**: Build the malicious endpoint.

Format as https://gratipay.com/auth/login/bitbucket:bitbucket.com/?oauth_token={preserved_token}.

> Replace {preserved_token} with the actual value.

### Step 2: Deliver to Victim

**Context**: Send via phishing.

Embed in an email or message, e.g., "Click here to login to Gratipay: [URL]".

> Expected output: Victim clicks and browser loads the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[Phishing]]
- [[url-crafting]]
