---
id: 50c4bfc7-18bd-44a4-a2b2-9df052c30963
name: Bypass 2FA and Restrictions Using Embedded Submission Form
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:39.301Z'
updated_at: '2025-12-11T03:47:39.301Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - authorization-bypass
  - web-vulnerability
  - hackerone
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---

# Bypass 2FA and Restrictions Using Embedded Submission Form

## Summary

This procedure exploits an authorization bypass in HackerOne's embedded submission form to submit reports without enforcing 2FA, rate limits, or reporter blacklists, allowing unauthorized report creation.

## Description

The vulnerability stems from the use of the interact_without_authorization method in the embedded endpoint, which skips ACL checks. This allows hackers to bypass program requirements by using the alternative submission path. The target environment is the HackerOne web platform built on Ruby on Rails, and successful execution results in report submission without restrictions.

## Requirements

1. Valid HackerOne account
2. Access to a web browser
3. Knowledge of the target program's embedded submission URL

## Defense

Defensive measures and detection strategies:

- Implement consistent ACL checks across all submission endpoints
- Monitor for anomalous submission patterns, such as repeated attempts without 2FA

## Objectives

1. Submit reports bypassing security restrictions
2. Evade blacklists and rate limits
3. Confirm unauthorized access to submission functionality

## Instructions

### Step 1: Disable 2FA on Account

**Context**: Access account settings to remove two-factor authentication enforcement.

Navigate to account settings and disable 2FA.

### Step 2: Test Standard Submission

**Context**: Verify the block on the standard form due to missing 2FA.

Navigate to https://hackerone.com/parrot_sec and attempt to submit a report, observing the restriction.

### Step 3: Retrieve Embedded URL

**Context**: Obtain the alternative submission endpoint from the program policy.

Extract the URL like https://hackerone.com/0a1e1f11-257e-4b46-b949-c7151212ffbb/embedded_submissions/new.

### Step 4: Submit via Embedded Form

**Context**: Use the form to bypass checks and submit the report.

Fill out and submit the form, confirming successful creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #authorization-bypass
- #web-vulnerability
