---
tags:
  - phabricator
  - email-change
  - account-manipulation
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
updated_at: '2025-12-14T17:31:30.987Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f72e9d71-92f9-4492-a52f-7aac875ed41b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Phabricator-Email-Address

## Summary

This procedure modifies the email associated with a Phabricator account, which should invalidate prior reset tokens but does not due to the vulnerability.

## Description

In the attack, after requesting a reset, the user logs in and updates the email to b@x.com, verifying it and removing the old one. This tests the system's failure to expire old tokens. Target environment: Phabricator settings page; outcome: Updated email without token invalidation. Prerequisites: Valid login credentials.

## Requirements

1. Active login session
2. Access to new email (b@x.com) for verification
3. Web access to account settings

## Defense

Defensive measures and detection strategies:

- Automatically invalidate all pending tokens on email changes
- Require re-authentication for sensitive changes like email
- Audit logs for email updates and correlate with reset activity

## Objectives

1. Alter account email
2. Verify the change
3. Expose token persistence flaw

## Instructions

### Step 1: Log In

**Context**: Gain access to settings.

Use original credentials to log into Phabricator.

> Expected: Dashboard access.

### Step 2: Update Email

**Context**: Change to new address.

Go to account settings, enter b@x.com as new email, and submit.

> Expected: Verification email sent to b@x.com.

### Step 3: Verify and Remove Old

**Context**: Complete the change.

Click verification link in b@x.com email, then remove a@x.com if listed.

> Expected: Email updated successfully.

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
- [[email-change]]
- [[account-manipulation]]
