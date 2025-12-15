---
id: proc-khan-csv-name-injection
tags:
  - csv-injection
  - formula-injection
type: procedure
tools:
  - '[[tools/LibreOffice]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:28.337Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# CSV-Injection-in-Student-Data-Export-via-Name-Field

## Summary

This procedure exploits insufficient escaping in Khan Academy's student data export function by injecting a formula payload into the student name field, leading to execution when the CSV is opened in LibreOffice.

## Description

In the teacher interface, the student name input is not properly sanitized for CSV export. Attackers can insert payloads that bypass a basic double-quote filter using whitespace and single-quote formatting specific to LibreOffice, resulting in client-side formula evaluation. This demonstrates initial injection feasibility but is limited by escaping on complex payloads.

## Requirements

1. Access to Khan Academy teacher account
2. LibreOffice installed for testing
3. Knowledge of CSV formula syntax

## Defense

Defensive measures and detection strategies:

- Implement strict CSV escaping (e.g., RFC 4180 compliance) for all user inputs
- Validate and sanitize inputs to prevent formula characters (=, +, -, @)
- Warn users or disable auto-execution in spreadsheet software

## Objectives

1. Inject and verify basic formula execution in exported CSV
2. Assess bypassing of existing filters
3. Establish foundation for more advanced exploits

## Instructions

### Step 1: Craft and Inject Payload

**Context**: Prepare a payload that evades the double-quote filter using LibreOffice's single-quote format.

No command executed; perform via web interface:

- Log in as teacher.
- Edit or add student with name: `',"=2+11',"`
- Save changes.

> This injects a formula that calculates 2+11=13 without triggering quote escaping.

### Step 2: Export and Test CSV

**Context**: Generate the CSV and open in LibreOffice to confirm execution.

Use LibreOffice to open the exported CSV file.

> Expected: Cell evaluates to 13, confirming injection success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/LibreOffice]]

## Tags

- [[csv-injection]]
- [[client-side-execution]]
