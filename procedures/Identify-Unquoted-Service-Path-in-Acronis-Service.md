---
tags:
  - discovery
  - service-enumeration
  - unquoted-path
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/query-acronis-service-config]]'
platforms:
  - Windows
techniques:
  - '[[System Service Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c353140c-8ca1-4e0f-bfe3-c4bb8f99efaf
created_at: '2025-12-14T17:26:17.568Z'
updated_at: '2025-12-14T17:26:17.568Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Service Discovery]]'
---
# Identify Unquoted Service Path in Acronis Service

## Summary

This procedure enumerates Windows services to identify the Acronis Nonstop Backup Service with an unquoted executable path, enabling potential hijacking for privilege escalation.

## Description

The Acronis True Image 2020 Nonstop Backup Service (afcdpsrv.exe) has its ImagePath set to 'C:\Program Files (x86)\Common Files\Acronis\CDP\afcdpsrv.exe', which contains spaces but lacks enclosing double quotes. This misconfiguration allows Windows to parse alternative paths during service startup, such as C:\Program.exe or C:\Program Files (x86)\Common.exe, if those files exist. The procedure uses built-in Windows tools to query and validate this vulnerability on a target system with local access.

## Requirements

1. Local access to a Windows system with Acronis True Image 2020 installed
2. Command prompt or PowerShell access (low privileges sufficient)
3. Service management permissions (standard user)

## Defense

Defensive measures and detection strategies:

- Use tools like Autoruns or PowerShell scripts to scan for unquoted service paths
- Monitor service configurations via Group Policy or SCCM for quote enforcement
- Enable Windows Event Logging for service start failures or unexpected executions

## Objectives

1. Confirm the presence of the vulnerable Acronis service
2. Identify exploitable hijack paths based on directory structure
3. Prepare for path hijacking in subsequent steps

## Instructions

### Step 1: Query Service Configuration

**Context**: Use the Service Control (sc) tool to retrieve details of the Acronis Nonstop Backup Service and inspect the ImagePath for quotes.

**Command** ([[commands/query-acronis-service-config]]):
```cmd
sc qc "Acronis Nonstop Backup Service"
```

> This command queries the service configuration and outputs details including STATE, BINPATH, and ImagePath. Look for ImagePath: C:\Program Files (x86)\Common Files\Acronis\CDP\afcdpsrv.exe without quotes. Expected output includes the unquoted path, confirming vulnerability. If quotes are present, the exploit fails.

### Step 2: Validate Hijack Paths

**Context**: Manually check if alternative paths like C:\Program.exe or C:\Program Files (x86)\Common.exe are writable by the current user.

**Command** (Manual check):
```cmd
dir C:\Program.exe
icacls "C:\Program Files (x86)\Common.exe"
```

> These commands list files and permissions. Expected output: File not found or writable permissions indicate exploit feasibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Service Discovery]] System Service Discovery

### Sub-Techniques


## Commands Used

- [[commands/query-acronis-service-config]]

## Tools Used


## Tags

- discovery
- windows-service
- enumeration
