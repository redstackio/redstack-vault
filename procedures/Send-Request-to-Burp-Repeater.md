---
id: uuid-repeater
tags:
  - repeater
  - request-replay
  - modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:28:59.261Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Send-Request-to-Burp-Repeater

## Summary

Forward a captured API request to Burp Repeater for easy editing and resending, facilitating parameter manipulation in API exploitation.

## Description

Burp Repeater allows isolated request testing without browser interaction, ideal for crafting malicious payloads like arbitrary teamIds in IDOR scenarios.

## Requirements

1. Request in Burp Proxy history
2. Burp Suite Professional or Community

## Defense

Defensive measures and detection strategies:

- Server-side rate limiting on API endpoints
- Anomaly detection for repeated identical requests
- WAF rules against modified payloads

## Objectives

1. Load request into editable interface
2. Verify original functionality
3. Set up for exploitation

## Instructions

### Step 1: Forward to Repeater

**Context**: Transfer from history for modification.

**Instructions**: Right-click the request in Proxy > HTTP history, select 'Send to Repeater', and confirm it loads in a new tab.

> Test by sending once to ensure original response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- replay
- testing
