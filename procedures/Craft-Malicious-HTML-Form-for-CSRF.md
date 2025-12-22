---
id: proc-craft-csrf-form
tags:
  - csrf
  - exploit
  - html
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
updated_at: '2025-12-14T17:27:57.524Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious HTML Form for CSRF

## Summary

This procedure details creating an HTML page with a hidden form that auto-submits a forged POST request to the NordVPN password change endpoint, allowing an attacker to set a new password without the victim's knowledge.

## Description

CSRF exploits rely on tricking authenticated users into submitting malicious requests via external pages. For NordVPN, the form targets https://nordvpn.com/profile/ with parameters tmpl=settings, password=attacker_password, and password_confirmation=attacker_password. The HTML uses JavaScript to auto-submit upon load, or a visible button for manual trigger, bypassing the lack of CSRF tokens.

## Requirements

1. Knowledge of the target endpoint and parameters from reconnaissance
2. Text editor for HTML creation
3. Attacker's desired new password

## Defense

Defensive measures and detection strategies:

- Require unique CSRF tokens per session and validate on server-side
- Use SameSite cookies to prevent cross-site requests
- Educate users on phishing and suspicious file opens

## Objectives

1. Generate a self-contained HTML exploit file
2. Ensure the form mimics legitimate submission
3. Test for successful request forging

## Instructions

### Step 1: Create Basic HTML Structure

**Context**: Set up the form with the target action and hidden inputs.

Write HTML with <form method="POST" action="https://nordvpn.com/profile/"> and inputs for tmpl, password, and password_confirmation.

**Expected Output**: Static form skeleton.

### Step 2: Add Auto-Submission Script

**Context**: Use JavaScript to submit the form on page load.

Include <script>document.forms[0].submit();</script> after the form.

**Expected Output**: Form that submits automatically when opened.

### Step 3: Test the Form Locally

**Context**: Open the HTML in a browser while authenticated to NordVPN to verify.

Load the file and check network tab for the POST request.

**Expected Output**: Password change request sent with attacker values.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-exploit]]
- [[JavaScript]]
