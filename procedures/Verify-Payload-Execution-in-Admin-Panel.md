---
id: proc-verify-xss-admin
tags:
  - xss
  - admin
  - concrete-cms
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.579Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Payload Execution in Admin Panel

## Summary

This procedure logs in as an admin and navigates to the Conversations Messages screen to confirm the Stored XSS executes in the backend admin context, highlighting privilege escalation risks.

## Description

Admins reviewing messages render the same unsanitized HTML, allowing JS execution with admin privileges. This extends the attack from frontend to backend in Concrete CMS, potentially enabling further compromise.

## Requirements

1. Admin credentials
2. Malicious comment stored
3. Access to admin dashboard

## Defense

Defensive measures and detection strategies:

- Sanitize admin views separately
- Use role-based rendering restrictions
- Monitor admin session for JS anomalies

## Objectives

1. Demonstrate backend execution
2. Highlight admin impact
3. Validate cross-context persistence

## Instructions

### Step 1: Admin Login

**Context**: Access the admin interface.

No command; UI:

- Log in to Dashboard
- Navigate to Conversations > Messages

> Expected: List of messages loads, including malicious comment.

### Step 2: Trigger Execution

**Context**: View the comment to render payload.

Open console (F12):

- Scroll or select the malicious message

> Expected: Script executes, log appears in admin context console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- [[xss]]
- [[admin]]
