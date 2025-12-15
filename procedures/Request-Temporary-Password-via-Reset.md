---
tags:
  - password-reset
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:28.473Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4b2b6efe-370a-4953-9159-45ef99722607
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-Temporary-Password-via-Reset

## Summary

This procedure initiates the password reset flow on the MTN Group web application to trigger the generation and email delivery of a weak alphanumeric temporary password, setting the stage for brute force exploitation.

## Description

In the MTN Group application at https://mycontract.mtn.co.za/landing/landing.htm, the password reset mechanism lacks strong generation policies, producing only alphanumeric temporary passwords (e.g., 8 characters from a-z0-9). This procedure covers navigating to the login, initiating reset, and submitting the user ID for email delivery. It exploits the absence of rate limiting or complexity requirements, making subsequent brute force viable. Prerequisites include knowing the target user ID and having network access to the site.

## Requirements

1. Web browser with internet access
2. Knowledge of the target user's ID or associated email
3. No authentication required for reset initiation

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on reset requests
- Generate temporary passwords with full character sets (including specials) and higher lengths
- Log and monitor reset attempts for anomalies

## Objectives

1. Trigger temporary password generation
2. Receive or predict the weak credential via email
3. Prepare for brute force without needing email interception

## Instructions

### Step 1: Access Login Page

**Context**: Load the target application's login interface.

Navigate to https://mycontract.mtn.co.za/landing/landing.htm in your browser.

> Verify the page displays login fields and a 'Forgot Password' link.

### Step 2: Start Reset Flow

**Context**: Begin the reset process to expose the vulnerability.

Click the 'Forgot Password' link.

> The reset form should appear, offering delivery options.

### Step 3: Submit for Email Delivery

**Context**: Request the temporary password, which will be weak and brute-forceable.

Select the email radio button, enter the user ID, and submit.

> A confirmation appears; the email contains the alphanumeric temporary password.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[web-auth]]
