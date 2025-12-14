---
tags:
  - account-ban
  - hackerone
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
updated_at: '2025-12-14T17:32:48.474Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 7852eaf2-72d0-43ed-99da-fca5f69c24e0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Ban-HackerOne-Test-Account

## Summary

This procedure simulates the banning of a HackerOne test account to trigger deletion, setting the stage for testing unrevoked API token access.

## Description

Contact HackerOne support to request a permanent ban on the test account. The account is deleted after processing, provided there are no pending payouts. This step assumes the tester has coordinated with HackerOne for vulnerability disclosure. The outcome is a banned/deleted account status, but with the API token still potentially active due to the flaw.

## Requirements

1. Active test account with generated token
2. Contact details for HackerOne support
3. No outstanding payments or reports on the account

## Defense

Defensive measures and detection strategies:

- Automate token revocation on ban events
- Audit banned account access logs
- Notify users of token invalidation post-ban

## Objectives

1. Permanently ban and delete the test account
2. Confirm web access is revoked
3. Prepare for API exploitation validation

## Instructions

### Step 1: Request Ban

**Context**: Submit a ban request to HackerOne support, explaining it's for testing.

Use the support form at https://hackerone.com/support or email, specifying the test account username 'mrtst'.

> Expect approval and confirmation email.

### Step 2: Wait for Processing and Verify Ban

**Context**: Allow time for the ban to process and account deletion.

Attempt web login; it should fail.

> Account shows as deleted or inaccessible via web, but API testing follows in next procedure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-ban
- hackerone
