---
id: proc-csrf-deliver-2024
tags:
  - csrf
  - social-engineering
  - delivery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.407Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver CSRF Payload to Authenticated Victim

## Summary

This procedure covers luring an authenticated Zomato user to a malicious page, executing the CSRF attack to alter their username without detection or consent.

## Description

Delivery is the final stage of CSRF, relying on social engineering to direct victims to the payload while they remain logged in. The malicious HTML page, once loaded, forges the request using the victim's session cookies. This targets web users in a phishing-like scenario, leading to account disruption like handle squatting or confusion.

## Requirements

1. Hosted malicious HTML page (e.g., via free hosting)
2. Method to contact victim (email, link sharing)
3. Victim's authentication to Zomato active

## Defense

Defensive measures and detection strategies:

- Browser extensions blocking auto-submits (e.g., NoScript)
- User training on suspicious links
- Server-side rate limiting on username changes
- Session invalidation on suspicious activity

## Objectives

1. Ensure victim loads page while authenticated
2. Trigger seamless username modification
3. Verify impact without alerting victim

## Instructions

### Step 1: Host the Malicious Page

**Context**: Make the payload accessible via a URL.

Upload the HTML file to a hosting service ensuring HTTPS. Use tools like ngrok for local testing if needed.

**Expected Output**: Public URL (e.g., https://attacker-site.com/csrf.html).

### Step 2: Lure the Victim

**Context**: Send the link disguised as legitimate content.

Craft a phishing email or message: "Check this Zomato deal: [URL]". Ensure victim clicks while logged in.

**Expected Output**: Victim visits, form submits, username changes.

**Success Indicators**:
- Attacker observes or victim notifies of change
- Zomato profile shows new handle

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
- [[delivery]]
