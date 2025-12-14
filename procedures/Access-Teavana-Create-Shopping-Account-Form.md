---
tags:
  - web
  - form-access
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
id: e47192a7-d827-42ea-8a82-d79bc82f2ac2
created_at: '2025-12-14T03:46:20.647Z'
updated_at: '2025-12-14T03:46:20.647Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Teavana Create Shopping Account Form

## Summary

This procedure transitions from the sign-in page to the account creation form, exposing the vulnerable partner ID input field for testing.

## Description

As part of the SQL injection attack chain on Teavana's sign-up process, this step involves interacting with the UI to reveal the registration form. The form is part of the Salesforce Commerce Cloud backend, where insufficient input validation on the partnerno field enables exploitation. Prerequisites include being on the account page; outcomes confirm the form's availability for payload injection.

## Requirements

1. Loaded account page from prior navigation
2. Standard web browser
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Use CAPTCHA on form access to deter bots
- Log form loads and monitor for rapid successive attempts

## Objectives

1. Display the sign-up form with all fields
2. Identify the partner ID field for targeting
3. Enable direct input testing

## Instructions

### Step 1: Click Sign-In and Select Create Account

**Context**: The sign-in page provides a gateway to creation; clicking initiates the form load.

**Action**:

Click the 'Sign In' button, then click 'Create Shopping Account'.

> Expected output: The form opens with fields for email, password, and partnerno. Verify the partner ID field is editable. If redirected unexpectedly, clear browser cookies and retry.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- form-access
