---
id: proc-create-accounts-001
tags:
  - account-creation
  - testing-setup
  - web
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:25:23.608Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create Multiple User Accounts for IDOR Testing

## Summary

This procedure sets up the foundational accounts needed to test Insecure Direct Object Reference (IDOR) vulnerabilities by creating a victim account for content generation and an attacker account for unauthorized access demonstration in web applications like demo.sftool.gov.

## Description

In scenarios involving access control flaws, such as IDOR, testers must simulate multiple users to isolate and exploit ownership bypasses. This involves registering distinct accounts on the target application, ensuring they can independently authenticate. The process targets applications with open registration, allowing creation of a 'victim' to own sensitive objects and an 'attacker' to probe unauthorized access. Expected outcomes include verified login for both, setting the stage for object creation and manipulation without triggering anti-automation measures.

## Requirements

1. Access to the target web application (e.g., https://demo.sftool.gov)
2. Valid email addresses or disposable credentials for registration
3. Web browser for navigation and form submission

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration to prevent bulk account creation
- Monitor for anomalous login patterns across new accounts
- Log all registration attempts and correlate with subsequent access events

## Objectives

1. Establish isolated victim and attacker personas
2. Verify independent authentication
3. Prepare for cross-account vulnerability testing

## Instructions

### Step 1: Navigate to Registration

**Context**: Locate and access the user registration endpoint to begin account creation.

No specific command; use browser to visit the login/registration page (typically /register or similar on demo.sftool.gov) and select 'Create Account'.

> Fill in required fields like username, email, and password for the victim account. Submit the form.

### Step 2: Complete Victim Account Setup

**Context**: Finalize the first account and test login to confirm functionality.

No specific command; after submission, check for confirmation email if required, then log in with victim credentials to verify access to the dashboard.

> Successful login indicates the account is active; log out after verification.

### Step 3: Repeat for Attacker Account

**Context**: Create the second account using different credentials to simulate an unauthorized user.

No specific command; repeat the registration process with distinct details for the attacker account, then log in and log out to confirm.

> Ensure no shared sessions or cookies interfere between accounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[idor-testing]]
- [[web-app]]
