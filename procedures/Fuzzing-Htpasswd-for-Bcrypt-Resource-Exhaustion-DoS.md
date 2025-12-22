---
tags:
  - dos
  - bcrypt
  - resource-exhaustion
  - htpasswd
type: procedure
tools:
  - '[[tools/American-Fuzzy-Lop-AFL]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:31.100Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: ecb38fdf-cd60-4896-9ae0-fd3c1897edc5
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Fuzzing Htpasswd for Bcrypt Resource Exhaustion DoS

## Summary

This procedure fuzzes Apache htpasswd with AFL to find high bcrypt cost factors (e.g., 31) causing prolonged computations, leading to server DoS even after connection closure.

## Description

Htpasswd lacks cost limits, allowing $2y$31$ hashes to take 30+ hours per login. Fuzz input hashes to trigger. Targets auth systems on Linux.

## Requirements

1. Htpasswd binary
2. AFL fuzzer
3. Seed hashes with varying costs
4. Vulnerable Apache setup

## Defense

Defensive measures and detection strategies:

- Cap bcrypt cost at 12-14
- Timeout auth attempts
- Rate limit logins

## Objectives

1. Set high cost in hash
2. Exhaust CPU for hours
3. DoS server processes

## Instructions

### Step 1: Fuzz Htpasswd with AFL

**Context**: Target hash computation.

**Command** (AFL):
Run afl-fuzz on htpasswd -nbm with seed inputs.

> Finds cost=31; hangs for days.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- None extracted

## Tools Used

- [[tools/American-Fuzzy-Lop-AFL]]

## Tags

- bcrypt-dos
- auth-fuzzing
