---
id: proc-uber-observe-001
tags:
  - sms-harassment
  - retry-mechanism
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - SMS Service
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:39.600Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Daily-Recurring-SMS-Floods

## Summary

This procedure monitors the target phone for the system's automated daily retries of undelivered queued SMS invitations, resulting in non-stop spam floods until manually stopped.

## Description

Uber's backend includes a retry mechanism that re-attempts sending queued messages daily (e.g., 9:30 AM IST), splitting each into three parts for 60 SMS per batch. Without strong opt-out, this perpetuates harassment from the initial queuing. Applicable to web-initiated SMS services; outcomes include ongoing privacy invasion, legal risks under DND regs, and costs for international/roaming users.

## Requirements

1. Prior successful queuing and initial trigger
2. Access to monitor the target phone number
3. Knowledge of system's retry schedule (daily batches)

## Defense

Defensive measures and detection strategies:

- Limit retry attempts to 1-2 per invitation with exponential backoff
- Auto-expire undelivered queues after 24-48 hours
- Integrate DND checks before sending retries
- Provide easy support escalation for spam reports

## Objectives

1. Validate persistent daily flooding behavior
2. Assess long-term impact of unstopped spam
3. Identify opt-out weaknesses (e.g., 'STOP' reply or support contact)

## Instructions

### Step 1: Monitor for First Retry Batch

**Context**: Wait for the scheduled retry time and check the target for incoming floods.

**Command** ():
```bash
# No command required; use phone logs or SMS app to observe
# Expected time: Next day at 9:30 AM IST
```

> Target receives 60 SMS parts daily. Success if floods recur without further input.

### Step 2: Test Opt-Out Mechanisms

**Context**: Attempt to halt the spam to confirm enforcement gaps.

**Command** ():
```bash
# From target phone: Reply 'STOP' to one of the SMS messages
# Alternatively: Contact Uber support via app or email
```

> Floods stop only on successful opt-out or intervention. Expected output: Confirmation of manual stop requirement.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sms-harassment
- retry-mechanism
