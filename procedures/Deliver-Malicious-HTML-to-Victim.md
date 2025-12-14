---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - delivery
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
updated_at: '2025-12-14T17:31:42.883Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-Malicious-HTML-to-Victim

## Summary

This procedure delivers the crafted CSRF HTML to the victim, triggering the account switch upon loading.

## Description

The attacker sends the HTML via phishing email, link, or attachment. When opened in the victim's browser (with Liberapay session active), the form submits, logging them into the attacker's account. The original session expires after a delay. This exploits the lack of CSRF validation, allowing silent takeover. Expected: Attacker gains access to victim's actions on their profile.

## Requirements

1. Crafted HTML POC from prior step
2. Delivery vector (email, messaging)
3. Victim's trust in attacker/source

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Browser same-origin policy enforcement; site-side CSRF tokens
- Monitor for session switches without direct logins

## Objectives

1. Induce victim to load HTML
2. Execute cross-site POST
3. Confirm account takeover

## Instructions

### Step 1: Prepare Delivery

**Context**: Host or package the HTML for sending.

Upload to a web server or attach to email with enticing subject (e.g., 'Liberapay Update').

> Ensure link points to HTML; avoid direct suspicion.

### Step 2: Send to Victim and Monitor

**Context**: Trigger the load and observe effects.

Send via preferred vector; wait for victim interaction.

> Victim loads: Form submits, URL changes to /about/; session switches. Attacker checks profile for new data.

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
- [[delivery]]
