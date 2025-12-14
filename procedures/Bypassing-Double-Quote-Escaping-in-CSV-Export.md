---
id: proc-khan-csv-bypass
tags:
  - csv-injection
  - escaping-bypass
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
updated_at: '2025-12-14T17:23:28.325Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Bypassing-Double-Quote-Escaping-in-CSV-Export

## Summary

This procedure tests and bypasses the double-quote escaping in Khan Academy's CSV export for student names, confirming executable payloads without quotes.

## Description

The export function doubles double quotes (" to ""), but payloads avoiding them or using alternative formatting execute in LibreOffice. This limits complex attacks but allows simple formulas, providing insight into filter weaknesses.

## Requirements

1. Teacher access to Khan Academy
2. LibreOffice for payload testing
3. Various test payloads prepared

## Defense

Defensive measures and detection strategies:

- Apply comprehensive escaping beyond just quotes (e.g., block = at start of fields)
- Log export attempts and monitor for anomalous inputs
- Use CSV libraries that enforce strict parsing

## Objectives

1. Identify escaping limitations
2. Verify non-quoted payload execution
3. Inform advanced injection strategies

## Instructions

### Step 1: Test Quoted Payloads

**Context**: Insert payloads with double quotes to observe escaping.

Via web interface:

- Add student name with payload including ": e.g., ="test"
- Export CSV and inspect.

> Quotes doubled to "" , preventing execution.

### Step 2: Test Non-Quoted Payloads

**Context**: Use payloads without double quotes and open in LibreOffice.

Export CSV and open in LibreOffice.

> Simple formulas like =2+11 execute successfully.

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

- [[escaping-bypass]]
- [[formula-testing]]
