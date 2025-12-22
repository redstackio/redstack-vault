---
tags:
  - auth-bypass
  - retest
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a4e3ade9-6099-41c4-9b63-b6baa99dc6ae
created_at: '2025-12-14T17:30:58.648Z'
updated_at: '2025-12-14T17:30:58.648Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Retest-Email-Change-Fix-in-Shopify

## Summary

This procedure involves retesting a prior fix for an email confirmation vulnerability in Shopify's account system, identifying that email changes can still be made before verification completes on the original email.

## Description

During retesting of a temporary fix for a previous bug (report #791775), the attacker logs into the Shopify admin panel and navigates to account settings. The process reveals that the system allows updating the email address immediately after initiation, without requiring completion of the verification sent to the original email. This sets the stage for exploitation in legacy accounts not using the single login system. Prerequisites include valid login credentials and access to the myshop.myshopify.com/admin portal.

## Requirements

1. Active Shopify account with admin access
2. Web browser for navigation and timing observation
3. Knowledge of the prior vulnerability (e.g., report #791775)

## Defense

Defensive measures and detection strategies:

- Implement strict verification sequencing where email changes are locked until original verification completes
- Monitor for rapid email change attempts via rate limiting or anomaly detection in logs
- Migrate all users to single login system to eliminate legacy bypasses

## Objectives

1. Confirm the persistence of the email change vulnerability post-fix
2. Gather timing details for subsequent exploitation
3. Validate impact on non-single-login accounts

## Instructions

### Step 1: Access Account Settings

**Context**: Log in and navigate to the email management section to initiate a change.

Open a web browser and go to myshop.myshopify.com/admin. Log in with valid credentials. Click on the account icon in the top right, then select "Account settings." Under the "Store details" or "User profile" section, locate the email change option and enter a new email address to trigger the verification process.

> Observe that a verification email is queued for the original address, but the UI allows proceeding without waiting.

### Step 2: Monitor and Test Timing

**Context**: Use developer tools to inspect if changes persist before original verification.

Press F12 to open developer tools, switch to the Network tab, and attempt to save the email change. Note the API calls (likely to /admin/account.json or similar endpoints) and check if the update succeeds immediately. Do not complete the original email verification to test the bypass window.

> Expected behavior: Email field updates in the profile without error, confirming the fix's inadequacy.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[retest]]
- [[shopify]]
