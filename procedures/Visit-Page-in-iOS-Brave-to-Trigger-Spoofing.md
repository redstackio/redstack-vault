---
id: proc-brave-visit-trigger
name: Visit-Page-in-iOS-Brave-to-Trigger-Spoofing
tags:
  - url-spoofing
  - ios-browser
  - brave
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:39.936Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Visit-Page-in-iOS-Brave-to-Trigger-Spoofing

## Summary

This procedure involves loading the hosted HTML page in the vulnerable iOS Brave browser to execute the JavaScript and observe the URL replacement to a blob format in the address bar.

## Description

Targeting iOS Brave version 1.3.1 (build 17.02.14.11), navigating to the local URL triggers the history.replaceState call, changing the displayed URL to blob:http://192.168.1.111/xxxx. This bypasses expected same-origin checks, differing from desktop Brave/Chrome. The outcome is visual spoofing, potentially confusing users. No network interception or data exfil is involved; it's a client-side execution demo.

## Requirements

1. iOS device with Brave 1.3.1 installed
2. Local server running and accessible
3. Wi-Fi connection to the hosting machine

## Defense

Defensive measures and detection strategies:

- Patch browser to enforce stricter History API origin checks
- Implement browser extensions to alert on URL changes via JS
- User training to inspect page content beyond URL

## Objectives

1. Load the page and execute the script
2. Verify URL spoofing in address bar
3. Document the behavior for reporting

## Instructions

### Step 1: Open Brave on iOS

**Context**: Launch the specific vulnerable version of Brave on the iOS device.

Ensure version 1.3.1 is active; no command needed—manual app open.

> Confirm version in settings.

### Step 2: Navigate to Hosted URL

**Context**: Enter the local server URL to load the HTML and trigger the script.

In the address bar, type: http://192.168.1.111/blob.html and press go.

> The page loads, script runs, and address bar updates to blob URL. Expected: No crash; visual change immediate.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[blob-url]]
- [[history-replacestate]]
