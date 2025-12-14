---
tags:
  - aws
  - session
  - timeout
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.704Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 232fb979-8728-4715-bc33-8a2ae7bb36f6
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Wait-for-AWS-Session-Timeout

## Summary

This procedure simulates an unattended session by waiting for the AWS Management Console's configured timeout to expire, creating the condition for the session bypass exploit.

## Description

AWS session timeouts are policy-driven (e.g., via IAM Identity Center settings, default 12 hours idle). This step involves idling the session until expiration, after which the console requires re-auth but the Access Portal does not, due to inconsistent enforcement. It's a passive step but critical for the attack scenario.

## Requirements

1. Active AWS Management Console session from prior login
2. Knowledge of timeout duration (check AWS console settings or assume default)
3. Patient observation or automated idle simulation

## Defense

Defensive measures and detection strategies:

- Configure uniform timeouts across console and portal
- Use session revocation APIs in IAM Identity Center
- Log and alert on long-idle sessions via CloudWatch

## Objectives

1. Expire the console session
2. Maintain browser state for portal test
3. Validate timeout enforcement in console

## Instructions

### Step 1: Idle the Session

**Context**: Prevent any user interaction to trigger idle timeout.

Close or minimize the console tab and wait the configured period (e.g., 8-24 hours).

> Use a timer or script to track time; avoid mouse/keyboard activity on the tab.

### Step 2: Verify Expiration

**Context**: Confirm the session has timed out.

Reopen the console tab and attempt navigation (e.g., to S3 or EC2).

> Expect a redirect to SSO login or error: 'Your session has expired'. Check cookies for invalidation.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[timeout]]
- [[idle-session]]
