---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Deliver-CSRF-Attack-to-Authenticated-Victim
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.234Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deliver-CSRF-Attack-to-Authenticated-Victim

## Summary

This procedure details methods to deliver the CSRF payload to an authenticated user of ExpressionEngine 6.0.1, exploiting their session to perform unauthorized comment modifications.

## Description

Delivery relies on social engineering to get the victim to visit the attacker's malicious page while logged in. The vulnerability's use of GET requests makes it seamless, as browsers automatically send the request. This targets site moderators or users with edit privileges, amplifying impact through misinformation. Expected outcome: Silent execution with no alerts if defenses are absent.

## Requirements

1. Hosted malicious page from the crafting procedure
2. Contact method for the victim (email, chat, forum)
3. Timing to ensure victim is authenticated

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Use Content Security Policy (CSP) to block unauthorized form submissions
- Log and alert on rapid comment changes from the same IP

## Objectives

1. Induce victim to load the payload page
2. Leverage their session for the forged request
3. Confirm modification without attacker authentication

## Instructions

### Step 1: Select Delivery Vector

**Context**: Choose a method to lure the victim, such as email or a forum post, ensuring the link appears legitimate.

Craft a phishing email: "Check out this interesting article: [malicious-link]" where malicious-link points to your hosted payload.

### Step 2: Distribute the Link

**Context**: Send the link to the target, timing it when they are likely logged in (e.g., during active site use).

Use email or post in a related forum. For testing, self-target while authenticated.

### Step 3: Verify Execution

**Context**: Monitor the target site for the modification to confirm success.

Visit the comment section post-delivery; the content should reflect the injected text.

**Expected Output**: Updated comment visible on the site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[csrf-delivery]]
