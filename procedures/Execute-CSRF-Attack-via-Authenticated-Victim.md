---
tags:
  - csrf
  - exploitation
  - victim-trickery
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.567Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: afac5def-17b4-4e5d-9a5b-2f78891e6f09
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute-CSRF-Attack-via-Authenticated-Victim

## Summary

This procedure demonstrates delivering and executing the malicious HTML form to an authenticated user, resulting in unauthorized raffle ticket purchases and account balance drain.

## Description

By having the victim load the crafted HTML page while logged into Unikrn, their browser sends the forged POST request using session cookies. The endpoint processes it without CSRF checks, leading to unintended transactions. This exploits trust in cross-site requests in web applications.

## Requirements

1. Hosted malicious HTML from prior procedure
2. Delivery vector (e.g., email, malicious site link, iframe embed)
3. Authenticated victim account on target platform

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication (MFA) for transaction confirmation
- Log and alert on rapid or anomalous raffle entries
- Browser extensions or policies to block auto-submitting forms
- Rate limiting on API endpoints for ticket purchases

## Objectives

1. Force unauthorized action via victim's session
2. Achieve financial impact without direct access
3. Validate full exploit chain success

## Instructions

### Step 1: Prepare Delivery

**Context**: Host the HTML securely and obtain a public URL for delivery.

Upload the file to a web server (e.g., GitHub Pages, ngrok for local). Note the URL, e.g., https://attacker.com/csrf-poc.html.

> Ensure the page loads quickly to avoid suspicion.

### Step 2: Trick Victim into Loading

**Context**: Use social engineering to get the victim to visit the URL while authenticated.

Send a phishing email: "Check this raffle update: [URL]". Or embed in an iframe on a controlled site.

> When victim clicks and loads, form auto-submits the POST.

### Step 3: Verify Exploitation

**Context**: Monitor or check victim's account post-load.

Instruct victim (or simulate) to log in, load page, then refresh Unikrn account. Look for new raffle entry and balance change.

> Expected output: Ticket purchased; balance deducted by ticket cost.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-execution]]
- [[phishing-delivery]]
- [[session-hijack]]
