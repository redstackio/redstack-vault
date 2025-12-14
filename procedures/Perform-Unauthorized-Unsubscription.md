---
tags:
  - idor
  - unsubscribe
  - exploitation
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
updated_at: '2025-12-14T17:25:30.037Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: da2433f1-602f-4ed8-b94b-7bee5a19f2c4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Unauthorized-Unsubscription

## Summary

This procedure exploits the IDOR to unsubscribe any subscribed user by submitting their email to the unprotected endpoint, optionally suppressing notifications for stealth.

## Description

The unsubscribe form at https://newsletter.nextcloud.com/?p=unsubscribe&id=1 accepts arbitrary emails without authentication, leading to immediate unsubscription. Appending &jo=1 to the request (as in email links) enables silent operation without sending a confirmation to the victim, allowing covert abuse. This directly impacts user privacy and trust in the newsletter service.

## Requirements

1. Target email address (subscribed or not; works on subscribed)
2. Access to the unsubscribe form
3. Optional: Proxy for request inspection

## Defense

Defensive measures and detection strategies:

- Require ownership verification (e.g., email token) for unsubscriptions
- Implement rate limiting on unsubscribe endpoints
- Audit for anomalous unsubscription patterns

## Objectives

1. Remove target from newsletter list
2. Achieve silent unsubscription if desired
3. Confirm exploitation success

## Instructions

### Step 1: Submit Target Email

**Context**: Use the form to target a specific email.

Enter the target email in the form at https://newsletter.nextcloud.com/?p=unsubscribe&id=1 and click 'Continue'.

> Expected output: Success message and optional confirmation email.

### Step 2: Enable Silent Mode (Optional)

**Context**: Suppress victim notification for stealth.

Append &jo=1 to the submission URL: https://newsletter.nextcloud.com/?p=unsubscribe&email=target@example.com&jo=1.

> Expected output: 200 OK without email sent to victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- unsubscribe
