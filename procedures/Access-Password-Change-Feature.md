---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
name: Access-Password-Change-Feature
tags:
  - web-navigation
  - discovery
type: procedure
tools: []
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
updated_at: '2025-12-14T17:33:11.967Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Password-Change-Feature

## Summary

This procedure navigates an authenticated session to the password change functionality on the DoD website, positioning the attacker to trigger and capture the vulnerable request.

## Description

Once authenticated, the password change feature is accessed via a menu or link within the user dashboard. This step is crucial for CSRF exploitation as it exposes the POST endpoint lacking token validation. The target environment is a web app on IIS, and outcomes include loading the form for parameter analysis.

## Requirements

1. Active authenticated session from prior login
2. Web browser with proxy interception enabled
3. Knowledge of the site's navigation structure

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens on all state-changing forms
- Log and alert on access to sensitive features like password changes
- Implement session timeouts to limit exposure windows

## Objectives

1. Load the password change interface
2. Identify form fields for later replication
3. Confirm endpoint URL and method

## Instructions

### Step 1: Navigate to User Settings

**Context**: From the dashboard, locate the account management section.

No specific command; click on user profile or settings link.

> Expect navigation to a submenu with password options.

### Step 2: Select Password Change Option

**Context**: Trigger the form load to prepare for submission interception.

No specific command; click the 'Change Password' button or link.

> Successful output: Form appears with fields for current/new password and email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-navigation
- discovery
