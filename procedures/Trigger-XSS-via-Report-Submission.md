---
id: proc-trigger-xss-report
tags:
  - xss
  - report
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:04.013Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Report-Submission

## Summary

This procedure submits a report associated with the malicious asset and views it to trigger XSS, demonstrating persistence across report contexts in HackerOne.

## Description

By linking the injected asset to a submitted report, the identifier renders in the report view, parsed by the vulnerable truncate function, executing the script. This extends the attack to report viewers, including program owners or other hackers, amplifying impact.

## Requirements

1. Malicious asset already injected
2. Ability to submit reports on the program
3. Viewer access to submitted reports

## Defense

Defensive measures and detection strategies:

- Sanitize asset references in report rendering
- Apply output encoding in report templates
- Monitor report views for JS execution anomalies
- Use strict CSP to block cross-origin or inline scripts

## Objectives

1. Persist XSS through report association
2. Execute payload in report viewing context
3. Affect report-specific user sessions

## Instructions

### Step 1: Submit Test Report

**Context**: Create a report that references the program's assets.

Go to the report submission form, select the program, and associate the malicious asset in the scope.

### Step 2: View Submitted Report

**Context**: Open the report to render the asset identifier.

Navigate to the report URL after submission.

**Expected Output**: Payload executes via alert on load.

### Step 3: Confirm Multi-User Impact

**Context**: Test in another session to verify broad execution.

Log in as another user and view the report.

**Expected Output**: XSS triggers for any viewer.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- report
