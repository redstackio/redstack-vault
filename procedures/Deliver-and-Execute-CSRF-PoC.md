---
id: proc-deliver-csrf-poc
tags:
  - csrf
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
  - '[[User Execution]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:27:57.522Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[User Execution]]'
  - '[[Phishing]]'
---
# Deliver and Execute CSRF POC

## Summary

This procedure covers delivering the crafted HTML POC to a victim and ensuring execution while they are authenticated to NordVPN, resulting in unauthorized password change and account takeover.

## Description

Delivery can occur via email attachment, malicious website link, or shared file. The victim opens the HTML in their browser, triggering the form submission if logged into NordVPN. This exploits the session cookie, forging the request server-side as legitimate, leading to password reset without alerts.

## Requirements

1. Crafted HTML POC from previous procedure
2. Social engineering access to victim (e.g., email)
3. Victim's active NordVPN session

## Defense

Defensive measures and detection strategies:

- Browser extensions blocking auto-submits or suspicious forms
- Server-side rate limiting on password changes
- User training on opening unknown files

## Objectives

1. Successfully deliver the POC to the victim
2. Ensure execution during authentication
3. Confirm account takeover

## Instructions

### Step 1: Prepare Delivery Method

**Context**: Choose and set up a delivery vector like email with HTML attachment.

Attach the HTML file disguised as a harmless document.

**Expected Output**: Victim receives and opens the file.

### Step 2: Instruct or Trick Victim Execution

**Context**: Ensure the victim is logged into NordVPN before opening.

Phish with a message like "Click to update your settings" while authenticated.

**Expected Output**: Form submits, changing password.

### Step 3: Verify Takeover

**Context**: Test login with the new password set by the attacker.

Attempt to access the account post-execution.

**Expected Output**: Successful login, confirming compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[User Execution]]
- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[account-takeover]]
