---
tags:
  - dos
  - assertion-failure
  - mruby
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Application or System Exploitation]]'
id: 23283c7f-13c3-42c7-8a6b-00a3bdb3fd95
created_at: '2025-12-11T03:47:48.074Z'
updated_at: '2025-12-11T03:47:48.074Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
---
# Initialize Decimal with Itself for Crash

## Summary

This procedure calls the initialize method on an existing mruby Decimal object, passing the object itself as the argument, which triggers an assertion failure and program crash for denial of service.

## Description

The vulnerability in mruby-mpdecimal's Decimal.initialize method occurs when the object is initialized with itself, creating an empty mpd_t structure. Subsequent calls like to_s access this structure, failing an assertion in mpd_msword. This leads to SIGABRT and application crash, impacting availability in mruby-based applications.

## Requirements

1. Existing Decimal object from prior instantiation
2. Running in mirb shell on Linux
3. Unpatched mruby-mpdecimal library

## Defense

Defensive measures and detection strategies:

- Patch mruby-mpdecimal to return self on self-initialization
- Monitor for SIGABRT signals in mruby processes

## Objectives

1. Trigger assertion failure in Decimal.initialize
2. Cause denial of service crash
3. Confirm exploit via process termination

## Instructions

### Step 1: Call Initialize with Self

**Context**: With an existing Decimal object 'a', call initialize passing 'a' to exploit the vulnerability.

**Command** ([[commands/decimal-initialize-self]]):
```bash
a.initialize a
```

> This command passes the instance as the argument, creating an empty mpd_t and triggering the assertion during to_s access.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[Application or System Exploitation]]

## Commands Used

- [[commands/decimal-initialize-self]]

## Tools Used

- #mirb

## Tags

- #dos
- #assertion-failure
- [[procedures/Create-mruby-Decimal-Object]]
