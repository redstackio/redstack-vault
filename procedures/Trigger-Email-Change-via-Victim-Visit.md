---
id: trigger-email-change-victim
tags:
  - csrf
  - email-change
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
updated_at: '2025-12-14T17:33:06.534Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger Email Change via Victim Visit

## Summary

This procedure describes the victim's interaction with the malicious page, resulting in the background submission of the CSRF form to update their IRCCloud email address.

## Description

When the victim loads the attacker's page while logged into IRCCloud, their browser automatically submits the hidden form using active session cookies. The POST to /chat/user-settings updates the email without any visible prompt or confirmation, exploiting the lack of CSRF tokens. This step is passive from the attacker's perspective but critical for chaining to email hijack.

## Requirements

1. Victim authenticated in IRCCloud browser session
2. No ad-blockers or CSP blocking cross-site forms
3. Functional malicious page hosted

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all POST endpoints
- Log and alert on unexpected settings changes
- Require same-site origin for sensitive form submissions
- User training on unexpected page behaviors

## Objectives

1. Silently alter victim's email in IRCCloud account
2. Avoid detection through background execution
3. Enable attacker to receive subsequent confirmations

## Instructions

### Step 1: Victim Loads Malicious Page

**Context**: Browser fetches and executes the HTML, triggering form submission.

**Instructions**: Victim clicks link; page loads, JavaScript submits form with fields: email=hacker@example.com, etc.

**Expected Output**: IRCCloud backend updates email; no user notification.

### Step 2: Verify Update (Attacker Side)

**Context**: Confirm change occurred via later steps.

**Instructions**: Proceed to monitor email for confirmation.

**Expected Output**: Email change processed successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[email-change]]
