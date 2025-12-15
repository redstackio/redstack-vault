---
tags:
  - uac-bypass
  - elevation
type: procedure
tools:
  - '[[tools/cmd-exe]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Bypass User Account Control]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b5066f2c-ded5-4f91-8df6-56fd204161b3
created_at: '2025-12-14T17:29:44.277Z'
updated_at: '2025-12-14T17:29:44.277Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# Complete Repair and Handle UAC

## Summary

This procedure allows the MSI repair to finish, handling the UAC prompt to ensure the elevated MsiExec.exe loads the hijacked DLL without additional user interaction, achieving escalation.

## Description

During repair, MsiExec.exe requests elevation via UAC. By denying the prompt, the process continues under the original context but loads the DLL elevated due to auto-elevation behavior, executing the malicious code as SYSTEM.

## Requirements

1. Malicious DLL in place
2. UAC enabled but deniable
3. No interruption to MsiExec process

## Defense

Defensive measures and detection strategies:

- Enable UAC secure desktop
- Log UAC prompts and denials
- Patch MSI auto-elevation vulnerabilities

## Objectives

1. Complete the repair process
2. Bypass UAC interaction
3. Trigger DLL load for escalation

## Instructions

### Step 1: Monitor Repair Progress

**Context**: Wait for the process to advance to DLL loading.

Use Task Manager or cmd to watch MsiExec.exe; no command needed.

> Process CPU usage spikes briefly; UAC may prompt after DLL creation.

### Step 2: Handle UAC Prompt

**Context**: Deny elevation to proceed seamlessly.

When UAC appears, select 'No'; the repair continues, loading the DLL.

> Expected: Elevated cmd.exe spawns automatically if payload succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/cmd-exe]]

## Tags

- [[uac-bypass]]
- [[elevation]]
