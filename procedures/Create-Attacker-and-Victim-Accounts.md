---
id: proc-765679-account-setup
tags:
  - account-creation
  - initial-access
type: procedure
tools:
  - '[[tools/Notepad]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:49.714Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Attacker-and-Victim-Accounts

## Summary

This procedure sets up two test accounts in the Outpost application to simulate an attacker-victim scenario for exploiting the stored XSS vulnerability.

## Description

In the context of testing the Outpost Inbox file upload, create an attacker account for uploading payloads and a victim account for receiving and interacting with them. This establishes the necessary environment without requiring existing access, using simple email-based registration. Expected outcomes include verified accounts ready for authentication and payload delivery.

## Requirements

1. Access to email services for verification (e.g., seq@seq.teamoutpost.com and seq1@seq1.teamoutpost.com)
2. Web browser for registration
3. No prior Outpost access needed

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from suspicious IPs
- Implement CAPTCHA on registration to prevent automation
- Rate-limit sign-ups to detect abuse

## Objectives

1. Establish controlled attacker access
2. Prepare victim profile for payload testing
3. Validate account functionality for Inbox interactions

## Instructions

### Step 1: Register Attacker Account

**Context**: Navigate to the Outpost registration page and create the attacker's account.

No specific command; use the web interface at https://app.outpost.co/sign-up, enter email seq@seq.teamoutpost.com, set a password, and complete verification.

> Successful registration redirects to login or dashboard; check email for confirmation.

### Step 2: Register Victim Account

**Context**: Repeat for the victim to simulate a target user.

Use the web interface to register seq1@seq1.teamoutpost.com with a password and verify via email.

> Account ready; no alerts or errors during creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Notepad]]

## Tags

- [[account-creation]]
- [[initial-access]]
