---
id: proc-uuid-3
tags:
  - csrf
  - execution
  - account-deletion
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
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:27:42.831Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Deliver and Execute CSRF Attack

## Summary

This procedure involves distributing the malicious HTML PoC to an authenticated victim, resulting in the automatic submission of a forged request that closes their account without their knowledge.

## Description

The final exploitation step relies on social engineering to lure the victim to the attacker's hosted page while they remain logged into the target application. The browser's existing session cookies enable the forged POST to /services/user/closeAccount, bypassing authorization checks due to missing CSRF validation. Prerequisites: Hosted PoC and victim targeting; outcomes: Immediate account termination, leading to loss of access and potential data disruption.

## Requirements

1. Hosted malicious HTML from previous procedure
2. Method to deliver URL (e.g., email, link in chat)
3. Victim authenticated to target site
4. No additional tools beyond hosting

## Defense

Defensive measures and detection strategies:

- Require user confirmation for destructive actions like account closure
- Implement referrer checks and strict CSP headers
- Monitor for sudden account closures and notify users

## Objectives

1. Induce victim to load the malicious page
2. Trigger forged request using victim's session
3. Achieve account deletion

## Instructions

### Step 1: Host the PoC

**Context**: Make the HTML accessible via a public URL.

Upload the HTML to a web server or free hosting service, obtaining a URL like http://attacker.com/close.html.

### Step 2: Distribute to Victim

**Context**: Use social engineering to get victim to visit.

Send the URL via phishing email or message, e.g., "Click here to view urgent update: http://attacker.com/close.html". Ensure victim is logged in to target.

### Step 3: Verify Execution

**Context**: Confirm the attack succeeded.

Monitor target application logs or attempt victim login; expect account access denied.

**Expected Output**: Account closure confirmation in app logs or victim reports loss of access.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Account Access Removal]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Execution]]
- [[account-deletion]]
