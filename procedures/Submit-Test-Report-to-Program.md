---
tags:
  - setup
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3dc4503a-d475-488d-9f38-020b2cca5e37
created_at: '2025-12-14T17:25:47.365Z'
updated_at: '2025-12-14T17:25:47.365Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Test-Report-to-Program

## Summary

This procedure sets up the attack by submitting a controlled test vulnerability report to a HackerOne program, providing a legitimate entry point for the subsequent review process exploitation.

## Description

In the context of exploiting an IDOR in HackerOne's feedback system, this initial step involves using a controlled hacker account to submit a benign test report to a target program (e.g., Parrot Sec). This report serves as the basis for the review process where the vulnerability can be triggered. The target environment is the HackerOne web platform, requiring a registered hacker account. Expected outcomes include a new report ID that can be closed and reviewed.

## Requirements

1. Valid HackerOne account (e.g., jong_jong) with program participation
2. Access to the target program dashboard
3. Basic knowledge of vulnerability reporting format

## Defense

Defensive measures and detection strategies:

- Monitor for unusual test or low-quality report submissions from known accounts
- Implement rate limiting on report submissions per user

## Objectives

1. Establish a report for review initiation
2. Ensure report is tied to the controlled account
3. Prepare for closure and feedback

## Instructions

### Step 1: Log In and Navigate to Program

**Context**: Access the HackerOne platform and select the target program to submit the report.

Log in to HackerOne as the controlled account and navigate to the Parrot Sec program page.

### Step 2: Create and Submit Test Report

**Context**: Draft a simple test vulnerability report to trigger the workflow.

Fill out the report form with basic details (e.g., a non-critical finding) and submit it.

**Expected Output**: Confirmation of report submission with a generated report ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[web]]
