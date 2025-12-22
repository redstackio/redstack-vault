---
id: proc-uuid-003
tags:
  - xss-trigger
  - execution
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.596Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# View and Trigger XSS in Imbox

## Summary

This procedure logs into the receiver account and views the forwarded email to execute the stored XSS payload in the browser, observing any CSP blocks or successful bypasses.

## Description

Upon rendering the email in hey.com's Imbox, the injected SVG CDATA payload executes JavaScript in the viewer's context, potentially alerting or loading external resources. CSP may block direct scripts, but onerror and style imports can partially succeed. Use DevTools to debug. Outcome: JS execution confirming vuln.

## Requirements

1. Receiver account with forwarded email
2. Chrome browser with DevTools enabled
3. No strict CSP bypass needed for initial test

## Defense

Defensive measures and detection strategies:

- Enforce CSP with 'unsafe-inline' restrictions
- Sanitize email rendering separately from web content
- Monitor browser console logs for injection attempts

## Objectives

1. Trigger stored XSS execution
2. Validate payload viability
3. Identify CSP limitations

## Instructions

### Step 1: Login and Navigate

**Context**: Access the receiver's Imbox.

Log in to receiver account and go to Imbox.

### Step 2: Open Email

**Context**: Render the payload.

Click the forwarded email. Open DevTools console to monitor.

**Expected Output**: Alert or console error from onerror; potential CSP violation logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-DevTools]]

## Tags

- xss-trigger
- execution
