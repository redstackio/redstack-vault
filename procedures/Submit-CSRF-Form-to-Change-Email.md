---
id: proc-uuid-5
tags:
  - csrf
  - account-takeover
type: procedure
tools:
  - '[[tools/Safari-Browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.661Z'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-CSRF-Form-to-Change-Email

## Summary

This procedure triggers the form submission to execute the CSRF attack, changing the victim's email to the attacker's controlled address.

## Description

With the form appended, clicking submit sends a POST with the malicious payload. The Referer from the special subdomain fools the server's regex, allowing the action without tokens.

## Requirements

1. Injected form visible on page
2. Authenticated session in another tab
3. Network access to target

## Defense

Defensive measures and detection strategies:

- Log all state changes and alert on Referer anomalies
- Use double-submit cookie pattern for CSRF protection
- Rate-limit email changes

## Objectives

1. Perform unauthorized account modification
2. Demonstrate endpoint vulnerability
3. Chain to further actions like cash out

## Instructions

### Step 1: Interact with Form

**Context**: Manually trigger to simulate user action.

Click the prominent submit button on the page.

> Expected: POST request in network tab to /change_email with email param.

### Step 2: Monitor Request

**Context**: Verify bypass success.

In dev tools Network tab, confirm 200 OK or redirect without errors.

> Expected: Successful response indicating change applied.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari-Browser]]

## Tags

- csrf
- account-takeover
