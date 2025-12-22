---
id: 08207f16-8216-4efa-9c25-589e8798f0b5
name: Terminate-Microsoft-Defender-to-Bypass-PPL
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.597041+00:00'
updated_at: '2023-04-10T20:37:03.700126+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Impair Defenses]]'
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - '[[tags/Protected Process Light]]'
  - '[[tags/Windows - Defenses]]'
  - defense-evasion
commands:
  - '[[commands/check-lsass-ppl-status]]'
  - '[[commands/attempt-kill-msmpeng-process]]'
platforms:
  - Windows
tools: []
validated: true
---

# Terminate-Microsoft-Defender-to-Bypass-PPL

## Summary

This procedure demonstrates an attempt to bypass Windows Defender's Protected Process Light (PPL) by terminating the MsMpEng.exe process, which protects critical system processes like LSASS. Although the termination often fails due to access protections, understanding this technique highlights defense evasion methods used in post-exploitation scenarios to access sensitive credential data in LSASS.

## Description

Protected Process Light (PPL) is a Windows security feature that prevents unauthorized tampering with critical processes, such as LSASS, which stores domain credentials. Microsoft Defender enforces PPL for these processes. Attackers may attempt to disable Defender by killing its core process (MsMpEng.exe) to weaken protections and enable credential dumping. This procedure first verifies if LSASS is running under PPL, then attempts termination. Note that on modern Windows systems with full protections, this will likely fail with 'Access is denied,' requiring alternative evasion techniques like DLL hijacking or kernel exploits. This is commonly used in privilege escalation chains targeting Active Directory environments.

## Requirements

1. Administrator-level privileges on the target Windows system
2. PowerShell or Command Prompt access
3. No additional tools required, but EDR bypass may be needed for execution

## Defense

- Ensure systems have up-to-date security patches and Windows Defender is fully enabled
- Implement application whitelisting and restrict PowerShell execution via Constrained Language Mode
- Use endpoint detection and response (EDR) tools to monitor process termination attempts and registry queries on security keys
- Enable LSASS protection via Credential Guard and monitor for anomalous Defender service stops

## Objectives

1. Verify if LSASS is protected by PPL to assess bypass feasibility
2. Attempt to terminate MsMpEng.exe to disable Defender's PPL enforcement
3. Gain potential access to LSASS for credential extraction if successful

## Instructions

### Step 1: Verify LSASS PPL Status

**Context**: Before attempting any bypass, check the registry to confirm if LSASS is running in Protected Process Light mode. This step determines if PPL is active and worth targeting.

**Command** ([[commands/check-lsass-ppl-status]]):
```powershell
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL
```

> This queries the RunAsPPL registry value. A value of '1' indicates LSASS is protected by PPL; '0' or absence means it's not. Run this in an elevated PowerShell session. If PPL is disabled, proceed to credential dumping without further steps.

### Step 2: Attempt to Terminate MsMpEng.exe

**Context**: Target the Microsoft Defender engine process to impair its ability to enforce PPL on LSASS. This step illustrates the protection mechanism, as termination typically fails on protected systems, highlighting the need for advanced evasion.

**Command** ([[commands/attempt-kill-msmpeng-process]]):
```powershell
taskkill /f /im MsMpEng.exe
```

> The taskkill command forcefully attempts to end the process by image name. On success (rare without bypasses), Defender stops, and PPL enforcement weakens, allowing LSASS access. Expected failure output includes 'Access is denied' due to process protections. If it succeeds, verify by re-running Step 1 and check for Defender service status with Get-Service MsMpEng.
