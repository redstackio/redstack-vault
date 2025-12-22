---
tags:
  - 2fa-bypass
  - session-hijacking
type: procedure
tools:
  - '[[tools/download.py]]'
  - '[[tools/GPU]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - SSL VPN
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cc58ca60-78c0-468f-87b3-190326eb2ec5
created_at: '2025-12-11T03:47:59.572Z'
updated_at: '2025-12-11T03:47:59.572Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Bypass Two-Factor Authentication in Pulse Secure VPN

## Summary

This procedure bypasses Duo 2FA in Pulse Secure VPN by using extracted integration keys or reusing active sessions from downloaded data.

## Description

Two methods are used: extracting Duo keys (integration key, secret key, API hostname) from system files to simulate 2FA, or hijacking sessions from .mdb files when Roaming Session is disabled (CVE-2019-11540).

## Requirements

1. Extracted files containing Duo keys or session data
2. Access to VPN login endpoint
3. Knowledge of session management in Pulse Secure

## Defense

Defensive measures and detection strategies:

- Enable Roaming Session and monitor for session reuse attempts
- Secure 2FA key storage and use anomaly detection

## Objectives

1. Gain authenticated VPN access without 2FA
2. Access internal resources
3. Prepare for admin interface exploitation

## Instructions

### Step 1: Extract Duo Keys

**Context**: Parse /data/runtime/mtmp/system for keys.

### Step 2: Simulate 2FA or Reuse Session

**Context**: Use keys to bypass or inject session from /data/runtime/mtmp/lmdb/randomVal/data.mdb.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #2fa-bypass
- #session-hijacking
