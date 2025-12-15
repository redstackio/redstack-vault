---
id: proc-khan-trigger-6564
name: Trigger Redirection via User Interaction
tags:
  - open-redirect
  - user-execution
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:26.354Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger Redirection via User Interaction

## Summary

This procedure embeds the crafted SWF URL in a webpage or shares it, then relies on user interaction (e.g., clicking within the player) to trigger the unvalidated redirect to a malicious external site, enabling phishing or drive-by attacks.

## Description

After constructing the malicious URL, embed it using HTML <embed> or <object> tags in a phishing page, or share the direct link via email/social media disguised as legitimate Khan Academy content. The Flash player requires user click on the screen or link to activate the redirect specified in the 'link' parameter. Target: Browsers with Flash. Prerequisites: Crafted URL from prior procedure, victim access. Outcomes: Victim redirected to attacker-controlled site for credential harvest or malware.

## Requirements

1. Crafted SWF URL with malicious 'link' parameter
2. Method to deliver the link/page to victim (e.g., email)
3. Victim browser supporting Flash and JavaScript

## Defense

Defensive measures and detection strategies:

- Disable Flash globally and use modern alternatives
- Implement redirect validation and user warnings
- Log and alert on unexpected redirects from embedded content
- Educate users on verifying links in educational media

## Objectives

1. Induce victim interaction with the embedded player
2. Execute the redirect without blocks
3. Achieve access to malicious site for further exploitation

## Instructions

### Step 1: Embed the SWF in a Delivery Mechanism

**Context**: Integrate the constructed URL into a webpage or share it to reach the victim.

No command; create HTML:

Use `<embed src="http://smarthistory.khanacademy.org/assets/images/media/player.swf?displayclick=link&link=http://evil.com/phish&file=1.jpg" type="application/x-shockwave-flash" width="400" height="300">` in an HTML file. Host on your server or share the direct SWF URL.

> Disguise as educational content. Victim loads the page/player.

### Step 2: Induce and Confirm Redirection

**Context**: Wait for or prompt victim click, then verify redirect occurs.

No command; user action:

Instruct victim to "click the image for more info" or rely on natural interaction. Upon click, browser follows the 'link' parameter to external site.

> Expected: Seamless redirect to http://evil.com/phish. Success if no internal restrictions block it.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[user-execution]]
