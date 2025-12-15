---
id: verify-email-takeover
tags:
  - verification
  - takeover-test
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:12.063Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Verify-Email-Change-and-Test-Takeover

## Summary

This procedure validates the success of the email change by checking account logs and testing sharing features to confirm attacker control over the taken-over account in Acronis File Sync & Share.

## Description

Post-modification, the attacker reviews logs to confirm the email update, which is isolated to File Sync & Share. Testing involves sharing files/folders to verify that invites now route to the new email, enabling impersonation and data access. If the victim tries to verify the email, they encounter an account creation error. This step assumes the modification succeeded and focuses on impact demonstration in the web environment.

## Requirements

1. Successful email change from prior step
2. Access to account logs and sharing interface
3. Control over the target unverified email inbox

## Defense

Defensive measures and detection strategies:

- Sync profile changes across all services and notify admins/users immediately
- Audit sharing activities for anomalies, like invites to new/unverified emails
- Implement email confirmation loops that alert on changes without user initiation
- Monitor for 'account not created' errors as potential takeover indicators

## Objectives

1. Confirm email update in logs
2. Demonstrate takeover via sharing invites
3. Highlight stealth and persistence

## Instructions

### Step 1: Check Account Logs

**Context**: Verify the email change is logged without alerting main profiles.

No specific command; navigate to https://mc-beta-cloud.acronis.com/fc/access#/log.

> Search for recent account update entries showing the new email. Absence in admin dashboard confirms isolation.

### Step 2: Test File Sharing

**Context**: Prove control by routing invites to attacker's email.

No specific command; from the dashboard, share a file or folder and enter the new email as recipient.

> The invite email arrives at the new address under attacker control. Attempt sharing to original email fails or routes incorrectly.

### Step 3: Simulate Victim Verification

**Context**: Test victim-side impact to ensure takeover locks them out.

No specific command; use the new email to attempt account creation or verification in Acronis.

> Victim sees 'This account has not been created yet' error, preventing recovery without admin intervention.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence
- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- log-review
- sharing-test
- persistence-check
