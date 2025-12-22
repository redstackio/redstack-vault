---
tags:
  - dos
  - sso
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Network Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 602980d6-a7f5-42d1-a2e8-c606f7a401ac
created_at: '2025-12-13T09:01:26.867Z'
updated_at: '2025-12-13T09:01:26.867Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Induce DoS on SSO Login

## Summary

This procedure triggers a denial of service on the legitimate organization's SSO by attempting logins after duplicate entityId propagation.

## Description

After a short wait for changes to propagate, login attempts to the original account fail due to the prioritized spaced entityId. This exploits the mismatch in trimming logic, targeting Grammarly's provisioning system.

## Requirements

1. Previously created duplicate entityId account
2. Access to legitimate account credentials
3. Network access to Grammarly

## Defense

Defensive measures and detection strategies:

- Monitor login failure rates for DoS patterns
- Validate entityId uniqueness strictly

## Objectives

1. Cause login failures
2. Deny access to legitimate users
3. Confirm DoS impact

## Instructions

### Step 1: Wait for Propagation

**Context**: Allow time for entityId changes to take effect.

Wait approximately 2 minutes after creating the duplicate account.

> Propagation is typically quick.

### Step 2: Attempt Login

**Context**: Test login to induce error.

Try logging into the legitimate account, observing the resulting error.

> This confirms the DoS condition.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[dos]]
- [[sso]]
