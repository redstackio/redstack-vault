---
tags:
  - xss
  - report-creation
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5183c85f-90f9-47dc-82e7-d5b46ac7731d
created_at: '2025-12-13T23:56:20.439Z'
updated_at: '2025-12-13T23:56:20.439Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Initiate New Network Report Creation

## Summary

This procedure starts the creation of a new network report in MoPub, exposing the name field for potential XSS injection.

## Description

Clicking the button opens the form where unsanitized inputs can be entered. This targets web apps with poor output escaping, allowing persistent scripts. Outcome is an open form ready for input.

## Requirements

1. Access to MoPub custom reports page
2. Web browser like [[tools/Chrome]]
3. Logged-in session

## Defense

Defensive measures and detection strategies:

- Enforce input validation on form submissions
- Monitor for repeated form initiations as anomaly

## Objectives

1. Open the report creation form
2. Access vulnerable input fields
3. Set stage for payload insertion

## Instructions

### Step 1: Click New Report Button

**Context**: Locate and click the button to begin report creation.

**Instructions**: On the reports page, click 'New network report'.

> This displays the form with the name field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[report-creation]]
