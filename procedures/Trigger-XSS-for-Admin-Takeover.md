---
id: 123e4567-e89b-12d3-a456-426614174003
name: Trigger-XSS-for-Admin-Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.426Z'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - account-takeover
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-XSS-for-Admin-Takeover

## Summary

This procedure logs in as an admin, edits the injected channel's title to force validation, and triggers the stored XSS payload via an unescaped error message in the toastr library, leading to arbitrary JavaScript execution and admin session theft.

## Description

Switch to the admin account, access the malicious channel settings, modify the title (e.g., 'me' to 'you'), and save. This invokes the rooms.saveRoomSettings endpoint, which calls getValidRoomName and reflects the invalid name in an error via handleError without HTML escaping, executing the payload in the admin's browser for potential keylogging, cookie theft, or further actions.

## Requirements

1. Admin credentials
2. Access to the channel with stored payload
3. Browser session as admin

## Defense

Defensive measures and detection strategies:

- Enable escapeHtml in toastr for all error messages
- Sanitize room names and error reflections server-side
- Monitor for XSS payloads in room metadata and logs

## Objectives

1. Execute JS in admin context
2. Steal admin session for privilege escalation
3. Enable further server access

## Instructions

### Step 1: Log Out and Log In as Admin

**Context**: Switch to the target admin session.

**Command** (No CLI; use UI):
Log out of attacker account and log in with admin credentials.

> Expected output: Admin dashboard loads.

### Step 2: Access Channel Settings

**Context**: Navigate to the injected channel.

**Command** (No CLI; use UI):
Join the channel and open settings.

> Expected output: Channel info visible with malicious name.

### Step 3: Edit Title

**Context**: Modify to trigger validation.

**Command** (No CLI; use UI):
Change title from payload-containing name (e.g., edit 'me' to 'you').

> Expected output: Edit mode active.

### Step 4: Save to Trigger XSS

**Context**: Invoke endpoint for reflection.

**Command** (No CLI; use UI):
Click the save button.

> Expected output: Error toast with unescaped payload executes alert(document.origin) or similar JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[account-takeover]]
