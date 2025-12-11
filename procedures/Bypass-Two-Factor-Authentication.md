---
tags:
  - 2fa-bypass
  - session-hijacking
type: procedure
tools:
  - '[[tools/download.py]]'
  - '[[tools/grep]]'
  - '[[tools/GPU]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - SSL VPN
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Web Session Cookie]]'
id: 6017eb14-6ffc-48d9-9df9-8dbb18dc08f6
created_at: '2025-12-11T06:10:40.282Z'
updated_at: '2025-12-11T06:10:40.282Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1550]]'
---
# Bypass Two-Factor Authentication

## Summary

This procedure uses extracted integration keys or reusable sessions to bypass Duo 2FA in Pulse Secure VPN, allowing unauthorized access.

## Description

By leveraging keys from configuration files or hijacking sessions from database files, attackers can authenticate without triggering 2FA, especially when Roaming Session is not enabled.

## Requirements

1. Extracted Duo keys or session data from files
2. Access to VPN login endpoint
3. Valid credentials from prior extraction

## Defense

Defensive measures and detection strategies:

- Enable Roaming Session and use secure session management
- Monitor for session reuse anomalies in logs

## Objectives

1. Gain authenticated access without 2FA
2. Enable post-auth exploitation
3. Access internal resources

## Instructions

### Step 1: Use Integration Keys for Bypass

**Context**: Apply extracted Duo keys to simulate valid 2FA.

Use the integration key, secret key, and API hostname from /data/runtime/mtmp/system to authenticate via the VPN login form.

### Step 2: Reuse Sessions

**Context**: Hijack existing sessions from database.

Extract and apply session data from /data/runtime/mtmp/lmdb/randomVal/data.mdb to log in without 2FA.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

- [[Web Session Cookie]]

## Commands Used



## Tools Used



## Tags

- [[2fa-bypass]]
- [[session-hijacking]]
