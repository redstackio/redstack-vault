---
tags:
  - shopify
  - email-change
  - session
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T17:28:58.533Z'
sub_techniques: []
id: 14cb81cb-f5de-4451-af7b-0e06e6283063
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Change-Shopify-Account-Email-Address

## Summary

This procedure updates the primary email address on a Shopify account, which is a prerequisite for demonstrating session persistence vulnerabilities where existing admin sessions are not invalidated.

## Description

In Shopify's authentication system, changing the account email does not trigger immediate session revocation. This allows testing for insufficient session expiration by simulating a credential update while maintaining active sessions tied to the old email. The procedure targets accounts managing multiple stores and uses a standard web browser to perform the change, confirming the update without disrupting ongoing access.

## Requirements

1. Valid Shopify account login credentials
2. Access to a new email address for verification
3. [[tools/Firefox]] browser for isolated session management

## Defense

Defensive measures and detection strategies:

- Implement immediate session invalidation on email changes
- Monitor for anomalous logins from old credentials post-change
- Enforce multi-factor authentication (MFA) for all session revocations

## Objectives

1. Update the Shopify account's primary email
2. Verify the change takes effect
3. Set up conditions for testing session persistence

## Instructions

### Step 1: Navigate to Account Settings

**Context**: Log in to the Shopify admin and access the profile settings to initiate the email change.

Use [[tools/Firefox]] to open the Shopify dashboard, go to Account Settings > Profile, and enter the new email address. Submit the form to request verification.

### Step 2: Confirm the Change

**Context**: Complete the verification process to finalize the email update.

Check the new email inbox for the confirmation link from Shopify and click it to activate the new address as primary.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- shopify
- email-change
