---
id: proc-uuid-1
tags:
  - csrf
  - account-creation
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.130Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Fake-Account-and-Change-Email-to-Generate-Confirmation-Link

## Summary

This procedure involves creating a disposable account on a web platform like HackerOne and initiating an email change to an attacker-controlled address, generating a CSRF-vulnerable confirmation link that can be used for subsequent exploitation.

## Description

In the context of a CSRF vulnerability in the email confirmation process, the attacker first registers a new account using minimal details. They then navigate to the account management section to request an email address change to one under their control. The platform sends a confirmation link to this new email, which directly processes the change upon access without CSRF tokens or session validation. This sets up the malicious link for phishing to victims, allowing forced authentication into the fake account. Prerequisites include access to a valid email service and basic knowledge of the target's registration flow.

## Requirements

1. Internet access to the target web platform
2. Control over an email address for receiving confirmations
3. No special privileges; open registration assumed

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints, including email confirmations
- Require re-authentication or session checks before processing confirmation links
- Monitor for unusual account creation patterns followed by rapid email changes

## Objectives

1. Establish a controlled fake account on the target platform
2. Generate a exploitable confirmation link lacking protections
3. Prepare for phishing delivery to victims

## Instructions

### Step 1: Register Fake Account

**Context**: Create a new account to serve as the impersonation vector.

Navigate to the target's registration page and provide arbitrary username, password, and initial email. Submit the form to complete signup.

> Upon success, the account dashboard should load, confirming registration.

### Step 2: Initiate Email Change

**Context**: Trigger the vulnerable confirmation process to obtain the malicious link.

Log into the new account, go to settings > account > change email, enter the attacker-controlled email, and submit. Check the controlled inbox for the confirmation email containing the link.

> The link will be in the format similar to https://target.com/confirm?token=abc123, directly actionable without further auth.

### Step 3: Extract and Validate Link

**Context**: Ensure the link is ready for distribution.

Copy the link from the email and test it in an incognito browser to verify it changes the email without errors or additional prompts.

> Successful test logs in or processes the change automatically, indicating CSRF vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[account-creation]]
