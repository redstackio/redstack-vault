---
tags:
  - csrf
  - social-engineering
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.386Z'
sub_techniques: []
id: 9a0ff9e5-48f4-4e14-aadf-05fa0633b1a6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trick Victim into Submitting Forged CSRF Request

## Summary

This procedure simulates social engineering to lure an authenticated user to the malicious CSRF page, resulting in the execution of the forged signup request and unauthorized account creation.

## Description

The attacker deploys the malicious HTML on a controlled domain and entices the victim via email, link sharing, or ads to visit it while logged into Crashlytics. Upon visit, the page auto-submits the POST, exploiting the CSRF flaw. This relies on victim interaction but requires no further attacker action. Target: Authenticated web users. Prerequisites: Hosted payload from prior procedure. Outcomes: Confirmation of impact through signup verification.

## Requirements

1. Hosted malicious page accessible via public URL
2. Social engineering vector (e.g., email client or messaging app)
3. Victim authenticated to Crashlytics session

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and unexpected link risks
- Implement multi-factor confirmation for sensitive actions like signups
- Use web application firewalls to block suspicious cross-origin POSTs

## Objectives

1. Induce victim visit to trigger the CSRF payload
2. Achieve unauthorized beta signup with controlled data
3. Validate exploitation success without alerting the victim

## Instructions

### Step 1: Prepare Distribution

**Context**: Craft a lure to direct the victim to the malicious URL.

Create a phishing email or message: "Check out this beta invite: http://attacker.com/csrf-poc.html"

Embed the link to the hosted page.

> Ensure the page appears benign, e.g., redirect after submission to a fake success page.

### Step 2: Deliver and Monitor

**Context**: Send the lure and observe the victim's interaction.

Distribute the link to the target victim. Use server logs or a proxy to monitor requests to the malicious page.

No command needed; track via access logs.

> Expected: Victim visits, triggering POST to target endpoint.

### Step 3: Verify Exploitation

**Context**: Confirm the forged request resulted in signup.

Check Crashlytics backend (if accessible) or send a test email to the fake address to see confirmation.

Simulate with self as victim: Log in, visit page, inspect network for successful POST.

> Success: HTTP response indicates signup processed, e.g., 302 redirect or JSON success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
- [[web]]
