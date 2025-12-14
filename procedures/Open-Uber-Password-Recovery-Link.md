---
tags:
  - xss
  - web
  - uber
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
updated_at: '2025-12-14T03:15:47.277Z'
sub_techniques: []
id: 1fcdc9b5-e92d-4b82-a29f-85749be25a0f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open-Uber-Password-Recovery-Link

## Summary

This procedure opens the emailed recovery link to access the password set interface, positioning for payload injection in the self-XSS attack.

## Description

Upon receiving the email, click the unique recovery link which directs to a time-limited password set page. This step assumes email access and browser continuity. Target is Uber's recovery endpoint. Outcome: Secure form for new password input.

## Requirements

1. Received recovery email from Uber
2. Same browser session for consistency
3. Link validity (typically 1 hour)

## Defense

Defensive measures and detection strategies:

- Link expiration and one-time use
- IP checks on link access

## Objectives

1. Load the password reset form
2. Ensure session continuity
3. Prepare for payload entry

## Instructions

### Step 1: Access Link from Email

**Context**: Click the link to transition to the set password stage.

No command; email interaction:

```plaintext
Click: https://login.uber.com/reset-password?token=...
```

> Page loads with password fields. Check for errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[uber]]
