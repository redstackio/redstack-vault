---
id: proc-weblate-capture-trial-001
tags:
  - capture
  - intercept
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.953Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Trial-Request-with-Burp-Suite

## Summary

This procedure intercepts the POST request sent when starting a trial, allowing analysis and forwarding for exploitation.

## Description

In the attack scenario, this captures the vulnerable /trial/ endpoint request during the commercial hosting trial initiation. The environment is the web platform with Burp proxy active. Expected outcome: Full request details available for replay.

## Requirements

1. Burp Suite proxy configured and intercept enabled
2. Browser navigated to trial prompt
3. Valid session cookie

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive requests end-to-end
- Detect proxy artifacts in request headers
- Log all trial initiation attempts

## Objectives

1. Isolate the trial POST request
2. Prepare for concurrent replay
3. Verify request payload integrity

## Instructions

### Step 1: Enable Intercept and Trigger Trial

**Context**: Position Burp to catch the exact request.

In Burp Suite, turn on intercept in the Proxy tab. In the browser, click 'Gratis trial for commercial hosting' followed by 'Start Trial'.

> The request will pause in Burp; inspect headers, body (likely JSON with account details), and forward if needed, but hold for analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- capture
- intercept
