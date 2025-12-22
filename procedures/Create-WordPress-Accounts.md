---
tags:
  - wordpress
  - account-creation
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
impact_level: medium
detection_risk: low
sub_techniques: []
id: dd72f92f-e034-49dd-acbe-1c92fe5dc6d7
created_at: '2025-12-13T09:01:26.553Z'
updated_at: '2025-12-13T09:01:26.553Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create WordPress Accounts

## Summary

This procedure creates a verified and an unverified account on WordPress.com to exploit the invitation-based verification bypass.

## Description

The verified account is used to send invitations, while the unverified one with the target email is manipulated to gain verification without owning the email.

## Requirements

1. Personal email for verification
2. Target email address
3. Web browser

## Defense

Defensive measures and detection strategies:

- Monitor for suspicious account creations on WordPress.com
- Implement stricter email verification processes

## Objectives

1. Establish a verified account for invitations
2. Create unverified account with target email
3. Set up for verification bypass

## Instructions

### Step 1: Create Verified Account

**Context**: Set up a confirmed account.

Create account A with personal email and confirm it via email link.

> Account is fully verified.

### Step 2: Create Unverified Account

**Context**: Set up the target account without confirmation.

Create account B with something@company.com.

> Account is created but remains unverified.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[wordpress]]
- [[account-creation]]
