---
tags:
  - phishing
  - ui-deception
  - credential-theft
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - iOS
  - WebView
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a71d2966-7ed8-422e-9aa4-be5cb2c5beea
created_at: '2025-12-14T17:24:44.875Z'
updated_at: '2025-12-14T17:24:44.875Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Deceive-User-with-Phishing-Content

## Summary

This final procedure loads malicious phishing content in the LINE iOS WebView while the spoofed address bar convinces the user of site legitimacy, enabling data theft.

## Description

Building on the vulnerability from HackerOne #1082991, after address bar spoofing, the WebView loads content from an attacker server via chained redirects. The mismatched timing hides the true origin, deceiving users into entering credentials or sensitive info. Scenario: User clicks spoofed link in LINE. Prerequisites: Prior steps completed. Outcomes: Phishing success with low detection.

## Requirements

1. Spoofed address bar active
2. Attacker-hosted phishing page (e.g., fake login)
3. User engagement with loaded content

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS-only with HSTS in WebViews
- Implement content security policies (CSP) to block unauthorized loads
- User training on domain verification and avoiding unsolicited links

## Objectives

1. Deliver phishing payload undetected
2. Harvest user inputs
3. Achieve initial access via deception

## Instructions

### Step 1: Chain Redirect to Malicious Server

**Context**: Use redirect in the URL to load attacker content post-spoof.

No command; embed in URL: `http://spoofed.com/redirect?to=phish.attacker.com`.

> WebView follows despite cancellation flags.

### Step 2: Render Phishing Interface

**Context**: Display fake forms matching the spoofed domain.

Host HTML/JS on server mimicking LINE UI.

> User sees "legitimate" page.

### Step 3: Capture User Interactions

**Context**: Log inputs like credentials sent to attacker endpoint.

Implement form submission to exfil server.

> Success: Data received without alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[phishing-delivery]]
- [[ui-spoofing]]
