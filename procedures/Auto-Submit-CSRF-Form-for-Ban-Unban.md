---
id: proc-auto-submit-csrf-001
tags:
  - csrf
  - javascript
  - execution
  - ban-unban
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/auto-submit-csrf-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.480Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Auto-Submit-CSRF-Form-for-Ban-Unban

## Summary

This procedure executes the CSRF attack by automatically submitting the hidden form via JavaScript upon page load, resulting in unauthorized banning or unbanning of users in the Steam broadcast chat.

## Description

The submission targets the unprotected `ajaxupdateusermute/` endpoint, forging a moderation action as the victim. The hidden iframe ensures invisibility. Prerequisites: Victim visit to the page while logged in; outcomes: Silent moderation change, disrupting chat without alerts.

## Requirements

1. Malicious HTML page loaded in victim's authenticated browser
2. Valid form parameters from prior steps
3. No browser extensions blocking auto-submits

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens on state-changing endpoints
- Log all mute/ban actions with IP and referrer checks
- Browser same-site cookie policies to mitigate CSRF

## Objectives

1. Trigger POST request silently on page load
2. Achieve ban/unban without user interaction
3. Confirm action via broadcast chat verification

## Instructions

### Step 1: Load the Malicious Page

**Context**: Ensure the page is accessed, activating the script.

When the victim visits, the JavaScript executes immediately.

### Step 2: Execute Auto-Submit Using JavaScript Command

**Context**: The form submission handles the exploitation.

Execute [[commands/auto-submit-csrf-form]] embedded in the HTML:

```javascript
document.getElementById("csrf-form").submit();
```

> This submits the POST to the endpoint with hidden parameters, performing the action in the background.

**Expected Output**: No visible change; server responds with success (e.g., JSON acknowledgment).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/auto-submit-csrf-form]]

## Tools Used


## Tags

- [[csrf]]
- [[JavaScript]]
- [[Execution]]
- [[ban-unban]]
