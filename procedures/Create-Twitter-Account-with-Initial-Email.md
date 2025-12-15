---
tags:
  - account-creation
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 74dab340-068f-4297-91f8-333eb57493ba
created_at: '2025-12-14T17:33:06.129Z'
updated_at: '2025-12-14T17:33:06.129Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Twitter-Account-with-Initial-Email

## Summary

This procedure sets up a new Twitter account using an initial email address, serving as the foundation for testing password reset vulnerabilities.

## Description

In the context of exploiting Twitter's password reset flaw, this step creates a controlled account with email abcd@x.com to mimic a victim's initial setup. It requires no prior access and focuses on registration via the web interface. Expected outcome is a fully registered account ready for further manipulation.

## Requirements

1. Access to email account abcd@x.com
2. Web browser with internet connection
3. Basic knowledge of Twitter registration

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from suspicious IPs
- Implement CAPTCHA on registration to deter automation

## Objectives

1. Establish baseline account for vulnerability testing
2. Verify email association
3. Prepare for reset link generation

## Instructions

### Step 1: Navigate to Registration

**Context**: Begin the account creation process on Twitter's signup page.

Access https://twitter.com/signup and enter details including email abcd@x.com, a username, and password.

> Upon submission, Twitter sends a verification email if required.

### Step 2: Verify Email

**Context**: Confirm the email to activate the account.

Check abcd@x.com for the verification link and click it to complete setup.

> Successful verification grants dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[twitter]]
