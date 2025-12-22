---
tags:
  - automation
  - poc-script
type: procedure
tools:
  - '[[tools/JavaScript]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 83e8c4a6-0582-4632-a532-89b9a6da94d7
created_at: '2025-12-13T09:00:34.391Z'
updated_at: '2025-12-13T09:00:34.391Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Automate Attack with JavaScript PoC

## Summary

This procedure automates the web cache poisoning attack using a JavaScript script to generate random URLs, trigger caching via popups, and facilitate data exfiltration.

## Description

The script creates a random ID, opens a popup to the crafted URL for the logged-in victim, closes it after a delay, and displays the URL for the attacker to access the cached data.

## Requirements

1. Victim interaction with the script (e.g., via malicious page)
2. JavaScript-enabled browser
3. Logged-in victim session

## Defense

Defensive measures and detection strategies:

- Block popups and monitor for suspicious URL patterns
- Use Content-Security-Policy to restrict scripts

## Objectives

1. Automate caching and disclosure
2. Scale the attack for multiple victims
3. Generate proof-of-concept for reporting

## Instructions

### Step 1: Run the JavaScript Script

**Context**: Execute the script to handle random ID generation and popup management.

The script generates a 10-character alphanumeric ID, opens popup to https://www.lyst.com/[random].css, waits, closes it, and provides the URL.

> Use timers for opening/closing to ensure caching occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/JavaScript]]

## Tags

- automation
- poc-script
