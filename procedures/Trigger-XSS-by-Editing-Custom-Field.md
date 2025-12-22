---
tags:
  - xss
  - trigger
  - ie11
  - hackerone
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
  - '[[tools/Ashampoo-Snap]]'
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
updated_at: '2025-12-13T23:56:03.947Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9e189d5d-1f25-4af7-8524-d00629230e61
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Editing-Custom-Field

## Summary

This procedure demonstrates triggering the stored XSS by having a program admin edit and save the custom field value in the malicious report, executing JavaScript in Internet Explorer 11.

## Description

As the program admin views the submitted report, editing the 'Custom data - hacker facing' field causes the unsanitized payload from the additional information to render and execute. This leads to arbitrary JS in the browser context, such as alerting the domain, with potential for session theft. The vulnerability is IE11-specific due to rendering differences.

## Requirements

1. Program admin access to view and edit reports
2. Internet Explorer 11 as the browser
3. Access to the submitted malicious report

## Defense

Defensive measures and detection strategies:

- Apply HTML entity encoding to custom field values on render
- Disable or restrict custom fields in legacy browser support
- Log and alert on JavaScript errors or unusual browser behaviors

## Objectives

1. Execute the stored JavaScript payload in the admin's session
2. Demonstrate impact like domain alerting or session access
3. Highlight IE11-specific exploitation

## Instructions

### Step 1: Open the Malicious Report

**Context**: Log in as admin and locate the submitted report.

Navigate to the program's reports dashboard and open the target report.

### Step 2: Edit and Save Custom Field

**Context**: Interact with the custom field to trigger rendering of the payload.

Locate the 'Custom data - hacker facing' field, edit or modify its value (e.g., append text), and click save.

Use [[tools/Internet-Explorer-11]] for this step, and capture screenshots with [[tools/Ashampoo-Snap]] to document the alert.

> Upon saving, the payload executes, showing an alert with 'hackerone.com'. In modern browsers, it may not trigger due to better parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer-11]]
- [[tools/Ashampoo-Snap]]

## Tags

- [[xss]]
- [[trigger]]
