---
id: proc-uuid-2
name: Intercept API Save Request with Burp Suite
tags:
  - ssrf
  - intercept
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:28.646Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept API Save Request with Burp Suite

## Summary

This procedure uses Burp Suite to capture the POST request to the /api/save/ endpoint during FAST form submission, isolating it in Repeater for payload modification. It enables precise editing of the JSON body to prepare for SSRF injection.

## Description

After form submission, the application sends a JSON payload to /api/save/ containing session data like 'globalInfo'. Burp Suite's Proxy history logs this; sending to Repeater allows replay and alteration without re-submitting the full form. This targets the insufficient sanitization in the PDF process.

## Requirements

1. Burp Suite running with browser traffic routed through it
2. Active FAST session with form partially submitted
3. Access to Proxy and Repeater tabs

## Defense

Defensive measures and detection strategies:

- Rate-limit API endpoints to detect repeated or modified requests
- Log and alert on JSON payload anomalies (e.g., script tags)
- Use request validation to reject intercepted/replayed requests

## Objectives

1. Capture the exact /api/save/ request structure
2. Isolate for safe modification and testing
3. Confirm request format for payload injection

## Instructions

### Step 1: Monitor Proxy History

**Context**: Observe requests during form interactions to spot the save endpoint.

In Burp Suite Proxy > HTTP history, filter for POST to /api/save/ after clicking CONTINUE or PRINT.

> Request appears with JSON body including 'globalInfo' object.

### Step 2: Send to Repeater

**Context**: Load the request into Repeater for editing without affecting the live session.

Right-click the /api/save/ entry in history and select 'Send to Repeater'.

> Tab opens with full request details, ready for body modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- intercept
- burp
