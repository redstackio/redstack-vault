---
id: 3146a3a4-e54d-4089-9cbd-1d2f41bbcb71
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Windows Management Instrumentation]]'
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - Enumeration
  - Operating Systems
commands:
  - '[[commands/wmic-query-installed-hotfixes]]'
  - '[[commands/systeminfo-display-system-configuration]]'
  - '[[commands/powershell-get-hotfix-sorted]]'
  - '[[commands/powershell-sherlock-find-allvulns]]'
platforms:
  - Windows
tools:
  - '[[tools/Sherlock]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# search-windows-installed-patches-hotfixes

## Summary

This procedure enumerates installed patches and hotfixes on a Windows system to identify potential vulnerabilities from missing updates. Attackers use this information to determine exploitable weaknesses, such as unpatched software flaws, by comparing installed KB numbers against known vulnerability databases.

## Description

Unpatched Windows systems are prime targets for exploitation due to known vulnerabilities in outdated components. This procedure leverages built-in Windows tools like WMIC, Systeminfo, and PowerShell cmdlets to query installed hotfixes, providing a list of KB updates that can be cross-referenced with CVE databases. For automated analysis, it also incorporates the Sherlock script, which not only lists patches but suggests potential exploits based on missing ones. This is typically performed during the discovery phase after initial access to a host, helping prioritize further attacks like privilege escalation or lateral movement. The technique relies on legitimate system queries, making it stealthy but detectable through command logging.

## Requirements

1. Local or remote access to a Windows system (e.g., via RDP, SSH, or compromised shell).
2. Execution privileges in Command Prompt or PowerShell (no admin rights required for basic queries).
3. For Sherlock: Internet access to download the script and PowerShell execution policy allowing script imports (bypass with Set-ExecutionPolicy if needed).
4. Optional: Access to a vulnerability database like Exploit-DB or NIST NVD for cross-referencing KB numbers.

## Defense

- Enable PowerShell logging and module logging to capture cmdlet executions like Get-HotFix.
- Monitor process creation for WMIC and systeminfo via Sysmon or EDR tools.
- Implement application whitelisting to restrict unsigned script execution like Sherlock.
- Regularly audit and patch systems using WSUS or similar to minimize missing hotfix exposure.

## Objectives

1. Retrieve a complete list of installed hotfixes to assess patch status.
2. Identify missing patches by comparing against expected updates for the OS version.
3. Automate vulnerability detection to suggest exploitable weaknesses.
4. Validate system security posture for targeted exploitation planning.

## Instructions

### Step 1: Query Installed Hotfixes Using WMIC

**Context**: WMIC provides a quick, tabular view of hotfixes using Windows Management Instrumentation, ideal for environments where PowerShell is restricted. This step lists key details like HotFixID and installation date to spot recent or missing updates.

**Command** ([[commands/wmic-query-installed-hotfixes]]):
```command_prompt
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

> Run this in Command Prompt to generate a list of all quick fixes (QFE). Review the HotFixID column for KB numbers and compare against known vulnerable KBs (e.g., KB4500331 for EternalBlue). If the output is empty or incomplete, it may indicate an unpatched system.

### Step 2: Retrieve System Configuration Including Hotfixes Using Systeminfo

**Context**: Systeminfo offers a comprehensive system overview, including a Hotfix(s) section, useful as a fallback when WMIC is unavailable or blocked. It provides context like OS version to better interpret patch relevance.

**Command** ([[commands/systeminfo-display-system-configuration]]):
```command_prompt
systeminfo
```

> Execute in Command Prompt; scroll to the Hotfix(s) section for a numbered list of installed KBs. Cross-reference with the OS version (from the top of output) to identify gaps, such as missing security updates for the build.

### Step 3: List and Sort Hotfixes Using PowerShell

**Context**: PowerShell's Get-HotFix cmdlet delivers structured output for easier parsing and sorting, allowing attackers to quickly identify the latest patches or gaps. This is more reliable than WMIC on modern Windows versions.

**Command** ([[commands/powershell-get-hotfix-sorted]]):
```powershell
Get-HotFix | Sort-Object HotFixID
```

> This outputs a sorted table by HotFixID, showing description, installer, and date. Export to file if needed (e.g., | Export-Csv patches.csv) for offline analysis. Success is confirmed by seeing KB entries; absence of recent security KBs indicates vulnerabilities.

### Step 4: Automate Enumeration and Vulnerability Detection Using Sherlock

**Context**: Sherlock is a PowerShell script that imports as a module and runs comprehensive checks, including patch enumeration, to flag missing updates and suggest exploits. This step requires downloading the script first for automated insights beyond manual queries.

**Instructions**: Download Sherlock.ps1 from the official GitHub repository using [[tools/Sherlock]]. Then, in PowerShell:
1. Navigate to the download directory and import: `Import-Module .\Sherlock.ps1` (or `. .\Sherlock.ps1` for dot-sourcing).
2. If execution policy blocks, run `Set-ExecutionPolicy Bypass -Scope Process` first.

**Command** ([[commands/powershell-sherlock-find-allvulns]]):
```powershell
Find-AllVulns
```

> This runs all vulnerability checks, outputting potential issues like 'MS17-010: Missing' with exploit suggestions. Review for high-impact vulns tied to missing patches; success is a report listing exploitable conditions.
