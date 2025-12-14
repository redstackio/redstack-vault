---
tags:
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:29:09.885Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c5253105-435d-4166-a912-46e9cde1b709
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure-Admin-to-Malicious-Page

## Summary

This procedure details social engineering techniques to direct a Nextcloud admin to the attacker's malicious CSRF page while their session is active, enabling the exploit.

## Description

Luring relies on deception to make the victim visit the page, where the CSRF payload executes. Common methods include phishing emails pretending to be legitimate updates or links in forums. The victim's browser must have an active Nextcloud session for authentication.

## Requirements

1. Contact information or communication channels for the admin
2. Crafted pretext for the lure (e.g., fake security alert)
3. Malicious page already hosted

## Defense

Defensive measures and detection strategies:

- Train users on phishing recognition
- Use email filters for suspicious links
- Log and alert on unusual external domain visits from admins

## Objectives

1. Convince the admin to click and load the page
2. Ensure timing aligns with active session
3. Minimize suspicion to avoid detection

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create a believable lure, such as an email claiming a Nextcloud update is available.

Example email body:

"Dear Admin, Please review this important Nextcloud recommendation: http://attacker.com/csrf-trigger.html"

> Send via email or messaging. Expected output: Admin receives and potentially clicks the link.

### Step 2: Monitor Engagement

**Context**: Track if the page is visited, perhaps via server logs or a tracking pixel.

Add a secondary img tag to log visits:

```html
<img src="http://attacker.com/log?ip=client" width="1" height="1" style="display:none;">
```

> Expected output: Log entry confirming visit.

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
