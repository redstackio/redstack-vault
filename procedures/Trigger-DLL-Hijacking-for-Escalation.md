---
id: trigger-dll-esc
tags:
  - escalation-trigger
  - dll-load
type: procedure
tools:
  - '[[tools/ProcMon]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/run-systeminfo-exe]]'
  - '[[commands/whoami-validate-privileges]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:36.851Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Trigger-DLL-Hijacking-for-Escalation

## Summary

This procedure triggers the DLL hijacking by re-executing systeminfo.exe, causing it to load the malicious snapapi.dll from the PATH directory and run the payload with elevated privileges, confirming local escalation.

## Description

With preparations in place, running systeminfo.exe exploits the search-order flaw, loading the hijacked DLL instead of the legitimate one. The DLL executes the batch payload in the elevated context of the Acronis utility. ProcMon can monitor for confirmation. This achieves arbitrary code execution as SYSTEM on vulnerable Windows setups with the agent.

## Requirements

1. Malicious DLL and batch payload prepared from prior procedure
2. ProcMon running for optional logging
3. Local execution rights for systeminfo.exe

## Defense

Defensive measures and detection strategies:

- Patch Acronis agent to fix search order (if available)
- Enable DLL secure loading via registry (SafeDllSearchMode)
- Log and alert on anomalous DLL loads in privileged processes

## Objectives

1. Load malicious DLL via hijacked path
2. Execute payload with elevated privileges
3. Validate escalation through output file

## Instructions

### Step 1: Restart ProcMon Monitoring

**Context**: Resume logging to capture the successful DLL load.

Launch or refresh ProcMon with the same filters as before (Process: systeminfo.exe, Operation: CreateFile).

> This ensures visibility into the load from C:\Python27.

### Step 2: Execute systeminfo.exe to Trigger Load

**Context**: Run the utility to initiate the hijack.

Use [[commands/run-systeminfo-exe]]:

```cmd
C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe
```

> The executable searches PATH first, loads malicious snapapi.dll, which runs C:\attacker\mmg.bat elevated.

### Step 3: Validate Escalation

**Context**: Check payload output for privilege confirmation.

Review the file created by [[commands/whoami-validate-privileges]]:

```cmd
type C:\attacker\who.txt
```

> Expected output includes 'nt authority\system' and elevated privileges, confirming success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/run-systeminfo-exe]]
- [[commands/whoami-validate-privileges]]

## Tools Used

- [[tools/ProcMon]]

## Tags

- escalation-trigger
- dll-load
