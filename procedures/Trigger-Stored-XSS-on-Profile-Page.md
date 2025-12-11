---
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1059  .007]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 690569ef-e802-4419-99bb-60091c5979f6
created_at: '2025-12-11T06:10:28.397Z'
updated_at: '2025-12-11T06:10:28.397Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059  .007]]'
---
# Trigger Stored XSS on Profile Page

## Summary

This procedure triggers the stored XSS by visiting the affected Imgur profile page, causing the injected JavaScript to execute.

## Description

Accessing the profile (e.g., https://gidsumaya.imgur.com/) loads the stored payload, executing the script in the browser. This demonstrates the vulnerability's impact, such as displaying an alert.

## Requirements

1. Injected album from previous step.
2. Web browser.
3. URL of the affected profile.

## Defense

Defensive measures and detection strategies:

- Regularly audit stored content for malicious scripts.
- Use browser security features like XSS Auditor (deprecated) or modern alternatives.

## Objectives

1. Execute the stored payload.
2. Confirm arbitrary code runs.
3. Assess potential for further exploitation.

## Instructions

### Step 1: Visit Profile

**Context**: Load the profile page to trigger execution.

Navigate to https://username.imgur.com/ where the album is linked.

> Observe the alert(1) popping up.

### Step 2: Verify Execution

**Context**: Inspect browser console for script activity.

Use developer tools to confirm script ran without errors.

> Look for executed JavaScript indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[Execution]]
