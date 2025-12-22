---
id: proc-uuid-005
tags:
  - xss
  - injection
  - admin-abuse
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:33.879Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Confirm-Admin-Privileges-and-Inject-Stored-XSS

## Summary

This procedure verifies the newly gained admin privileges on the Uber ReadMe.io project and exploits the admin feature to inject arbitrary JavaScript into documentation pages, resulting in stored XSS on developer.uber.com.

## Description

With admin access, navigate to the project dashboard to confirm the role on the users page. ReadMe.io allows admins to embed custom JavaScript in docs by design, which renders on uber.readme.io and propagates to developer.uber.com. This enables stored XSS attacks that execute in the victim's browser context, potentially stealing session cookies or hijacking accounts.

## Requirements

1. Admin access from previous exploit
2. Access to Uber project dashboard
3. Knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Disable or sanitize JavaScript injection in documentation platforms.
- Implement Content Security Policy (CSP) on rendered pages.
- Audit admin actions and monitor for anomalous JS embeds.

## Objectives

1. Validate privilege escalation success.
2. Inject persistent XSS payload.
3. Achieve code execution on target domain.

## Instructions

### Step 1: Verify Admin Role

**Context**: Confirm access level in the dashboard.

1. Go to https://dash.readme.io.
2. Select Uber project.
3. Navigate to Users page and check role (should show Admin).
4. Take screenshot as evidence; optionally remove self to clean up.

> Role confirmation indicates successful escalation.

### Step 2: Inject JavaScript Payload

**Context**: Use admin edit privileges to embed malicious JS.

1. Go to a doc page, e.g., https://developer.uber.com/docs/rides/getting-started.
2. Edit the content and insert <script>alert(document.cookie)</script> or more advanced payload.
3. Save changes.

> Payload stores and executes on page load for all visitors to developer.uber.com/docs, enabling session hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[injection]]
