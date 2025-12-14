---
tags:
  - phabricator
  - password-reset
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:31:30.990Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: de2f7350-c62e-43ff-bfbb-65395c7fe63a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Request-Phabricator-Password-Reset-Link

## Summary

This procedure generates a password reset token in Phabricator without immediately using it, setting up for later exploitation.

## Description

The attack scenario involves logging out and requesting a reset to obtain a token-linked URL sent via email. This token persists even after email changes, enabling takeover. Target is Phabricator's reset endpoint; expected outcome is receipt of an unused reset link. Prerequisites: Existing account and email access.

## Requirements

1. Logged-in session to log out from
2. Access to the account's email (a@x.com)
3. Web access to login/reset page

## Defense

Defensive measures and detection strategies:

- Expire reset tokens quickly (e.g., 15 minutes)
- Log reset requests and alert on multiples from same IP
- Invalidate tokens on any account changes

## Objectives

1. Obtain a valid reset token
2. Ensure token is not consumed
3. Prepare for email manipulation

## Instructions

### Step 1: Log Out

**Context**: Ensure no active session interferes with reset.

Navigate to the logout option in Phabricator and log out.

> Expected: Redirect to login page.

### Step 2: Initiate Reset

**Context**: Trigger email with reset link.

On the login page, select 'Forgot Password' or similar, enter a@x.com, and submit.

> Expected: Email sent with reset URL (e.g., containing token).

### Step 3: Capture Link

**Context**: Store the link for later use without clicking.

Open the email in a@x.com and copy the reset URL without accessing it.

> Expected: Link saved securely.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[password-reset]]
