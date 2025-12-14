---
tags:
  - xss
  - web-access
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
id: d12dabb2-e14d-4847-9cb0-c70b11f8c46a
created_at: '2025-12-13T23:56:20.441Z'
updated_at: '2025-12-13T23:56:20.441Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate to MoPub Custom Reports Page

## Summary

This procedure involves accessing the custom reports page in the MoPub web application as the initial step to identify and exploit input fields for vulnerabilities like XSS.

## Description

Navigating to the specified URL sets up the environment for testing report creation features. This is targeted at web applications lacking proper input validation, leading to potential script injection. Expected outcome is loading the page for further interaction.

## Requirements

1. Web browser (e.g., [[tools/Firefox]] or [[tools/Chrome]])
2. Valid MoPub account and internet access
3. No special configurations needed

## Defense

Defensive measures and detection strategies:

- Implement access controls and monitor unusual navigation patterns
- Use web application firewalls (WAF) to detect suspicious URL access

## Objectives

1. Gain access to the report creation interface
2. Prepare for payload injection
3. Confirm endpoint availability

## Instructions

### Step 1: Open Browser and Navigate

**Context**: Launch a browser and enter the target URL to access the reports page.

**Instructions**: Open [[tools/Firefox]] or [[tools/Chrome]] and go to https://app.mopub.com/reports/custom/.

> This loads the custom reports interface for further actions.

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
- [[web-access]]
