---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - crowdsignal
  - survey-creation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.585Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Crowdsignal-Survey

## Summary

This procedure outlines creating a new survey in the Crowdsignal platform, which serves as the initial setup for exploiting IDOR vulnerabilities in media handling.

## Description

In the context of the IDOR attack on Crowdsignal, creating a survey provides the editable environment where questions, headers, footers, and polls can be manipulated. The platform uses authenticated sessions, and this step assumes valid user credentials. Expected outcome is a new survey ready for adding elements that trigger media_code requests.

## Requirements

1. Valid Crowdsignal account login
2. Web browser access to https://app.crowdsignal.com
3. No special permissions beyond standard user access

## Defense

Defensive measures and detection strategies:

- Monitor for unusual survey creation patterns from new accounts
- Implement rate limiting on survey edits

## Objectives

1. Establish a controllable survey instance
2. Prepare for media embedding actions
3. Enable request interception setup

## Instructions

### Step 1: Log In and Navigate to Dashboard

**Context**: Access the Crowdsignal interface to initiate survey creation.

Log in at https://app.crowdsignal.com and click 'New Survey' on the dashboard.

> This loads the survey editor; no code execution needed.

### Step 2: Configure Basic Survey Details

**Context**: Set up the survey to make it editable for questions.

Enter a title and description, then proceed to the editor.

> Survey is now created with a unique ID for subsequent edits.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[crowdsignal]]
- [[survey-creation]]
