---
id: 6acfefb7-490d-48e6-99ed-fd746459410b
name: Check-PowerShell-Session-Language-Mode
type: procedure
verified: true
submitted: true
created_at: '2020-03-30T18:49:29.648478+00:00'
updated_at: '2023-05-25T19:53:23.044009+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Security Software Discovery]]'
sub_techniques: []
tags:
  - Enumeration
commands:
  - '[[commands/powershell-show-session-language-mode]]'
platforms:
  - Windows
tools: []
validated: true
---

# Check-PowerShell-Session-Language-Mode

## Summary

This procedure checks the current PowerShell session's language mode to determine if Constrained Language Mode (CLM) is enabled, which restricts scripting capabilities to reduce the attack surface while allowing basic administrative tasks. Attackers use this to assess if advanced PowerShell techniques are viable or if bypasses are needed.

## Description

Constrained Language Mode (CLM) in PowerShell limits the use of certain language elements, such as unsigned scripts, module loading from remote sources, and reflective code execution, to prevent exploitation. This mode is often enforced by security policies like AppLocker, Device Guard, or WDAC. While not impenetrable—bypasses like Just Enough Administration (JEA) evasion or environment variable manipulation exist—CLM can force attackers to pivot to alternative methods, such as native Windows binaries or LOLBins. This procedure is typically run early in post-exploitation to gauge the environment's restrictions on PowerShell usage, aiding in decision-making for subsequent actions like lateral movement or persistence.

## Requirements

1. Active PowerShell session on a Windows target (PowerShell 3.0 or later).
2. Local or remote execution privileges (e.g., via interactive shell or remote management tools like WinRM).
3. No additional tools required; uses built-in PowerShell variables.

## Defense

Defensive measures and detection strategies:

- Enable PowerShell Constrained Language Mode via Group Policy (Administrative Templates > Windows Components > Windows PowerShell > Turn on PowerShell Script Block Logging).
- Monitor PowerShell execution logs for queries to $ExecutionContext.SessionState.LanguageMode using Event ID 4104 (Script Block Logging).
- Implement Application Control policies (e.g., AppLocker) to enforce CLM and block unsigned scripts.
- Use Sysmon to log PowerShell process creation and module loads for anomalous activity.

## Objectives

1. Identify if the PowerShell session is in ConstrainedLanguage, FullLanguage, or RestrictedLanguage mode.
2. Assess the feasibility of advanced PowerShell-based attacks in the current environment.
3. Inform pivoting to alternative techniques if restrictions are detected.

## Instructions

### Step 1: Query the Session Language Mode

**Context**: This step retrieves the current language mode of the PowerShell session. Possible outputs include 'FullLanguage' (unrestricted), 'ConstrainedLanguage' (limited scripting), or 'RestrictedLanguage' (no scripting). Understanding the mode helps attackers evaluate if they can execute complex scripts or need to use workarounds.

**Command** ([[commands/powershell-show-session-language-mode]]):
```powershell
$ExecutionContext.SessionState.LanguageMode
```

> This command accesses the built-in $ExecutionContext variable to inspect the session state without requiring elevated privileges or external modules. Run it in an interactive PowerShell prompt. If the output is 'ConstrainedLanguage', consider bypass techniques like launching a new unconstrained process via cmd.exe or using environment variables to alter policy enforcement.

**Expected Output**: A string indicating the mode, such as 'ConstrainedLanguage' or 'FullLanguage'.
