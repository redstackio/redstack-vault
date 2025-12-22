---
tags:
  - execution
  - monitoring
  - dos
type: procedure
tools:
  - '[[tools/Windows-Task-Manager]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.892Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 418c553a-b375-41f4-bfb1-2a6a9bae5277
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Execute PoC and Monitor Memory Usage

## Summary

This procedure runs the PoC executable to trigger the memory leak in OCUtil.dll's IsChildFile function and monitors resource consumption using Task Manager to validate the DoS impact.

## Description

The PoC executable loads OCUtil_x64.dll, retrieves the IsChildFile function pointer, and calls it infinitely with paths like "C:\parent" and "C:\parent\child.txt". Due to the leak at line 42, memory accumulates without freeing, exhausting RAM. In a real attack, this could be triggered via explorer.exe context menus. Expected outcome: Process memory balloons, leading to crashes. Run in a VM to avoid system damage.

## Requirements

1. Compiled tests.exe PoC
2. OCUtil_x64.dll in PATH
3. Windows Task Manager access

## Defense

Defensive measures and detection strategies:

- Enable memory leak detection in client software
- Monitor for anomalous memory growth in explorer.exe
- Implement rate limiting on context menu actions

## Objectives

1. Trigger repeated function calls to exploit the leak
2. Observe and quantify memory exhaustion
3. Confirm DoS potential on the target system

## Instructions

### Step 1: Launch the PoC

**Context**: Start the executable to begin the infinite loop calling the vulnerable function.

Double-click or run tests.exe from Command Prompt.

> The program will load the DLL and start allocating memory; no output console may appear, but it runs silently.

### Step 2: Open Task Manager

**Context**: Monitor the tests.exe process for increasing memory usage.

Press Ctrl+Shift+Esc to open Task Manager, go to the Processes tab, and locate tests.exe.

> Sort by Memory column; watch for steady increase (e.g., 10-50 MB per minute depending on system).

### Step 3: Validate Impact

**Context**: Run until memory exhaustion or terminate to assess the leak.

Allow execution for 1-5 minutes, noting peak memory, then end the process via Task Manager.

> Success: Memory usage exceeds baseline significantly; potential system slowdown if scaled.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Windows-Task-Manager]]

## Tags

- execution
- monitoring
- dos
