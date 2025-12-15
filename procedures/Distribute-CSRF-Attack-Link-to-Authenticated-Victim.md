---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csrf
  - social-engineering
  - phishing
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
updated_at: '2025-12-14T17:27:23.189Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Distribute-CSRF-Attack-Link-to-Authenticated-Victim

## Summary

This procedure covers sending the malicious CSRF HTML page link to a victim who is currently authenticated on the target WordPress site, leveraging social engineering to ensure they click it while logged in.

## Description

The attack relies on the victim being in an authenticated state, so the forged request uses their session cookies. Delivery methods include email, chat, or social media lures like "Check this urgent update on the blog." The page loads in the victim's browser, submitting the form transparently. Expected outcome: Unauthorized comment posted under the victim's account.

## Requirements

1. Hosting for the HTML page (e.g., GitHub Pages, personal server)
2. Victim's contact info (email, social handle)
3. Confirmation that victim has admin/editor access to post comments

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Implement referrer checks or same-site cookies
- Log and alert on anomalous comment submissions from external referrers

## Objectives

1. Induce victim to load the malicious page while authenticated
2. Ensure session hijacking via CSRF without direct credential theft
3. Maximize reach for spam campaigns

## Instructions

### Step 1: Host the Malicious Page

**Context**: Make the HTML accessible via a URL to send to the victim.

Upload csrf.html to a web server or use a free hosting service, obtaining a URL like https://attacker.com/csrf.html.

> Expected output: Page accessible and loads without errors.

### Step 2: Craft and Send the Lure

**Context**: Use social engineering to trick the victim into clicking.

Send an email or message: "Hey, saw this on the site - click here: https://attacker.com/csrf.html" Ensure timing when victim is likely logged in.

> Expected output: Victim receives and clicks the link, loading the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
- [[social-engineering]]
