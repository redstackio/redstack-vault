---
tags:
  - xss
  - execution
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b3405635-89f7-4007-b077-ef707684637d
created_at: '2025-12-13T23:52:43.787Z'
updated_at: '2025-12-13T23:52:43.787Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Title-Suggestion

## Summary

This procedure triggers the stored XSS payload by simulating a victim creating a new thread with a similar title, causing the system to suggest and display the malicious title, executing the script in the browser.

## Description

On support.rockstargames.com, the autocomplete feature searches stored titles and displays matches without proper escaping, leading to XSS execution. The attacker can use a secondary account or social engineering to prompt a victim to create a thread with a title close to the injected one (e.g., keyword overlap). Outcomes include JavaScript running in the victim's context, enabling cookie theft or keylogging. Prerequisites: The injection procedure completed, and access to trigger the suggestion.

## Requirements

1. Access to a victim account or ability to influence victim behavior
2. Knowledge of the injected title for similarity crafting
3. Monitoring tools to capture exfiltrated data

## Defense

Defensive measures and detection strategies:

- Sanitize all suggestion outputs with HTML escaping
- Rate-limit or validate autocomplete queries
- Log and alert on script execution attempts via browser console monitoring

## Objectives

1. Display the stored payload in a victim's browser
2. Execute JavaScript to steal session data
3. Achieve session hijacking or data exfiltration

## Instructions

### Step 1: Simulate Victim Thread Creation

**Context**: Use a victim-like account to start a new thread with a title similar to the injected one.

Log in with a secondary account, go to Create New Thread, and enter a title like 'GTA Help Issue' if the injected was 'GTA Help Problem'.

> The system queries and suggests matching titles, pulling the malicious one.

### Step 2: Observe Execution

**Context**: As the suggestion appears, the payload executes automatically.

Select or view the suggested title; the script runs, e.g., sending cookies to attacker server.

> Verify via network tab: Look for outbound requests to external domains.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
