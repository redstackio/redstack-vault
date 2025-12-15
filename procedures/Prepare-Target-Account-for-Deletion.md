---
id: proc-uuid-001
tags:
  - csrf
  - web
  - account-creation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.930Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Target-Account-for-Deletion

## Summary

This procedure sets up a test user account in the target web application to explore the account deletion functionality, confirming the presence of a vulnerable endpoint for subsequent CSRF exploitation.

## Description

In the context of testing a U.S. Department of Defense web application, this involves registering a new account, logging in, and initiating the deletion process to observe the request flow. It requires public registration access and serves as the foundation for capturing vulnerable requests. Expected outcome is visibility into the profile deletion UI without actual deletion during preparation.

## Requirements

1. Access to the target web application's registration page (e.g., https://█████)
2. Valid email or credentials for account creation
3. Browser configured for proxying (e.g., Burp Suite)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation to prevent abuse
- Log all registration and profile access attempts for anomaly detection
- Use CAPTCHA on registration to deter automated testing

## Objectives

1. Establish a controllable test account for vulnerability probing
2. Verify deletion endpoint accessibility
3. Prepare for request interception without alerting defenses

## Instructions

### Step 1: Create Test Account

**Context**: Register a new account to gain authenticated access to the profile section.

Navigate to the account creation page and submit the form with test details.

**Expected Output**: Confirmation email or success message; ability to log in.

### Step 2: Access Profile and Initiate Deletion

**Context**: Log in and trigger the deletion flow to expose the vulnerable button and confirmation.

Click on the profile section, locate the 'DELETE ACCOUNT' button, and enter 'YES' in the confirmation input.

**Expected Output**: Deletion prompt appears; do not submit to avoid early deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[account-creation]]
