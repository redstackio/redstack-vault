---
tags:
  - information-disclosure
  - web-export
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: d115b05c-5a2d-4f96-b847-c4a5a97939a2
created_at: '2025-12-11T03:47:39.513Z'
updated_at: '2025-12-11T03:47:39.513Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Export Report via UI

## Summary

This procedure uses the HackerOne UI export button to trigger the disclosure of hidden comments in partially disclosed reports.

## Description

By clicking the export button on a report page, the feature fails to restrict hidden comments, including them in the export. This targets the HackerOne web interface and results in unauthorized information disclosure.

## Requirements

1. Access to a partially disclosed report
2. Web browser
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Patch export functionality to enforce visibility restrictions
- Log and alert on export actions for partially disclosed reports

## Objectives

1. Initiate export via UI
2. Obtain exported data with hidden comments
3. Confirm disclosure vulnerability

## Instructions

### Step 1: Click Export Button

**Context**: Trigger the export on the report page.

Locate and click the 'Export' button on the report interface.

> This generates an export that includes hidden comments.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques

None

## Commands Used

None

## Tools Used

None

## Tags

- information-disclosure
- web-export
