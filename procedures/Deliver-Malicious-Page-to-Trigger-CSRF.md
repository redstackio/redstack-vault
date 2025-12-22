---
id: proc-uuid-3
tags:
  - csrf
  - delivery
  - phishing
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:30.121Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Deliver Malicious Page to Trigger CSRF

## Summary

This procedure involves distributing the crafted malicious HTML to an authenticated victim, causing their browser to unknowingly submit the CSRF request and send an unauthorized private project invitation in Localize.

## Description

Delivery methods include phishing emails, malicious links on forums, or compromised sites. When the victim loads the page while logged into Localize, the auto-submitting form uses their session cookies to authenticate the request to http://www.localize.io/, bypassing any client-side checks due to the server's lack of token validation. This can lead to spam invitations or unintended access grants. Prerequisites are the ready HTML exploit and a social engineering vector to reach the victim.

## Requirements

1. Hosting for the HTML file (e.g., GitHub Pages, personal server)
2. Method to lure victim (email, social media)
3. Victim must be authenticated to Localize during page load

## Defense

Defensive measures and detection strategies:

- Deploy browser extensions or policies to warn on auto-submitting forms
- Log and alert on rapid or anomalous invitation requests
- Implement multi-factor approval for sensitive actions like invitations

## Objectives

1. Ensure victim loads the page in an authenticated state
2. Trigger the forged request without user awareness
3. Achieve unauthorized action via session hijacking

## Instructions

### Step 1: Host the Malicious HTML

**Context**: Make the exploit accessible via a URL.

Upload the HTML file to a web server or free hosting service, obtaining a public URL like http://attacker.com/exploit.html.

**Expected Output**: Accessible link to the page.

### Step 2: Lure and Trigger

**Context**: Send the link to the victim via phishing or other means.

Email or message: "Check this important update: [URL]". When clicked and loaded, the form submits automatically if the victim is logged into Localize.

Monitor network traffic or server logs to confirm the POST request.

**Expected Output**: Invitation sent from victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[delivery]]
- [[Phishing]]
- [[web]]
