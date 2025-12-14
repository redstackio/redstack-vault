---
id: p-enumerate-emails
tags:
  - email-enum
  - info-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.001]]'
updated_at: '2025-12-14T17:31:31.158Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.001]]'
---
# Enumerate-Admin-Emails-via-Password-Recovery

## Summary

This procedure abuses the Revive Adserver password recovery endpoint to enumerate valid admin email addresses by sending requests and observing success responses like 'Email Password Reset sent'.

## Description

The /admin/password-recovery.php endpoint lacks proper validation or rate limiting, leaking whether an email is registered. Attackers can guess common admin emails (e.g., admin@domain.com) to identify targets for token guessing, enabling account takeover.

## Requirements

1. Target URL for password-recovery.php
2. List of potential email guesses
3. HTTP client for POST requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on recovery endpoints
- Return generic error messages for all inputs
- Require CAPTCHA or secondary auth for recovery

## Objectives

1. Send POST requests with guessed emails
2. Identify valid accounts via response differences
3. Trigger recovery for targeted emails

## Instructions

### Step 1: Prepare Email List

**Context**: Generate common admin email patterns.

Create a wordlist: admin@target.com, root@target.com, etc.

### Step 2: Send Requests and Check Responses

**Context**: Probe for valid emails.

POST to /admin/password-recovery.php with email parameter: curl -X POST -d 'email=guess@target.com' https://target.com/admin/password-recovery.php

**Expected Output**: Success message for valid emails, error for invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.001]] Account Discovery: Local Account

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enumeration
- disclosure
