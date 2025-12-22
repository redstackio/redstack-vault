---
id: proc-uuid-002
tags:
  - xss
  - execution
  - trigger
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
updated_at: '2025-12-14T03:16:08.210Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-on-View

## Summary

This procedure triggers the execution of a stored XSS payload by accessing the affected page, causing the malicious JavaScript to run in the context of the viewer's browser session.

## Description

Once injected, the payload in the DoD application's stored content (e.g., a comment section) executes automatically when rendered in HTML. This relies on the application's output lacking proper encoding, affecting any user viewing the page. Prerequisites include successful injection; outcomes involve client-side script runtime, enabling further exploits.

## Requirements

1. Access to the page displaying stored content
2. Victim or test browser to observe execution
3. Payload already persisted from prior injection

## Defense

Defensive measures and detection strategies:

- Enforce output encoding on all dynamic content
- Deploy browser-based protections like XSS auditors
- Log and alert on unexpected script executions via client-side monitoring

## Objectives

1. Cause payload to load and execute in browser
2. Confirm cross-origin or same-origin execution
3. Prepare for impact exploitation

## Instructions

### Step 1: Access Affected Page

**Context**: Navigate to the resource containing the stored payload to trigger rendering.

Use a browser to visit https://███ and load the vulnerable content (e.g., a specific post or dashboard).

### Step 2: Observe Execution

**Context**: Monitor for script runtime upon page load.

Open dev tools (F12) and watch the console/network tab. The payload should execute, e.g., popping an alert or sending a beacon.

> Expected output: Console logs script activity; network requests to attacker endpoints if beaconed.

### Step 3: Simulate Victim View

**Context**: Test with a secondary account or incognito to mimic other users.

Log in as another user and view the page to ensure execution affects non-injector sessions.

> Expected output: Script runs in new session context, accessing victim-specific data like cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
