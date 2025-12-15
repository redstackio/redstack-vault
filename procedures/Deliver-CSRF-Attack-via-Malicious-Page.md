---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.807Z'
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
# Deliver-CSRF-Attack-via-Malicious-Page

## Summary

This procedure delivers the CSRF PoC by tricking the victim into visiting and interacting with a malicious HTML page, triggering the email change request while they are authenticated to IRCCloud.

## Description

Delivery relies on social engineering, such as phishing emails or malicious links, to get the victim to load the HTML page in a browser session where IRCCloud is active. The page submits a POST to the user-settings endpoint without a CSRF token, resulting in an unauthorized email update. This targets users who are logged in, exploiting the lack of origin validation. Expected outcome is the victim's email changed to the attacker's control.

## Requirements

1. Hosted malicious HTML (e.g., on attacker server)
2. Method to lure victim (email, link, etc.)
3. Victim authenticated to IRCCloud

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Monitor for CSRF-like requests from external domains
- Implement referrer policy checks

## Objectives

1. Induce victim interaction with malicious page
2. Execute forged request for email change
3. Confirm change via response

## Instructions

### Step 1: Host and Lure Victim

**Context**: Make the PoC accessible and send to victim.

Host 'a.html' on a web server and send a link via email or chat, e.g., "Click here to update your settings: http://attacker.com/a.html".

> Victim clicks and loads the page. Expected output: Page prompts or auto-submits form.

### Step 2: Trigger Submission

**Context**: Ensure victim interacts to send the request.

Victim fills email (pre-filled) and clicks 'update settings'.

> Browser sends POST; inspect network for {"_reqid":0,"success":true}. Expected output: Email changed silently.

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
