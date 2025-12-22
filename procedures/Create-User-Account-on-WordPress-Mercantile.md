---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - account-creation
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T03:47:12.722Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-User-Account-on-WordPress-Mercantile

## Summary

This procedure registers a new user account on the WordPress Mercantile site, providing access to editable profile sections necessary for subsequent injection attacks.

## Description

In the context of exploiting AngularJS template injection, creating an account is the initial step to gain authenticated access to user-editable fields like addresses. The Mercantile plugin on WordPress allows public registration, making this straightforward. Expected outcome is a functional account for testing injections without administrative privileges.

## Requirements

1. Access to https://mercantile.wordpress.org/
2. Valid email address for registration
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Require CAPTCHA on registration to prevent automated account creation
- Monitor for unusual registration patterns from single IPs

## Objectives

1. Gain authenticated access to /my-account/
2. Enable editing of billing and shipping addresses
3. Set up for template injection testing

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the public signup endpoint to initiate account creation.

No specific command; manually visit https://mercantile.wordpress.org/ and click the registration link or form.

> Fill in required fields: username, email, password. Submit the form.

### Step 2: Complete Registration

**Context**: Submit details and confirm via email if required.

Log in after registration to verify access.

> Expected: Redirect to dashboard or /my-account/ with user session active.

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
- [[wordpress]]
