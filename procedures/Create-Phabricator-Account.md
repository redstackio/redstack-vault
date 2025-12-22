---
tags:
  - phabricator
  - account-creation
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
updated_at: '2025-12-14T17:31:30.992Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: eeff1080-b18a-4ba6-a45e-3124e8e56bbd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Phabricator-Account

## Summary

This procedure outlines the creation of a new user account in Phabricator, serving as the initial setup for testing authentication vulnerabilities.

## Description

In the context of exploiting Phabricator's password reset flaw, creating an account establishes a baseline for subsequent steps like requesting resets and changing emails. The target environment is a Phabricator web instance, and the outcome is a fully registered account with email verification. Prerequisites include access to a unique email address (e.g., a@x.com) and no existing account on the target.

## Requirements

1. Direct web access to the Phabricator instance
2. Valid, unique email address for registration
3. No prior account conflicts

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation to prevent abuse
- Monitor for unusual registration patterns from single IPs
- Require CAPTCHA on registration forms

## Objectives

1. Establish a testable account
2. Verify email integration
3. Prepare for reset token generation

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the account creation interface to input details.

No specific command; use the web browser to visit the Phabricator signup page (typically /account/register/ or similar).

> Fill in username, password, and email a@x.com, then submit.

### Step 2: Verify Email

**Context**: Confirm the account via email to activate it.

Check the inbox for a@x.com and click the verification link.

> Expected: Account activated, login enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[account-creation]]
