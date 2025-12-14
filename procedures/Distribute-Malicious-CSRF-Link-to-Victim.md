---
id: proc-uuid-3
tags:
  - phishing
  - social-engineering
  - csrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:27:50.265Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Distribute Malicious CSRF Link to Victim

## Summary

This procedure covers delivering the CSRF PoC link to a target victim through social engineering or phishing, tricking them into loading the malicious HTML page that will forge the password reset request.

## Description

The attacker hosts the crafted HTML on a public or controllable domain (e.g., via free hosting services) and sends the URL to the victim via email, SMS, or social media, disguised as a relevant message like a Firefox account verification. When clicked, the victim's browser executes the CSRF without their knowledge. This requires social engineering skills and results in the victim unwittingly disclosing their details; no technical tools beyond hosting are needed beyond the PoC.

## Requirements

1. Hosted location for the HTML PoC (e.g., GitHub Pages, ngrok)
2. Victim contact method (email, messaging app)
3. Plausible pretext for the link (e.g., account security alert)

## Defense

Defensive measures and detection strategies:

- User training on suspicious links and verifying URLs
- Email filters for phishing detection
- Browser extensions blocking auto-submitting forms

## Objectives

1. Successfully deliver the link without raising suspicion
2. Ensure victim clicks and loads the page
3. Prepare for monitoring reset email arrival

## Instructions

### Step 1: Host the PoC Page

**Context**: Make the HTML accessible via a public URL.

Upload the HTML to a hosting service and obtain the direct link, e.g., https://attacker-domain.com/csrf-poc.html.

**Expected Output**: Page loads in browser and auto-submits when tested.

### Step 2: Craft Delivery Message

**Context**: Create a convincing phishing pretext.

Compose an email: "Your Firefox account needs verification. Click here: [link]" using the hosted URL, shortened if needed (e.g., via bit.ly).

**Expected Output**: Message ready for sending.

### Step 3: Send to Victim

**Context**: Deliver via chosen vector.

Send the email or message to the victim's address, timing it for high open rates (e.g., during work hours).

**Expected Output**: Delivery confirmation; await victim interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
- [[csrf]]
