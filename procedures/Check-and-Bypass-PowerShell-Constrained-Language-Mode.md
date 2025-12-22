---
id: d46c4f92-fb7c-4824-aca1-278c7b4f8555
name: Check-and-Bypass-PowerShell-Constrained-Language-Mode
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.993289+00:00'
updated_at: '2023-10-10T20:37:00.424076+00:00'
tactics:
  - '[[Discovery]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[System Information Discovery]]'
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - powershell
  - constrained-mode
  - evasion
  - discovery
commands:
  - '[[commands/powershell-get-language-mode]]'
  - '[[commands/powershell-launch-version-2]]'
platforms:
  - Windows
tools: []
validated: true
---

# Check-and-Bypass-PowerShell-Constrained-Language-Mode

## Summary

This procedure checks the current PowerShell execution context language mode to determine if it is operating in Constrained Language Mode, which restricts certain commands and features for security. If constrained, it provides a method to bypass this restriction by launching PowerShell version 2, which operates in Full Language mode, allowing broader script execution during red team engagements or testing.

## Description

PowerShell Constrained Language Mode is a security feature that limits the language elements and cmdlets available to prevent unauthorized or malicious script execution, often enforced via Group Policy or application whitelisting. In offensive security scenarios, attackers may encounter this during post-exploitation to assess the environment's restrictions. This procedure first queries the session state to identify the mode (FullLanguage or ConstrainedLanguage). If ConstrainedLanguage is detected, it bypasses by invoking PowerShell v2, which does not enforce the same constraints and enables execution of restricted scripts. This is useful for evasion in Windows environments where modern PowerShell (v3+) is locked down. Expected outcomes include confirmation of the mode and successful launch of an unrestricted shell for further actions like script execution or tool invocation.

## Requirements

1. Administrative or user-level access to a PowerShell session on a Windows target.
2. PowerShell v2.0 or later installed (v2 is typically available on Windows 7+).
3. No additional tools required, as this uses built-in PowerShell capabilities.

## Defense

- Enforce Constrained Language Mode via Group Policy (Administrative Templates > Windows Components > Windows PowerShell) to limit scripting capabilities.
- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor execution contexts and detect mode checks or version switches.
- Implement application control solutions like AppLocker or WDAC to block PowerShell v2 execution and restrict downgrades.
- Monitor for anomalous PowerShell processes spawning older versions or unusual language mode queries.

## Objectives

1. Identify if the current PowerShell session is restricted by Constrained Language Mode.
2. Bypass restrictions if present to gain Full Language mode capabilities.
3. Verify successful mode transition for continued operations.

## Instructions

### Step 1: Query Current Language Mode

**Context**: Begin by checking the execution context to determine the current language mode. This reveals if restrictions are active, guiding whether a bypass is needed. FullLanguage allows all features, while ConstrainedLanguage blocks sensitive operations like reflection or unsigned scripts.

**Command** ([[commands/powershell-get-language-mode]]):
```powershell
$ExecutionContext.SessionState.LanguageMode
```

> This command outputs the mode as a string (e.g., "ConstrainedLanguage" or "FullLanguage"). If ConstrainedLanguage is returned, proceed to bypass; otherwise, the session is unrestricted.

### Step 2: Launch PowerShell Version 2 for Bypass

**Context**: If ConstrainedLanguage is detected, invoke PowerShell v2 to escape restrictions. Version 2 runs in FullLanguage mode by default and supports legacy scripting without modern constraints, enabling execution of blocked cmdlets or code.

**Command** ([[commands/powershell-launch-version-2]]):
```powershell
powershell -version 2
```

> This spawns a new PowerShell v2 interactive shell. Within this shell, re-run the language mode check to confirm FullLanguage. Use this session for subsequent restricted actions, such as loading modules or running scripts.

### Step 3: Verify Bypass Success

**Context**: After launching v2, confirm the mode has changed to ensure the bypass worked. This validates the environment for further exploitation.

**Command** ([[commands/powershell-get-language-mode]]):
```powershell
$ExecutionContext.SessionState.LanguageMode
```

> Expected output in the v2 shell: "FullLanguage". If still constrained, investigate deeper restrictions like execution policies or whitelisting.
