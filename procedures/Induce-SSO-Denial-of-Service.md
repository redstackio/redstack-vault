---
tags:
  - sso
  - dos
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ab85aaa4-f410-4736-8e84-cd0e89822213
created_at: '2025-12-11T03:47:39.566Z'
updated_at: '2025-12-11T03:47:39.566Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0005]]'
mitre_techniques:
  - '[[T1550]]'
---
# Induce SSO Denial of Service

## Summary

This procedure triggers a denial of service on the legitimate SSO by exploiting the entityId conflict after propagation.

## Description

After waiting for changes to take effect, attempting login to the original account results in failure due to the duplicate entityId with space. This affects any organization's SSO, preventing logins. The environment is web-based Grammarly services.

## Requirements

1. Malicious account already registered (from previous procedure).
2. Access to legitimate account login page.
3. Patience for 2-minute propagation delay.

## Defense

Defensive measures and detection strategies:

- Monitor SSO login failures for patterns.
- Validate entityIds strictly during registration.

## Objectives

1. Cause authentication failure.
2. Demonstrate DoS impact.
3. Prepare for provisioning step.

## Instructions

### Step 1: Wait for Propagation

**Context**: Allow time for the malicious entityId to propagate in Grammarly's systems.

Wait 2 minutes after registration.

> No active steps; time-based.

### Step 2: Attempt Login

**Context**: Test login to observe error.

Try SSO login to the legitimate account; note the error.

> Expect authentication conflict error.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #dos
- #sso
