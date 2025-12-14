---
id: uuid-placeholder
tags:
  - privilege-escalation
  - dll-hijacking
  - windows
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/start-glasswire-service]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:26:22.837Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Trigger-GlassWire-Service-for-SYSTEM-Execution

## Summary

This procedure triggers the GlassWire service (GWCtlSrv.exe) to load the malicious DLL from the hijacked PATH, resulting in arbitrary code execution with SYSTEM privileges for escalation.

## Description

The GlassWire service runs as SYSTEM and loads DLLs like swift.dll during startup. With PATH modified, it loads the malicious version from the writable directory. Monitor with Process Monitor to confirm. Requires reboot or manual service start; ideal for post-compromise escalation.

## Requirements

1. PATH already modified with writable directory
2. Malicious DLL placed (e.g., swift.dll)
3. Admin access to start services or reboot capability

## Defense

Defensive measures and detection strategies:

- Disable unnecessary services or run with least privilege
- Monitor service starts (Event ID 7045) and DLL loads (Sysmon 7)
- Use protected process light for critical services
- Block writable PATH directories in policy

## Objectives

1. Execute payload as SYSTEM
2. Escalate from user to system privileges
3. Inject into service process if needed

## Instructions

### Step 1: Start the Service

**Context**: Initiate the service load to trigger DLL hijacking.

**Command** ([[commands/start-glasswire-service]]):
```cmd
net start GWCtlSrv
```

> Starts the GlassWire Control Service. If already running, stop and start: net stop GWCtlSrv then net start. Expected: Service started successfully.

### Step 2: Monitor Execution

**Context**: Verify DLL load and payload activation.

Use [[tools/Process-Monitor]] filtered for GWCtlSrv.exe and path C:\Dima\.

> Expected: Entry for DLL load from custom path, followed by payload (e.g., network connection).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[DLL Search Order Hijacking]] DLL Search Order Hijacking

### Sub-Techniques


## Commands Used

- [[commands/start-glasswire-service]]

## Tools Used

- [[tools/Process-Monitor]]

## Tags

- [[privilege-escalation]]
- [[dll-hijacking]]
