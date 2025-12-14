---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
name: Craft-and-Deliver-CSRF-Proof-of-Concept
tags:
  - csrf-poc
  - account-takeover
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:11.961Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Craft-and-Deliver-CSRF-Proof-of-Concept

## Summary

This procedure constructs a malicious HTML form that auto-submits a forged password change request, tricking an authenticated victim into resetting their password to attacker-controlled values.

## Description

Using captured parameters, an HTML page with a hidden form posts to https://████████.mil/scripts/wa.exe without CSRF tokens. When the victim visits the link while logged in, the form submits automatically, changing their password (p parameter) and associating a new email (q). This leads to full account takeover. Delivery via phishing email or malicious site.

## Requirements

1. Captured request parameters from prior interception
2. Web server to host the HTML PoC
3. Victim's authenticated session on the target site

## Defense

Defensive measures and detection strategies:

- Add unique CSRF tokens to all POST forms and validate on server
- Educate users on phishing and warn against clicking untrusted links
- Monitor for unexpected password changes and alert users

## Objectives

1. Forge and auto-submit the password reset request
2. Achieve unauthorized password modification
3. Gain persistent access to victim account

## Instructions

### Step 1: Create HTML Form

**Context**: Build the PoC page mimicking the legitimate request.

No specific command; write HTML with <form method="POST" action="https://████████.mil/scripts/wa.exe"> including hidden inputs for p, q, etc., and JavaScript to auto-submit on load.

> Example snippet: <input type="hidden" name="p" value="attackernewpass"> <input type="hidden" name="q" value="attacker@email.com">

### Step 2: Host and Test PoC

**Context**: Deploy the page and verify it submits correctly.

No specific command; host on a server (e.g., GitHub Pages) and test in an authenticated browser.

> Expected: Password changes upon page load without user interaction.

### Step 3: Deliver to Victim

**Context**: Send the link via email or other means to the target.

No specific command; include the PoC URL in a phishing message, e.g., "Click to update your profile."

> Success: Victim visits while authenticated, triggering takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf-poc
- account-takeover
- social-engineering
