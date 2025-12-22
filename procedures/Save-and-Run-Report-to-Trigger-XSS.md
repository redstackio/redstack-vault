---
tags:
  - xss
  - trigger-exploit
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 23ca6649-9915-4583-a861-f3bdffbd68c3
created_at: '2025-12-13T23:56:20.436Z'
updated_at: '2025-12-13T23:56:20.436Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save and Run Report to Trigger XSS

## Summary

This procedure saves the report with the injected payload and triggers the XSS by running or viewing it.

## Description

Saving persists the script, and viewing executes it, potentially stealing cookies or data. This confirms the stored XSS in MoPub. Outcome is script execution.

## Requirements

1. Payload-injected form
2. Permission to save reports
3. Browser to view results

## Defense

Defensive measures and detection strategies:

- Validate and sanitize stored data before rendering
- Monitor for JavaScript execution alerts in logs

## Objectives

1. Persist and execute the script
2. Demonstrate data theft potential
3. Validate vulnerability impact

## Instructions

### Step 1: Click Run and Save

**Context**: Submit the form to save and execute the report.

**Instructions**: Click 'Run and save' to persist the payload.

> Upon viewing, the script triggers an alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[trigger-exploit]]
