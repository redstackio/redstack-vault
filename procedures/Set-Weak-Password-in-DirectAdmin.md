---
id: proc-uuid-2
tags:
  - weak-password
  - directadmin
  - password-policy
  - brute-force
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:28:28.479Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
---
# Set-Weak-Password-in-DirectAdmin

## Summary

This procedure exploits the lack of password complexity requirements in DirectAdmin's password change functionality, allowing the setting of weak passwords like '1234' or '0000', which significantly lowers the barrier for brute-force attacks on user accounts.

## Description

The DirectAdmin password change endpoint at /user/password?redirect=yes does not enforce minimum length, character variety, or bans on dictionary/common weak passwords. An authenticated user can navigate to this page, enter their current password for verification, and submit any weak new password, which is accepted without validation. This misconfiguration reduces the effective security of accounts, making them prime targets for guessing attacks. The procedure is typically used in penetration testing to demonstrate policy weaknesses, with prerequisites including an active session from prior login.

## Requirements

1. Active authenticated session in DirectAdmin (from prior login procedure)
2. Knowledge of the current password for verification
3. Access to the web interface without session timeouts

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies in DirectAdmin configuration (e.g., edit directadmin.conf to set min password length and complexity rules)
- Implement server-side validation scripts or plugins to reject weak passwords before acceptance
- Log all password changes and alert on suspicious patterns, such as short or numeric-only passwords, via integration with SIEM tools

## Objectives

1. Change account password to a deliberately weak value
2. Verify the absence of policy enforcement
3. Highlight the resulting increase in brute-force vulnerability

## Instructions

### Step 1: Navigate to Password Change Page

**Context**: Access the dedicated endpoint for modifying the user password within the authenticated session.

From the DirectAdmin dashboard, click on the 'Password' option in the user menu, or directly enter the URL: https://da.theendlessweb.com:2222/user/password?redirect=yes (replace with target). The form will load with fields for current password, new password, and confirmation.

### Step 2: Submit Weak Password

**Context**: Input and apply a weak password to test policy enforcement.

Enter the current password in the verification field. In the new password and confirmation fields, enter a weak value such as '1234' or '0000'. Click the submit button.

> The form processes without errors, displaying a success message like 'Password has been changed.' Log out and test logging back in with the new weak password to confirm. No validation warnings appear, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used


## Tags

- [[weak-password]]
- [[directadmin]]
- [[password-policy]]
- [[brute-force]]
