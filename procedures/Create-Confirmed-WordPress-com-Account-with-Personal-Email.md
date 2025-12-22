---
tags:
  - account-creation
  - wordpress-com
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
updated_at: '2025-12-14T17:31:42.768Z'
sub_techniques: []
id: a69508ca-9ca5-4d27-9f6d-52dfcee7f32e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Confirmed-WordPress-com-Account-with-Personal-Email

## Summary

This procedure registers and verifies a personal WordPress.com account that the attacker controls, used later to send invitations.

## Description

WordPress.com requires email confirmation for full account functionality. This controlled account allows the attacker to invite other emails, exploiting the verification flaw. The process is standard registration but ensures verification to gain invitation privileges.

## Requirements

1. Access to the attacker's personal email
2. Web browser
3. No prior WordPress.com account

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from suspicious IPs
- Implement CAPTCHA on registrations
- Rate-limit invitation sends

## Objectives

1. Establish a verified attacker account
2. Gain ability to send invites
3. Prepare for verification bypass

## Instructions

### Step 1: Register Account

**Context**: Start the signup process.

Visit wordpress.com/signup, enter personal email, username, and password, then submit.

> Confirmation email is sent to the personal inbox.

### Step 2: Verify Email

**Context**: Complete verification to activate the account.

Open the confirmation email and click the link inside.

> Account dashboard loads, showing verified status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- wordpress-com
