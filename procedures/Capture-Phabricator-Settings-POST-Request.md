---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - request-capture
  - phabricator
type: procedure
tools:
  - '[[tools/Browser-Network-Inspector]]'
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
updated_at: '2025-12-14T03:16:31.200Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Capture-Phabricator-Settings-POST-Request

## Summary

This procedure uses browser developer tools to intercept and copy the POST request sent when saving Phabricator settings, providing a template for injecting the XSS payload without browser-side sanitization.

## Description

Phabricator's settings save functionality sends a POST request to /settings/panel/display/ with form data, including the 'editor' parameter. By capturing this with the browser's network panel, attackers can replicate it using tools like curl to include unsanitized payloads. This targets the libphutil library's phutil_tag function weakness. Prerequisites include an active session; outcomes are a copyable curl command with all headers and parameters.

## Requirements

1. Browser with DevTools (e.g., Chrome)
2. Active Phabricator session
3. Network panel enabled

## Defense

Defensive measures and detection strategies:

- Log all settings POST requests and flag unusual payloads
- Rate-limit settings changes to prevent rapid modifications

## Objectives

1. Intercept the legitimate save request
2. Extract curl-compatible format
3. Identify key parameters like 'editor' and CSRF token

## Instructions

### Step 1: Enable Network Panel

**Context**: Open DevTools to monitor HTTP traffic during the save action.

No command required; right-click page and select 'Inspect', then go to Network tab.

> Clear any existing logs and ensure 'Preserve log' is checked.

### Step 2: Trigger Save and Capture

**Context**: Perform a benign save to generate the POST request for copying.

No command required; modify a non-critical setting (e.g., theme) and click 'Save'.

> In the Network panel, locate the POST to /settings/panel/display/, right-click, and select 'Copy as cURL'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Network-Inspector]]

## Tags

- [[request-capture]]
- [[phabricator]]
