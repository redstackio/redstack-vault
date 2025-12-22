---
id: cb2b4945-7a2b-48ac-9589-5edb5c49a34a
name: Reflection-Method-with-WMF5-Autologging-Bypass-using-PowerShell-v2
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.102057+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Bypass User Account Control]]'
  - '[[PowerShell]]'
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - powershell
  - uac-bypass
  - logging-bypass
  - privilege-escalation
  - wmf5-bypass
  - reflection-method
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Reflection-Method-with-WMF5-Autologging-Bypass-using-PowerShell-v2

## Summary

This procedure uses Matt Graeber's reflection-based technique combined with a WMF5 autologging bypass to execute PowerShell v2 in an elevated context, evading User Account Control (UAC) prompts and module logging on Windows systems with Windows Management Framework 5 (WMF5) or later. By leveraging .NET Framework 2.0 for PowerShell v2 execution, it allows attackers to run scripts without triggering advanced logging features introduced in later PowerShell versions, facilitating stealthy privilege escalation and post-exploitation activities.

## Description

The technique exploits the availability of legacy PowerShell v2, which relies on .NET 2.0 and lacks the enhanced logging and constrained language mode of WMF5+. Matt Graeber's reflection method involves dynamically loading assemblies via .NET reflection to instantiate PowerShell runspaces without direct invocation of powershell.exe, but in this implementation, it focuses on launching a v2 session after verifying .NET compatibility. This bypasses UAC by running in a non-interactive elevated context and avoids autologging by staying within v2's limited telemetry. It is particularly effective on domain-joined Windows 10/11 or Server 2016+ systems where WMF5 is default. Success grants an elevated shell for further actions like credential dumping or lateral movement, with reduced forensic footprint.

## Requirements

1. Local user access to the target Windows system (standard user sufficient for initial execution, as UAC bypass elevates to admin).
2. .NET Framework 2.0.50727 installed (common on Windows 7+; verify via registry).
3. PowerShell execution policy allowing script runs (bypassable with -ExecutionPolicy Bypass if needed).
4. Administrative privileges prompted via UAC (the bypass avoids consent but requires compatible environment).

## Defense

- Disable or uninstall legacy PowerShell v2 and .NET 2.0 where possible; enforce WMF5+ with constrained language mode.
- Enable PowerShell logging (Module, Script Block, and Transcription) via Group Policy and monitor Event IDs 400-410, 800-999 in Windows Event Logs.
- Implement application whitelisting (e.g., AppLocker) to block unsigned scripts and reflection-based loads.
- Monitor registry queries to HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP and anomalous powershell.exe -version 2 launches via Sysmon (Event ID 1: Process Creation with Image: powershell.exe, CommandLine: *-version 2*).

## Objectives

1. Bypass UAC to achieve elevated execution without user interaction.
2. Evade WMF5 autologging to reduce detection of script activities.
3. Establish a stealthy PowerShell v2 session for further privilege escalation or persistence.
4. Perform malicious actions (e.g., credential access, file exfiltration) in an unlogged context.

## Instructions

### Step 1: Verify System Compatibility

**Context**: Before executing the bypass, confirm the presence of .NET 2.0.50727 and PowerShell v2 availability to ensure the technique will succeed. This step queries the registry non-destructively and provides verbose output for troubleshooting.

Run the compatibility check using PowerShell (inline or saved as a .ps1 file). If .NET 2.0 is absent, the procedure cannot proceed—consider alternative escalation paths.

**Expected Output**: Verbose message confirming ".Net version 2.0.50727 found." or error if not present.

### Step 2: Prepare and Execute the Bypass Script

**Context**: Use the provided script to check .NET version and launch PowerShell v2 if compatible. Set $ShowOnly to $true for dry-run instructions without execution, or $false to perform the actual bypass. This step handles the core logic of detecting the framework and invoking the legacy runtime.

Reference the code snippet [[codes/Check-DotNet-Version-and-Launch-PowerShell-v2]] and execute it in an elevated PowerShell prompt (right-click PowerShell > Run as Administrator, or use another UAC bypass if needed).

To run inline:

```powershell
$ShowOnly = $false  # Set to $true for dry-run
# Paste the code from [[codes/Check-DotNet-Version-and-Launch-PowerShell-v2]] here
```

Save as Bypass.ps1 and run:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Bypass.ps1
```

**Expected Output**: If successful, a new PowerShell v2 window opens with prompt "PS Microsoft.PowerShell.Core\Program Files\Windows PowerShell\v1.0> " indicating v2 runtime. Verbose output shows ".Net version 2.0.50727 found." and "Executing the bypass."

### Step 3: Validate Elevated v2 Session and Perform Actions

**Context**: Once in the PowerShell v2 session, verify elevation and lack of logging. Use built-in cmdlets to confirm admin rights and test stealth by running a non-logged command (e.g., whoami /priv). This step ensures the bypass worked and allows chaining to reflection-based loads for further evasion.

In the new v2 session:

```powershell
whoami /groups | findstr "High Mandatory"
Get-ExecutionPolicy  # Should allow unrestricted or bypass
```

For reflection (per Graeber's method), load assemblies dynamically:

```powershell
Add-Type -AssemblyName System.Management.Automation; $runspace = [runspacefactory]::CreateRunspace(); $runspace.Open(); $ps = [powershell]::Create(); $ps.Runspace = $runspace; # Add scripts here
```

**Expected Output**: Output confirms "BUILTIN\Administrators" with high integrity. No new events in PowerShell operational logs for v2 actions.

### Step 4: Exit and Clean Up

**Context**: After completing objectives, exit the v2 session to minimize exposure. Check for any artifacts (e.g., temporary files) and ensure no persistent changes were made unless intended.

In the v2 session:

```powershell
exit
```

Review event logs manually or via script to confirm no logging occurred.

**Expected Output**: Session closes cleanly; no anomalous entries in Event Viewer under Applications and Services Logs > Microsoft > Windows > PowerShell.
