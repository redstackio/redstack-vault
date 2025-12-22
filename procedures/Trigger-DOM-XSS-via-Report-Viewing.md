---
id: proc-infogram-trigger-001
tags:
  - xss-trigger
  - execution
  - browser
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
updated_at: '2025-12-14T03:16:02.893Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-XSS-via-Report-Viewing

## Summary

This procedure demonstrates triggering the stored DOM XSS by viewing the published Infogram report and interacting with the injected element, resulting in JavaScript execution in the victim's browser.

## Description

Viewing the public report causes the browser to parse and render the Overview Table, executing the onmouseover event handler when hovered. This leads to arbitrary JS execution, such as alerts or data exfiltration, in the context of the Infogram domain. Impact includes session theft or phishing; requires the published URL from prior steps.

## Requirements

1. Public report URL
2. Victim browser (or incognito session for testing)
3. No account needed for viewing

## Defense

Defensive measures and detection strategies:

- Content Security Policy (CSP) to block inline JS execution
- Browser-side XSS auditors or extensions for detection
- Monitor for anomalous JS alerts in error logs

## Objectives

1. Load the report in a browser
2. Interact to fire the payload
3. Observe JS execution confirming vuln

## Instructions

### Step 1: Open Published Report

**Context**: Access the report as a victim would.

Navigate to the public URL, e.g., https://infogram.com/report-classic-1g57pr0g3xdvp01.

> Report loads with Overview Table displaying the injected link.

### Step 2: Interact with Payload

**Context**: Trigger the event handler.

Hover the mouse over the "Click for Detail" link in the table.

> JavaScript alert executes: "HackerOne MkSecurity Dom XSS".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[Execution]]
- [[browser]]
