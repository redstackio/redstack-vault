---
id: uuid-placeholder
tags:
  - persistence
  - dll-hijacking
  - windows
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/launch-glasswire-gui]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:26:22.834Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Trigger-GlassWire-GUI-for-User-Execution

## Summary

This procedure launches the GlassWire GUI (GlassWire.exe) after user logon, causing it to load the malicious Wtsapi32.dll from the hijacked PATH for arbitrary code execution in the user context, suitable for persistence.

## Description

The GUI loads Wtsapi32.dll upon launch. With PATH hijacked, the malicious DLL executes as the logged-in user, enabling persistence on shared systems or lateral movement. Triggered manually or via autostart; monitor for loads.

## Requirements

1. PATH modified and malicious Wtsapi32.dll placed
2. User logon session
3. GlassWire installed and accessible

## Defense

Defensive measures and detection strategies:

- Verify DLL signatures in user processes
- Monitor GUI launches and DLL loads (Sysmon 7)
- Restrict PATH to trusted directories via GPO
- Use behavioral analytics for anomalous user executions

## Objectives

1. Execute payload in user context
2. Establish persistence on logon
3. Enable lateral movement if multi-user

## Instructions

### Step 1: Launch GUI

**Context**: Start the GlassWire executable to trigger DLL load.

**Command** ([[commands/launch-glasswire-gui]]):
```cmd
start "" "C:\\Program Files (x86)\\GlassWire\\GlassWire.exe"
```

> Launches the GUI. Expected: Application window opens.

### Step 2: Confirm Hijack

**Context**: Observe the DLL loading behavior.

Run [[tools/Process-Monitor]] on GlassWire.exe.

> Expected: Wtsapi32.dll loaded from C:\Dima\, payload activates.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[DLL Search Order Hijacking]] DLL Search Order Hijacking

### Sub-Techniques


## Commands Used

- [[commands/launch-glasswire-gui]]

## Tools Used

- [[tools/Process-Monitor]]

## Tags

- [[Persistence]]
- [[dll-hijacking]]
