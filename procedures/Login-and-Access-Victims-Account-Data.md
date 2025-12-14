---
id: proc-login-access-data
tags:
  - account-takeover
  - data-access
  - pii-exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:18.226Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Account Discovery]]'
---
# Login and Access Victim's Account Data

## Summary

This procedure logs into the newly associated account to view and manage the victim's sensitive data, including PII, order history, addresses, and saved payment details, completing the account takeover.

## Description

After the IDOR exploitation links the new credentials to the victim's order, logging in grants full access to the account as if the attacker were the owner. This allows disclosure of full name, address, phone, all orders, and payment info, with capabilities to delete or modify orders. The target is theperfumeshop.com's account dashboard post-registration.

## Requirements

1. New email and password from IDOR exploitation step
2. Valid session from previous requests
3. Browser access to login endpoint

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication (MFA) for account access
- Monitor login attempts from new IPs and alert on suspicious activity
- Audit order associations during registration for anomalies

## Objectives

1. Authenticate with compromised credentials
2. Exfiltrate PII and account details
3. Demonstrate control over victim's orders and payments

## Instructions

### Step 1: Navigate to Login Page

**Context**: Go to https://theperfumeshop.com/login in the browser.

Use the UI to enter the random email and password (e.g., 'Password123').

> Submit the form; expect redirection to dashboard upon success.

### Step 2: View Account Sections

**Context**: Once logged in, navigate to 'My Account' > Personal Info, Addresses, Orders, and Payments.

Inspect the pages for victim's data.

> Expected output: Victim's full name, address, phone number, order history (e.g., past purchases), and saved card details visible and editable.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[pii-exfiltration]]
