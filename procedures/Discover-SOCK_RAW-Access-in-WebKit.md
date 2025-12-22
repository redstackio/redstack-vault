---
tags:
  - ps4
  - webkit
  - sock-raw
  - privilege-management
type: procedure
tools:
  - '[[tools/poc.c]]'
  - '[[tools/ps4.c]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - PS4
  - FreeBSD
techniques:
  - '[[procedures/Trigger-Double-Free-for-Privilege-Escalation]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6094974d-aaae-48ff-a2a3-9737c60ad98f
created_at: '2025-12-11T03:47:39.444Z'
updated_at: '2025-12-11T03:47:39.444Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Discover SOCK_RAW Access in WebKit

## Summary

This procedure identifies the ability to open SOCK_RAW sockets from the WebKit process on PS4 without root privileges, enabling raw packet manipulation for further exploitation.

## Description

On PS4, the WebKit process unexpectedly allows creation of SOCK_RAW sockets, contrary to standard FreeBSD requirements. This improper privilege management provides unprivileged access to raw IPv6 packet sending, setting the stage for kernel vulnerability exploitation.

## Requirements

1. Access to PS4 WebKit process
2. Development environment for testing socket creation
3. No root privileges needed

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected SOCK_RAW socket creations in non-privileged processes
- Patch kernel to enforce proper privilege checks for raw sockets

## Objectives

1. Confirm SOCK_RAW access without root
2. Enable raw packet sending for exploitation
3. Prepare for IPv6 packet crafting

## Instructions

### Step 1: Attempt Socket Creation

**Context**: Test opening a SOCK_RAW socket in the WebKit context.

Use standard socket API calls in C code running in WebKit to create SOCK_RAW for IPv6.

> Expected: Successful socket creation without permission denial.

### Step 2: Verify Functionality

**Context**: Send a test packet to confirm raw access.

Attempt to send a benign IPv6 packet to loopback.

> Expected: Packet sent without errors, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[procedures/Trigger-Double-Free-for-Privilege-Escalation]]

### Sub-Techniques

## Commands Used

## Tools Used

## Tags

- [[tools/ps4.c]]
- #webkit
- #sock-raw
