---
id: proc-procmon-monitor-001
tags:
  - monitoring
  - dll-loading
  - recon
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:29:19.667Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[T1057.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Monitor-DLL-Loading-with-Process-Monitor

## Summary

This procedure uses Process Monitor to observe and analyze DLL loading behavior in Acronis True Image, identifying untrusted search order paths like C:\Python27 for potential hijacking opportunities.

## Description

Process Monitor (ProcMon) from Sysinternals captures real-time file, registry, and process activity. In this scenario, launch Acronis as admin and filter for TrueImage.exe events to reveal attempts to load tcmalloc.dll from PATH directories, including writable ones. This reconnaissance step confirms the vulnerability before payload deployment. Prerequisites: Admin rights to run Acronis, ProcMon installed on target.

## Requirements

1. Process Monitor downloaded from Microsoft Sysinternals
2. Acronis True Image installed and runnable as admin
3. Target Windows machine with Python 2.7 PATH entry

## Defense

Defensive measures and detection strategies:

- Block unauthorized use of monitoring tools via application whitelisting
- Audit process creation events (Event ID 4688) for ProcMon execution
- Implement DLL safe loading via application manifests

## Objectives

1. Capture DLL search order during application execution
2. Identify writable paths in search sequence
3. Validate administrative context of loading process

## Instructions

### Step 1: Launch Process Monitor

**Context**: Start capturing all system events before running the target application.

Run ProcMon.exe as administrator and click 'Capture' to begin logging.

### Step 2: Launch Acronis True Image

**Context**: Trigger the vulnerable process to observe DLL loads.

Execute `C:\Program Files (x86)\Acronis\TrueImageHome\TrueImageLauncher.exe` as admin, which spawns TrueImage.exe.

> ProcMon will log sub-process creation and file access attempts.

### Step 3: Apply Filters for DLL Events

**Context**: Narrow down logs to relevant NOT FOUND events in Python path.

Stop capture, then set filters: Process Name is TrueImage.exe (Include), Result contains NOT FOUND (Include), Path contains Python27 (Include).

> Expected: Events showing LoadLibrary calls to tcmalloc.dll in C:\Python27 failing.

### Step 4: Analyze Results

**Context**: Confirm vulnerability details.

Review filtered events for path order and privileges (right-click > Properties > Process tab).

> Success: tcmalloc.dll search includes C:\Python27 under admin context.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Process Discovery]]

### Sub-Techniques

- [[T1057.001]]

## Commands Used


## Tools Used

- [[tools/Process-Monitor]]

## Tags

- monitoring
- dll
- process-activity
