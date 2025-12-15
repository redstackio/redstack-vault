---
tags:
  - execution
  - service-manipulation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/restart-acronis-service]]'
platforms:
  - Windows
techniques:
  - '[[Service Execution]]'
  - '[[Hijack Execution Flow]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b77e9518-62df-4273-a1dc-1d66a6c28d74
created_at: '2025-12-14T17:26:17.562Z'
updated_at: '2025-12-14T17:26:17.562Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Service Execution]]'
  - '[[Hijack Execution Flow]]'
---
# Trigger Service Restart to Execute Hijacked Payload

## Summary

This procedure restarts the vulnerable Acronis Nonstop Backup Service, causing Windows to execute the hijacked malicious executable with SYSTEM privileges due to the unquoted path.

## Description

By stopping and starting the service, or rebooting, the Windows service manager resolves the ImagePath from left to right, hitting the malicious file first. This triggers arbitrary code execution as SYSTEM without modifying the service registry, relying solely on the path misconfiguration.

## Requirements

1. Malicious executable placed in hijack path from prior step
2. Local access to run sc commands (low privileges)
3. Acronis service installed and running initially

## Defense

Defensive measures and detection strategies:

- Quote all service paths in registry (HKLM\SYSTEM\CurrentControlSet\Services)
- Monitor service restarts via Event ID 7036 in System logs
- Use privileged service hardening (e.g., restrict service accounts)

## Objectives

1. Force resolution of the hijacked path
2. Achieve code execution as SYSTEM
3. Minimize detection by using legitimate service controls

## Instructions

### Step 1: Stop the Service

**Context**: Halt the Acronis service to prepare for restart, ensuring clean state.

**Command** (Part of [[commands/restart-acronis-service]]):
```cmd
sc stop "Acronis Nonstop Backup Service"
```

> Stops the service gracefully. Expected output: SERVICE_NAME: Acronis Nonstop Backup Service
STATE 1 STOPPING ...

### Step 2: Start the Service

**Context**: Restart the service to trigger path resolution and payload execution.

**Command** (Part of [[commands/restart-acronis-service]]):
```cmd
sc start "Acronis Nonstop Backup Service"
```

> Starts the service, executing the hijacked EXE. Expected output: SERVICE_NAME: Acronis Nonstop Backup Service
TYPE : 10  WIN32_OWN_PROCESS
STATE : 2  START_PENDING

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Service Execution]] System Services: Service Execution
- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used

- [[commands/restart-acronis-service]]

## Tools Used


## Tags

- service-restart
- trigger-execution
- escalation
