---
tags:
  - proxy-access
  - internal-pivoting
type: procedure
tools:
  - '[[tools/download.py]]'
  - '[[tools/GPU]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - SSL VPN
techniques:
  - '[[Remote Services]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4a81aa5a-8219-4ec6-8233-c381f5baa0ec
created_at: '2025-12-11T03:47:59.569Z'
updated_at: '2025-12-11T03:47:59.569Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0005]]'
mitre_techniques:
  - '[[T1021]]'
---
# Access Admin Interface via VPN Web Proxy

## Summary

This procedure uses the VPN's web proxy to access the internal admin interface after authentication, enabling further exploits like command injection.

## Description

After logging in, the proxy allows navigation to https://0/admin/, bypassing external restrictions and chaining to post-auth vulnerabilities like CVE-2019-11539.

## Requirements

1. Authenticated VPN session
2. Web browser or proxy tool
3. Knowledge of admin endpoint

## Defense

Defensive measures and detection strategies:

- Restrict proxy access to admin interfaces
- Monitor internal traffic for anomalous admin access

## Objectives

1. Reach admin interface
2. Set up for RCE exploitation
3. Gain deeper system access

## Instructions

### Step 1: Log In to VPN

**Context**: Use extracted credentials to authenticate.

### Step 2: Navigate via Proxy

**Context**: Access https://0/admin/ through the VPN proxy.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Remote Services]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #proxy-access
- #internal-pivoting
