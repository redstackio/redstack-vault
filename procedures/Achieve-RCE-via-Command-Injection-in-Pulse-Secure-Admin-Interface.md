---
tags:
  - command-injection
  - rce
type: procedure
tools:
  - '[[tools/download.py]]'
  - '[[tools/GPU]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - SSL VPN
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: c16f8806-9eaf-43ff-a01e-fe7260a13085
created_at: '2025-12-11T03:47:59.566Z'
updated_at: '2025-12-11T03:47:59.566Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Achieve RCE via Command Injection in Pulse Secure Admin Interface

## Summary

This procedure exploits CVE-2019-11539 for remote code execution by cracking admin hashes or capturing logins, then injecting commands in the admin interface.

## Description

After accessing the admin interface, use GPU-accelerated cracking on hashes from downloaded files or wait for admin login capture to gain credentials, then trigger command injection for RCE.

## Requirements

1. Access to admin interface
2. Downloaded files with admin hashes
3. GPU for hash cracking

## Defense

Defensive measures and detection strategies:

- Patch CVE-2019-11539 and use input sanitization
- Monitor admin logs for injection attempts

## Objectives

1. Crack or capture admin credentials
2. Execute arbitrary commands
3. Achieve full system compromise

## Instructions

### Step 1: Crack Admin Hash

**Context**: Use [[tools/GPU]] to crack hashes from files.

### Step 2: Trigger Injection

**Context**: Inject commands in admin features.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GPU]]

## Tags

- #command-injection
- #rce
