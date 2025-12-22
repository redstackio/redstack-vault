---
id: fa528ab6-8d18-428c-bb1a-6952e8531cf2
name: Bypass-PowerShell-Logging-with-Invisi-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T04:43:16.991778+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[PowerShell]]'
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - defense-evasion
  - powershell
  - amsi-bypass
  - logging-bypass
commands:
  - '[[commands/invisi-shell-run-with-path-as-admin]]'
  - '[[commands/invisi-shell-run-with-registry-non-admin]]'
  - '[[commands/load-powershell-from-cmd]]'
platforms:
  - Windows
tools:
  - '[[tools/Invisi-Shell]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# Bypass-PowerShell-Logging-with-Invisi-Shell

## Summary

This procedure uses Invisi-Shell to bypass PowerShell security features such as ScriptBlock logging, Module Logging, Transcription, and AMSI (Antimalware Scan Interface) within the current console session. It allows execution of PowerShell scripts without triggering logging or scanning, making it useful for evading detection during post-exploitation or red team operations on Windows systems.

## Description

Invisi-Shell is a .NET-based tool that injects obfuscated PowerShell code into memory to disable key security monitoring features. By running one of its batch launchers from a CMD prompt, it sets up an environment where subsequent PowerShell commands and scripts execute invisibly to standard logging mechanisms. This technique is particularly effective in environments with constrained PowerShell logging enabled via Group Policy. The bypass is session-specific and does not persist across new PowerShell instances. It targets Windows platforms where PowerShell is the primary scripting interpreter, enabling stealthy command execution for further actions like lateral movement or data exfiltration. Prerequisites include administrative or non-administrative access to run the batch files, and the tool must be downloaded and extracted locally.

## Requirements

1. Windows operating system (Windows 7 or later, tested on Windows 10/11).
2. Access to a CMD prompt with execute permissions on the local directory.
3. Download and extraction of the Invisi-Shell tool from its GitHub repository.
4. For admin variant: Elevated privileges (Run as Administrator).
5. .NET Framework 4.0 or later installed (required for Invisi-Shell binaries).

## Defense

Defensive measures and detection strategies:

- Enable PowerShell Constrained Language Mode via AppLocker or WDAC to restrict unsigned scripts.
- Monitor for unusual process injections or memory modifications using EDR tools like Sysmon (Event ID 8 for CreateRemoteThread) or Windows Defender ATP.
- Audit CMD executions of batch files from temporary directories and correlate with PowerShell launches.
- Implement AMSI enhancements and script block logging at the host level, watching for attempts to unload AMSI.dll.
- Use behavioral analytics to detect PowerShell sessions without corresponding logging events.

## Objectives

1. Disable ScriptBlock, Module, and Transcription logging in the current PowerShell session.
2. Bypass AMSI scanning for script execution.
3. Establish a stealthy PowerShell environment for running undetected commands.
4. Verify the bypass by executing a test script without logging.

## Instructions

### Step 1: Download and Prepare Invisi-Shell

**Context**: Obtain the Invisi-Shell tool and extract it to a local directory. This ensures the batch files are available for execution. The tool must be cloned or downloaded from the official repository to avoid tampered versions.

Navigate to a working directory in CMD and download the tool.

**Command** (use standard git or manual download):

```bash
# Assuming git is available; otherwise, download ZIP from GitHub
mkdir C:\temp\invisi-shell
cd C:\temp\invisi-shell
git clone https://github.com/OmerYa/Invisi-Shell.git
cd Invisi-Shell
# Build if source; or use precompiled binaries if available
```

> This step prepares the environment. Expected output is the cloned repository with batch files like RunWithPathAsAdmin.bat and RunWithRegistryNonAdmin.bat. If building from source, compile the .NET project using Visual Studio or msbuild.

### Step 2: Execute Invisi-Shell Launcher Based on Privileges

**Context**: Run the appropriate batch file to load Invisi-Shell into memory. Use the admin version if elevated privileges are available for broader bypass coverage; otherwise, use the non-admin version which relies on registry modifications.

For non-admin users:

**Command** ([[commands/invisi-shell-run-with-registry-non-admin]]):

```command_prompt
RunWithRegistryNonAdmin.bat
```

For admin users:

**Command** ([[commands/invisi-shell-run-with-path-as-admin]]):

```command_prompt
RunWithPathAsAdmin.bat
```

> The batch file will execute silently or with minimal output, loading the Invisi-Shell DLL into the process. Expected output: No errors, and the CMD prompt returns without visible changes. Success is confirmed by the lack of logging in subsequent PowerShell activity. If errors occur (e.g., missing .NET), install prerequisites.

### Step 3: Launch PowerShell in the Bypassed Session

**Context**: From the same CMD prompt where Invisi-Shell was loaded, start a new PowerShell instance. This inherits the bypass environment, allowing script execution without detection.

**Command** ([[commands/load-powershell-from-cmd]]):

```command_prompt
powershell
```

> This opens a PowerShell prompt (PS C:\...>). Expected output: Standard PowerShell banner. Test the bypass by running a simple script like `Write-Host 'Test'` and verify no logs are generated in Event Viewer (under Applications and Services Logs > Microsoft > Windows > PowerShell). If logging still occurs, reload Invisi-Shell or check privileges.

### Step 4: Verify Bypass and Execute Scripts

**Context**: Confirm the logging bypass works by running a test command or script. This step includes decision points: If admin access is detected, use advanced tests; otherwise, stick to basic verification.

In the PowerShell session, execute a test:

```powershell
# Test script
Get-Process | Out-File -FilePath C:\temp\test.txt
```

> Expected output: File created without AMSI alerts or script block logs. Check Event Viewer for absence of PowerShell events (ID 4103/4104). If logs appear, the bypass failed—revert to Step 2 and ensure correct batch file. For cleanup, exit the session and delete temporary files.
