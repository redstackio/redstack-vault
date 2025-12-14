---
id: proc-create-account-concretecms
tags:
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:11.160Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Account-in-Concrete-CMS

## Summary

This procedure outlines registering a new user account in Concrete CMS to set up the environment for testing authentication vulnerabilities.

## Description

In the context of exploiting Concrete CMS authentication flaws, creating a test account provides the necessary foothold. The registration process is standard for web-based CMS platforms, requiring basic user details and email verification. This step is prerequisite for generating and testing password reset tokens.

## Requirements

1. Access to a Concrete CMS instance with user registration enabled
2. Valid email address for account verification
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Require CAPTCHA on registration to prevent automated account creation
- Monitor for unusual registration spikes from single IPs
- Implement email verification delays

## Objectives

1. Establish a controllable test account
2. Enable subsequent authentication testing
3. Confirm platform accessibility

## Instructions

### Step 1: Navigate to Registration

**Context**: Locate and access the user signup form.

**Instructions**: Open the Concrete CMS login page and click the 'Register' or 'Sign Up' link. Fill in required fields: username, email, password.

> Submit the form to complete registration. Expect an email confirmation if required.

### Step 2: Verify Account

**Context**: Ensure the account is active.

**Instructions**: Check your email for a verification link and click it, or attempt login immediately if no verification is needed.

> Successful login confirms account creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[web]]
