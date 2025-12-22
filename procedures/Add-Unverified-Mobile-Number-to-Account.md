---
tags:
  - broken-authentication
  - mobile-verification
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
updated_at: '2025-12-14T17:30:58.806Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d03d865e-0c26-45d0-9330-895075f55726
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add-Unverified-Mobile-Number-to-Account

## Summary

This procedure exploits a flaw in Twitter's mobile number addition flow by inputting an unverified or random number, which gets loosely associated with the account without requiring code confirmation, setting up for subsequent password reset abuse.

## Description

In the context of Twitter's account settings, the mobile verification process fails to enforce verification during initial number submission. An attacker with access to the target account can enter any mobile number (e.g., one they control), receive a code prompt, but proceed without entering it. This associates the number for reset purposes, enabling takeover if the attacker controls the number. The target environment is the Twitter web platform, requiring only a logged-in session. Expected outcome is the number being usable for resets without full verification.

## Requirements

1. Active session in the target Twitter account via web browser
2. Control over a mobile number capable of receiving SMS
3. Standard internet access to Twitter's web interface

## Defense

Defensive measures and detection strategies:

- Enforce mandatory verification code entry before associating any mobile number
- Implement rate limiting on mobile number additions and reset attempts
- Log and monitor unverified number associations for anomaly detection

## Objectives

1. Associate a controlled mobile number with the target account without verification
2. Prepare the account for unauthorized password reset
3. Enable reception of reset codes on the attacker's device

## Instructions

### Step 1: Access Account Settings

**Context**: Log in to the target account and navigate to the mobile settings to initiate number addition.

Navigate to Twitter's account settings page, then select the "Phone" or mobile section under security options.

### Step 2: Input Mobile Number

**Context**: Enter and submit a random or controlled mobile number without verifying it.

Select the appropriate country code, input the mobile number (e.g., +1-555-123-4567 if testing with a controlled US number), and click "Continue" or "Send code". Ignore the verification prompt and do not enter any code; the system allows loose association.

> The interface will show "Verification code sent" but proceeds without input enforcement, linking the number for reset flows.

### Step 3: Confirm Association

**Context**: Verify the number appears in settings as added, even unverified.

Check the mobile settings; the number should be listed, confirming the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-authentication]]
- [[mobile-verification]]
