---
tags:
  - debugging
  - windbg
  - process-attachment
type: procedure
tools:
  - '[[tools/WinDBG]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:08.819Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5465a4bd-914c-4b43-9d1b-4c284b126563
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Attach WinDBG Debugger to CS:GO Process

## Summary

This procedure sets up debugging by attaching WinDBG to the running CS:GO process (csgo.exe), allowing monitoring of memory operations and crash analysis during the exploit trigger.

## Description

WinDBG is a Microsoft debugging tool used here to observe the buffer overflow in real-time. After launching CS:GO, attach to the process to breakpoint on exceptions like access violations. This step is crucial for reproducing and confirming the vulnerability in a controlled environment, typically on a test machine. Expected outcomes include successful attachment and readiness to capture the crash from malformed .BSP parsing.

## Requirements

1. WinDBG installed (part of Windows SDK or standalone)
2. CS:GO running on the target Windows machine
3. Administrative privileges for process attachment

## Defense

Defensive measures and detection strategies:

- Enable anti-debugging in applications or use tools like PEB checks
- Monitor for debugger attachments via process monitoring (e.g., Sysmon events)
- Game integrity checks to detect modified executables

## Objectives

1. Gain visibility into CS:GO's memory during map loading
2. Prepare for exception handling and stack trace analysis
3. Ensure safe reproduction without permanent damage

## Instructions

### Step 1: Launch CS:GO

**Context**: Start the game process to which the debugger will attach.

Run CS:GO via Steam shortcut or executable.

> Expected output: csgo.exe process active in Task Manager.

### Step 2: Attach WinDBG

**Context**: Use WinDBG's attach feature to hook into the live process for monitoring.

Launch WinDBG and select File > Attach to a Process, then choose csgo.exe from the list.

> Expected output: WinDBG console shows ".attach csgo.exe" success, with process under debug control. Set breakpoints if needed, e.g., on memory access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/WinDBG]]

## Tags

- debugging
- windbg
- process-attachment
