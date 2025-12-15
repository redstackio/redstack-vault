---
id: proc-slack-csrf-link-send
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
updated_at: '2025-12-14T17:27:29.571Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Send-Malicious-CSRF-Link-to-Victim

## Summary

This procedure involves crafting and delivering a phishing link to a logged-in Slack user, leading them to a malicious page that exploits CSRF to add a secondary 2FA phone number.

## Description

In the context of Slack's CSRF vulnerability in the 2FA SMS endpoint, the attacker sends a link to slackcsrf.html hosted on their server. The victim, while logged in, clicks it, triggering automated form submissions that bypass CSRF protection due to missing 'crumb' token validation. This enables adding the attacker's phone without consent, setting up for 2FA bypass. Prerequisites include victim being logged in and attacker controlling a web server.

## Requirements

1. Hosted malicious HTML/JS file (slackcsrf.html)
2. Victim's contact method (email, chat) for link delivery
3. Victim actively logged into Slack web app

## Defense

Defensive measures and detection strategies:

- Enable strict CSRF token validation on all state-changing endpoints
- User training on suspicious links and verifying URLs before clicking
- Browser extensions like uBlock Origin to block malicious scripts
- Monitor for anomalous 2FA additions in account logs

## Objectives

1. Gain victim's interaction with malicious page while authenticated
2. Initiate CSRF chain for 2FA manipulation
3. Position for credential access via 2FA bypass

## Instructions

### Step 1: Craft the Malicious Link

**Context**: Create a URL pointing to your hosted slackcsrf.html, disguising it as a legitimate Slack notification or urgent message.

No command required; manually construct: http://attacker-domain.com/slackcsrf.html

> Ensure the page is served over HTTP/HTTPS accessible to victim.

### Step 2: Deliver the Link

**Context**: Send via phishing email or in-app message to entice click.

Example message: "Slack security update required: [link]"

> Success: Victim loads the page, triggering auto-forms.

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
