---
id: p3c4d5e6-g7h8-9012-cdef-345678901234
tags:
  - phishing
  - hosting
  - csrf
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:33:24.305Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Host-and-Deliver-CSFR-PoC

## Summary

This procedure deploys the CSRF HTML PoC on an attacker-controlled web server and distributes the URL to the target victim through phishing or social engineering.

## Description

The attacker uploads the generated HTML file to a server (e.g., VPS or free hosting) and crafts a phishing email or message with the link, luring the victim to visit while logged into the DoD application. This triggers the cross-site request using the victim's session.

## Requirements

1. Access to a web server for hosting
2. Victim's email or contact method for delivery
3. Basic phishing template

## Defense

Defensive measures and detection strategies:

- User training on phishing recognition
- Email filters for suspicious links
- Browser extensions blocking auto-submits

## Objectives

1. Make the PoC accessible via a public URL
2. Successfully deliver and have victim interact with the link
3. Ensure the page loads without triggering browser warnings

## Instructions

### Step 1: Deploy PoC to Server

**Context**: Host the HTML file publicly.

**Instructions**: Use a tool like Python's http.server or upload to a hosting service. Example: `python3 -m http.server 80` in the directory with csrf_poc.html.

> Expected output: Server running; access via http://attacker-ip/csrf_poc.html.

### Step 2: Send Link to Victim

**Context**: Trick the victim into visiting the page while authenticated.

**Instructions**: Craft an email like 'Click here to update your profile: [URL]'. Send via email or messaging.

> Expected output: Victim clicks and loads the page, submitting the form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.001]] Spearphishing Attachment (adapted for link)

## Commands Used

- None

## Tools Used

- None

## Tags

- phishing
- hosting
- csrf
