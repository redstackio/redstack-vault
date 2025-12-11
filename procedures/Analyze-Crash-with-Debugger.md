---
tags:
  - debugging
  - crash-analysis
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/Immunity-Debugger]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-steam-serverinfo-exploit]]'
platforms:
  - Windows
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: 0e208ed6-7cf6-4d79-960b-fc36a4f17ce4
created_at: '2025-12-11T06:10:40.336Z'
updated_at: '2025-12-11T06:10:40.336Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Analyze Crash with Debugger

## Summary

This procedure uses Immunity Debugger to analyze crashes in Steam.exe caused by buffer overflows, identifying exploit paths.

## Description

Attach the debugger to Steam.exe, trigger the crash via malicious UDP response, and inspect the stack to note the overflow in serverbrowser and absence of canaries.

## Requirements

1. Immunity Debugger installed
2. Steam.exe running
3. Malicious UDP server active

## Defense

Defensive measures and detection strategies:

- Enable stack canaries and DEP
- Use automated crash reporting tools

## Objectives

1. Confirm buffer overflow vulnerability
2. Map stack layout for exploitation
3. Identify ROP gadget opportunities

## Instructions

### Step 1: Attach Debugger

**Context**: Launch and attach Immunity Debugger to Steam.exe.

> Run Immunity Debugger and select Steam.exe process.

### Step 2: Trigger and Inspect Crash

**Context**: Send malicious payload and analyze in debugger.

> View modules, base addresses, and stack trace.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Immunity-Debugger]]

## Tags

- debugging
- crash-analysis
