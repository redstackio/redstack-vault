---
id: proc-uuid-3
tags:
  - credential-use
  - account-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.248Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Compromised-myPay-Account

## Summary

This procedure uses the newly set password to authenticate to the myPay account, granting access to sensitive financial information for the targeted DoD employee.

## Description

After exploiting the password reset, log in via the standard myPay login form using the target username and new password. This provides dashboard access to view/modify pay history, partial SSNs, addresses, and direct deposits. Targets the web login at https://mypay.dfas.mil. Expected outcome: Full account control.

## Requirements

1. Compromised credentials (username and new password)
2. Web browser
3. Internet access to myPay

## Defense

Defensive measures and detection strategies:

- Enable login notifications and anomaly detection (e.g., unusual IP logins)
- Implement account lockout after failed attempts
- Require MFA for all logins

## Objectives

1. Authenticate with stolen credentials
2. Access and potentially alter financial data
3. Chain to linked services

## Instructions

### Step 1: Navigate to Login

**Context**: Go to the myPay authentication page.

Visit https://mypay.dfas.mil/ and click login.

### Step 2: Submit Credentials

**Context**: Enter the compromised details to gain access.

Input username: targetuser, password: newpass, and submit the form.

**Expected Output**: Redirect to personalized dashboard with account data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- login
- valid-accounts
