---
tags:
  - registry
  - discovery
  - windows
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/reg-query-service-imagepath]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.161Z'
sub_techniques: []
id: 5c5a033f-09c4-460c-b966-dd76092d2491
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Examine-Windows-Registry-for-Rockstar-Service

## Summary

This procedure queries the Windows Registry to locate the Rockstar Game Library Service entry and retrieve its ImagePath, revealing potential misconfigurations for privilege escalation attacks.

## Description

The Rockstar Game Library Service manages installation, updates, and uninstallation of Rockstar Games titles. Its registry key under HKLM\SYSTEM\CurrentControlSet\Services contains an ImagePath value that specifies the executable path. Examining this allows attackers to identify unquoted paths, which Windows parses insecurely by searching each space-separated segment as a directory. This procedure assumes local access and uses built-in tools to avoid detection.

## Requirements

1. Local access to a Windows machine with Command Prompt or PowerShell
2. Rockstar Games Launcher installed (service present)
3. Administrative knowledge of registry paths (no elevated privileges needed for read)

## Defense

Defensive measures and detection strategies:

- Monitor registry reads via Sysmon Event ID 11 with registry filters
- Enforce service path quoting in software deployments
- Use AppLocker or WDAC to restrict executable paths

## Objectives

1. Retrieve the service's ImagePath value
2. Identify the exact registry key location
3. Prepare for further analysis of path vulnerabilities

## Instructions

### Step 1: Query the Registry Key

**Context**: Use reg.exe to read the ImagePath value from the service's registry key, typically named RockstarService or similar under Services.

**Command** ([[commands/reg-query-service-imagepath]]):
```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services\RockstarService" /v ImagePath
```

> This command outputs the current value of ImagePath, e.g., `C:\Program Files\Rockstar Games\Launcher\Rocker.exe`. Success is indicated by the path being displayed without errors.

### Step 2: Verify Service Existence

**Context**: Confirm the service key exists before querying specifics.

**Command** ([[commands/reg-enumerate-services]]):
```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services /s /f Rockstar*
```

> Filters for Rockstar-related services and lists matching keys. Expected output includes the full path to the service key.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery (adapted for registry enumeration)

### Sub-Techniques

-

## Commands Used

- [[commands/reg-query-service-imagepath]]
- [[commands/reg-enumerate-services]]

## Tools Used

-

## Tags

- [[registry-enumeration]]
- [[service-discovery]]
