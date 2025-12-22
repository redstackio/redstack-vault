---
id: 7842cbab-3dfe-47d5-9d3c-53d9495d2d5a
name: Check-PowerShell-Constrained-Language-Mode
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.470722+00:00'
updated_at: '2023-04-10T20:37:07.123835+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Constrained Language Mode]]'
  - '[[tags/Powershell]]'
  - '[[tags/Windows - Defenses]]'
commands:
  - '[[commands/powershell-get-language-mode]]'
platforms:
  - Windows
tools: []
validated: true
---

# Check-PowerShell-Constrained-Language-Mode

## Summary

This procedure checks whether the current PowerShell session is operating in Constrained Language Mode, a security feature that limits the execution of certain scripts and commands to prevent malicious activity. It is useful during red team engagements to assess if defensive restrictions are in place that could hinder script-based attacks or evasion techniques.

## Description

Constrained Language Mode in PowerShell enforces a whitelist of approved commands and restricts access to potentially dangerous features like unsigned scripts, COM objects, and certain .NET types. This mode is often enabled via AppLocker, WDAC (Windows Defender Application Control), or group policy to mitigate risks from PowerShell-based malware. Attackers use this check to determine if they need to adapt their tactics, such as falling back to alternative execution methods like WMI or native binaries if Constrained Mode blocks their payloads. The procedure queries the session state directly and interprets the result to guide next steps in an engagement. It applies to Windows environments where PowerShell is available, typically Windows 7 and later.

## Requirements

1. Administrative or user-level access to a Windows system with PowerShell installed (version 3.0 or later).
2. Ability to execute PowerShell commands interactively or via a remote session.
3. No external tools required; uses built-in PowerShell features.

## Defense

- Enable Constrained Language Mode through Group Policy or device configuration to restrict PowerShell execution.
- Monitor PowerShell logs via Event ID 4103/4104 for script block logging and unusual queries to session state properties.
- Implement just-in-time (JIT) application allowlisting with tools like AppLocker to enforce mode restrictions.

## Objectives

1. Identify if the PowerShell environment is restricted by Constrained Language Mode.
2. Assess potential impacts on script execution and plan workarounds if restrictions are active.
3. Verify the mode without triggering alerts in monitored environments.

## Instructions

### Step 1: Launch PowerShell Session

**Context**: Start a PowerShell session to access the execution context. This ensures you are querying the current environment's configuration.

Open PowerShell via the command line, Start menu, or remotely (e.g., via WinRM). No special privileges are needed for the check itself.

### Step 2: Query Language Mode

**Context**: Use the built-in session state property to retrieve the current language mode. This reveals whether the session allows full PowerShell capabilities or is constrained.

**Command** ([[commands/powershell-get-language-mode]]):
```powershell
$ExecutionContext.SessionState.LanguageMode
```

> This command outputs the mode as a string: 'FullLanguage' for unrestricted access or 'ConstrainedLanguage' for restricted mode. If the output is 'ConstrainedLanguage', scripts using restricted features (e.g., Invoke-Expression on unsigned code) will fail. In 'FullLanguage' mode, proceed with standard PowerShell techniques.

### Step 3: Interpret and Verify Results

**Context**: Based on the output, evaluate the environment and test a restricted operation if needed to confirm.

If the mode is 'ConstrainedLanguage', attempt a simple restricted command like `Get-Process -Name nonExistent` to verify failures. Document the result for reporting evasion needs.

**Expected Output**: For the query command, a string value such as:

```
ConstrainedLanguage
```

Or:

```
FullLanguage
```

For verification tests in Constrained Mode, expect errors like 'The assignment expression is not valid' for restricted syntax.
