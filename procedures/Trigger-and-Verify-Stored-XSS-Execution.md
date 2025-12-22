---
id: proc-uuid-4
tags:
  - xss
  - execution
  - verification
  - slack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:47.430Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger and Verify Stored XSS Execution

## Summary

This procedure triggers the stored XSS by refreshing or switching contexts and verifies execution through source inspection confirming arbitrary JS capability.

## Description

After injection payloads execute on re-render due to lack of sanitization. Refreshing Slack or switching teams forces content reload leading to onload firing. Inspect /files source to see payload in script tags. Requires prior injections. Outcome: JS execution like domain prompt and evidence of storage for victim impact assessment.

## Requirements

1. Previously injected payloads in Slack
2. Browser developer tools for inspection
3. Access to multiple teams or willingness to refresh

## Defense

Defensive measures and detection strategies:

- Add nonce-based CSP to prevent onload execution
- Rate-limit refreshes and monitor for repeated team switches
- Audit /files source for unsanitized content periodically

## Objectives

1. Trigger payload execution via page interactions
2. Observe JS alert for confirmation
3. Inspect source to validate storage

## Instructions

### Step 1: Refresh or Switch Teams

**Context**: Force re-rendering to activate onload handlers; may require multiple attempts due to trial-and-error.

Manually refresh the page (F5) or switch teams via sidebar.

> Repeat if needed; payload executes sometimes inconsistently.

### Step 2: Inspect /files Source

**Context**: Navigate to yourdomain.slack.com/files and view page source.

Use browser dev tools (Ctrl+U or right-click > View Page Source).

> Look for payload inside <script> tags confirming reflection and storage.

Expected output: SVG onload visible unsanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
