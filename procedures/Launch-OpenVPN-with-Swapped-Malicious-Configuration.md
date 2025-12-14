---
tags:
  - openvpn-launch
  - dll-execution
  - openssl-engine
  - system-privileges
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:28.599Z'
sub_techniques:
  - '[[T1068.001]]'
id: b3642e51-6941-4818-881e-060daa49341f
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[DLL Search Order Hijacking]]'
---
# Launch OpenVPN with Swapped Malicious Configuration

## Summary

This procedure relies on the NordVPN service launching OpenVPN with the swapped config, processing the OpenSSL engine directive to load and execute an arbitrary DLL with SYSTEM privileges.

## Description

Post-swap, the service invokes OpenVPN.exe with the malicious config path. OpenVPN parses the config and encounters the 'engine' option (previously mitigated but bypassed via path control), loading the specified DLL via OpenSSL's dynamic engine loading. The DLL executes in the context of the SYSTEM-privileged OpenVPN process, allowing code injection and escalation from low-priv user.

## Requirements

1. Successful file swap from prior step
2. Malicious DLL placed at the engine path (e.g., C:\temp\malicious.dll) with payload for execution
3. NordVPN service configured to launch OpenVPN as child process

## Defense

Defensive measures and detection strategies:

- Whitelist OpenVPN config options and block 'engine' entirely at parse time
- Run OpenVPN in a restricted integrity level or sandbox to limit DLL loading
- Audit OpenVPN process creation and loaded modules for anomalies using API monitoring

## Objectives

1. Ensure OpenVPN launches with the tampered config
2. Trigger DLL load and execution as SYSTEM
3. Confirm privilege escalation via injected code

## Instructions

### Step 1: Await Service Launch

**Context**: The service automatically starts OpenVPN after validation.

Monitor for OpenVPN.exe process creation via Task Manager or ProcMon.

> Process runs as SYSTEM, parented by NordVPN service.

### Step 2: Verify DLL Execution

**Context**: Check if the malicious DLL has loaded and executed.

Use the DLL's payload (e.g., a beacon or log write) to confirm execution.

> Success if payload actions (e.g., file drop or registry write) occur under SYSTEM.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[DLL Search Order Hijacking]] DLL Search Order Hijacking

### Sub-Techniques

- [[T1068.001]] Exploitation for Privilege Escalation: Vulnerability in Software

## Commands Used


## Tools Used


## Tags

- openvpn-launch
- dll-execution
- openssl-engine
- system-privileges
