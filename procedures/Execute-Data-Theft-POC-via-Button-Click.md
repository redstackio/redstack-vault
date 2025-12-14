---
id: proc-004
tags:
  - poc
  - data-theft
  - web
  - csrf
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:29:57.288Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Execute-Data-Theft-POC-via-Button-Click

## Summary

This procedure finalizes the attack by clicking a generated button on the simulation page, which invokes the JavaScript function to perform CSRF escalation and XSS-based data theft from HackerOne reports.

## Description

The proof-of-concept (PoC) relies on a dynamically created HTML button that, when clicked, calls the XSRF() function to orchestrate the entire chain: opening the escalation endpoint, simulating XSS for bypass, extracting data via regex, and displaying it. This step requires no further coding and demonstrates the attack's no-interaction nature. The target environment is the prepared web page with an active session, leading to exposure of private report details like descriptions.

## Requirements

1. Simulation page loaded with the 'H1 XSRF PoC' button generated.
2. Valid report ID configured in the script.
3. No browser popup blockers interfering.

## Defense

Defensive measures and detection strategies:

- Enforce user confirmation dialogs for sensitive actions like report escalations.
- Monitor for chained anomalous requests between HackerOne and JIRA, such as unexpected escalations followed by redirects.
- Use browser extensions or policies to block auto-popup scripts from external sites.

## Objectives

1. Trigger the full CSRF and XSS chain with minimal user action.
2. Achieve unauthorized data exfiltration from private reports.
3. Validate the vulnerability's impact in a controlled PoC.

## Instructions

### Step 1: Locate the POC Button

**Context**: Identify the interface element that initiates the attack.

On the loaded simulation page, find the button labeled 'H1 XSRF PoC'.

> Expected output: Button is visible and clickable.

### Step 2: Click to Execute

**Context**: Perform the single interaction to launch the theft sequence.

Click the 'H1 XSRF PoC' button.

> This calls the XSRF() function, leading to window open, escalation, data extraction, and redirect. Expected output: Report escalates silently; stolen data (e.g., description) appears on the final page without further input.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc]]
- [[data-theft]]
- [[web]]
- [[csrf]]
