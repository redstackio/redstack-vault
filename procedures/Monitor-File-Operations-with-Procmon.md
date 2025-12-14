---
id: monitor-procmon-acronis
tags:
  - procmon
  - file-monitoring
type: procedure
tools:
  - '[[tools/Procmon]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/procmon-launch-filtered]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:28:52.226Z'
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
# Monitor-File-Operations-with-Procmon

## Summary

This procedure sets up Process Monitor (Procmon) to capture file system operations by the Acronis Scheduler2 Service (schedul2.exe), specifically CreateFile events on 'C:\program.exe', to observe the hijacking attempt during service startup.

## Description

Procmon from Sysinternals is used to monitor process activity in real-time. Filters are applied to focus on schedul2.exe and file creates/opens, revealing the service's insecure lookup. This is crucial for verifying the vulnerability without manual debugging. Prerequisites include downloading Procmon and running as admin for full capture. Expected outcome: Logs showing the execution attempt as SYSTEM.

## Requirements

1. Sysinternals Procmon downloaded and extracted
2. Admin privileges to launch with full monitoring
3. Target process (schedul2.exe) will start later in chain

## Defense

Defensive measures and detection strategies:

- Use EDR tools like Sysmon for persistent monitoring instead of manual Procmon
- Alert on unexpected file creates in C:\ by services
- Block unsigned EXEs in system roots

## Objectives

1. Capture service file access attempts
2. Filter noise to focus on vulnerable path
3. Log for post-analysis of privilege escalation

## Instructions

### Step 1: Launch Procmon

**Context**: Start Procmon with EULA acceptance and optional backing file for capture.

Execute [[commands/procmon-launch-filtered]]:

```bash
procmon.exe /AcceptEula /BackingFile acronis_capture.pml
```

> Launches Procmon; GUI opens for filter setup.

### Step 2: Apply Filters

**Context**: Configure filters to monitor only relevant events.

In Procmon GUI: Add filter - Process Name is schedul2.exe, then Operation is CreateFile, Path contains Program.exe.

No CLI command; use GUI.

> Filters reduce noise; start capture.

### Step 3: Begin Capture

**Context**: Start monitoring before triggering the service.

Click Capture in Procmon (or Ctrl+E).

> Events begin logging in real-time.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Process Discovery]] Process Discovery

### Sub-Techniques

- [[T1057.001]] Process Dump

## Commands Used

- [[commands/procmon-launch-filtered]]

## Tools Used

- [[tools/Procmon]]

## Tags

- [[tools/Procmon]]
- [[monitoring]]
