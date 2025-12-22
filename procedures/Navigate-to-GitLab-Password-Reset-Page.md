---
tags:
  - gitlab
  - password-reset
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
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
id: 94681932-1d6c-4c9d-9a9b-c652215087a7
created_at: '2025-12-11T06:10:31.182Z'
updated_at: '2025-12-11T06:10:31.182Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Navigate to GitLab Password Reset Page

## Summary

This procedure involves accessing the GitLab password reset form and submitting the victim's email address to initiate the reset process, setting up for request interception.

## Description

In this initial step of exploiting the GitLab password reset vulnerability, the attacker navigates to the 'Forgot Your Password' page on a GitLab instance and enters the victim's email. This triggers an HTTP request that can be intercepted for further manipulation. The target environment is a web-based GitLab service, and the expected outcome is the generation of a password reset request.

## Requirements

1. Access to a web browser
2. Knowledge of the victim's email address
3. GitLab instance URL

## Defense

Defensive measures and detection strategies:

- Monitor for unusual password reset requests
- Implement rate limiting on reset endpoints

## Objectives

1. Initiate password reset process
2. Prepare for request interception
3. No direct impact yet, but sets stage for exploitation

## Instructions

### Step 1: Access the Form

**Context**: Open the GitLab login page and navigate to the password reset section.

Access the password reset form and enter the victim's email address (e.g., victim@gmail.com).

> Submit the form to trigger the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- gitlab
- password-reset
