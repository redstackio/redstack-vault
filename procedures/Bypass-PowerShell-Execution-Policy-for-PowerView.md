---
id: 4a9593ba-f0d1-4059-9928-1c773a178401
name: Bypass-PowerShell-Execution-Policy-for-PowerView
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.967799+00:00'
updated_at: '2023-04-10T20:37:00.752574+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Signed Script Proxy Execution|T1216 - Signed Script Proxy
    Execution]]
sub_techniques: []
tags:
  - '[[tags/Execution Policy]]'
  - '[[tags/Powershell]]'
  - powerview
  - defense-evasion
commands:
  - '[[commands/load-powerview-encoded-command]]'
  - '[[commands/load-powerview-bypass-policy]]'
  - '[[commands/set-powershell-execution-policy-currentuser-unrestricted]]'
  - '[[commands/set-powershell-execution-policy-process-bypass]]'
platforms:
  - Windows
tools: []
validated: true
---

# Bypass-PowerShell-Execution-Policy-for-PowerView

## Summary

This procedure demonstrates how to bypass PowerShell's execution policy restrictions to load and run the PowerView reconnaissance tool, which is useful for Active Directory enumeration during red team engagements. By setting the policy to Unrestricted for the current user or Bypass for the process scope, attackers can execute unsigned scripts like PowerView.ps1 without triggering default security blocks.

## Description

PowerShell's execution policy is a safety mechanism that controls script execution based on signatures and sources, defaulting to Restricted to prevent unauthorized code from running. PowerView, a PowerShell module for AD reconnaissance (e.g., user enumeration, group discovery), often requires bypassing this policy since it's typically unsigned. This technique evades endpoint detection by using scoped policy changes that don't require administrative privileges for user-level adjustments. It's applicable in Windows environments with domain-joined systems, where an initial foothold (e.g., via phishing or exploit) provides command execution access. Success allows loading PowerView for further discovery without altering system-wide settings, minimizing detection risk.

## Requirements

1. PowerShell v2.0 or later installed on a Windows system.
2. Access to the PowerView.ps1 script file (downloaded or transferred to the target).
3. Encoded command string for initial module load (generated via PowerShell encoding).
4. User-level access (admin not strictly required for CurrentUser scope; Process scope works in any session).

## Defense

- Enforce strict execution policies via Group Policy (e.g., set to AllSigned or RemoteSigned domain-wide).
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to capture policy changes and script loads.
- Monitor for suspicious PowerShell processes spawning with -EncodedCommand or -ep bypass flags using EDR tools.
- Verify script signatures and block unsigned downloads via AppLocker or WDAC.

## Objectives

1. Temporarily bypass PowerShell execution policy to load unsigned scripts.
2. Successfully import and execute PowerView for AD reconnaissance.
3. Maintain low detection profile by using scoped policy changes.
4. Verify PowerView functionality post-load without system-wide alterations.

## Instructions

### Step 1: Load PowerView Using Encoded Command

**Context**: Use an encoded PowerShell command to initially import the PowerView module, avoiding direct script execution restrictions. This step decouples the load from policy enforcement.

**Command** ([[commands/load-powerview-encoded-command]]):
```powershell
powershell -EncodedCommand $encodedCommand
```

> Generate the $encodedCommand by encoding a PowerShell snippet that imports PowerView (e.g., using `powershell -c "[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes('Import-Module PowerView.ps1'))"`). Expected output: PowerShell session loads the module without errors, confirming import via `Get-Command Get-DomainUser` availability.

### Step 2: Load PowerView with Bypass Flag

**Context**: If the encoded method fails due to policy, directly load the script by bypassing policy for this invocation only. This is a fallback for environments with partial restrictions.

**Command** ([[commands/load-powerview-bypass-policy]]):
```powershell
powershell -ep bypass ./PowerView.ps1
```

> Run from the directory containing PowerView.ps1. Expected output: Script loads successfully, with PowerView functions (e.g., Get-NetDomain) now available in the session.

### Step 3: Set Execution Policy to Unrestricted for Current User

**Context**: Change the policy scope to CurrentUser, allowing unrestricted script execution for the logged-in user without affecting others. This persists across sessions for that user.

**Command** ([[commands/set-powershell-execution-policy-currentuser-unrestricted]]):
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

> Confirm with `Get-ExecutionPolicy -List`. Expected output: Policy shows 'Unrestricted' for CurrentUser scope, enabling script runs like `& ./PowerView.ps1`.

### Step 4: Set Execution Policy to Bypass for Current Process

**Context**: For non-persistent bypass limited to the current PowerShell process, use this to execute scripts inline without altering user or machine policies.

**Command** ([[commands/set-powershell-execution-policy-process-bypass]]):
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

> Ideal for one-off executions. Expected output: Policy shows 'Bypass' for Process scope; test by running an unsigned script, which executes without warnings.

### Step 5: Verify PowerView Load and Test Functionality

**Context**: After policy bypass, confirm PowerView is loaded and functional by invoking a basic reconnaissance command.

**Instructions**: Run `Get-DomainUser` or similar PowerView cmdlet. If in a domain context, it should enumerate users.

> Expected output: List of domain users or error if not domain-joined. Success confirms the bypass worked, allowing further AD ops.
