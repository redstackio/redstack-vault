---
tags:
  - authentication-bypass
  - retesting
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3d8d3d0c-7849-4258-875e-aa846ace50e3
created_at: '2025-12-11T06:10:40.129Z'
updated_at: '2025-12-11T06:10:40.129Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Retest Email Confirmation Fix

## Summary

This procedure involves retesting the fix for a previous email confirmation bypass vulnerability in Shopify, verifying that email confirmations cannot be received and integrations across stores or partners are blocked.

## Description

In this procedure, the attacker retests the remediation applied to a prior vulnerability (report #791775) by attempting to trigger email changes and observing system behavior. The goal is to confirm if the fix effectively prevents bypasses, such as blocking unverified changes and integrations. This is done in the context of Shopify's web-based user account management, targeting myshop.myshopify.com. Expected outcomes include identifying any remaining gaps that could lead to further exploitation.

## Requirements

1. Access to a Shopify user account
2. Web browser for interacting with myshop.myshopify.com
3. Knowledge of the previous vulnerability technique

## Defense

Defensive measures and detection strategies:

- Implement strict email verification timeouts and ownership checks
- Monitor for rapid email change attempts in user logs

## Objectives

1. Verify effectiveness of the previous fix
2. Identify potential bypass opportunities
3. Document system behavior for escalation

## Instructions

### Step 1: Initiate Email Change Test

**Context**: Attempt to change the email address to test if the system blocks unverified actions.

Navigate to account settings on myshop.myshopify.com and submit an email change request. Observe if the change is pending verification.

> Expected: System requires verification email to original address before proceeding.

### Step 2: Check Integration Blocking

**Context**: Test if cross-store or partner integrations are blocked post-fix.

Attempt to access or integrate with other stores/partners without completing verification. Confirm if the system prevents such actions.

> Expected: Integrations blocked until verification is complete.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- authentication-bypass
- retesting
- shopify
