---
id: 0ab2b46e-a3fe-47fb-aa6c-596d75997eff
name: Discover-and-Impair-Windows-Defender-Antivirus
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.630716+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Security-Software-Discovery|T1063 - Security Software
    Discovery]]
  - >-
    [[techniques/Impair-Defenses-Disable-or-Modify-Tools|T1562.001 - Impair
    Defenses: Disable or Modify Tools]]
sub_techniques: []
tags:
  - '[[tags/Windows-Defender-Antivirus]]'
  - '[[tags/Windows-Defenses]]'
  - antivirus-evasion
  - defense-impairment
commands:
  - '[[commands/get-mpcomputerstatus-check-defender-status]]'
  - '[[commands/set-mppreference-disable-realtime-monitoring]]'
  - '[[commands/set-mppreference-exclude-paths-and-processes]]'
  - '[[commands/mpcmdrun-remove-definitions]]'
  - '[[commands/start-mpscan-quick-scan]]'
  - '[[commands/start-mpscan-full-scan]]'
  - '[[commands/set-mppreference-enable-realtime-protection]]'
platforms:
  - Windows
tools: []
validated: true
---

# Discover-and-Impair-Windows-Defender-Antivirus

## Summary

This procedure allows red team operators to discover the status of Windows Defender Antivirus on a target Windows system and impair its functionality by disabling real-time monitoring, excluding paths and processes from scanning, and removing signature definitions. It is useful during post-exploitation to evade detection while maintaining persistence or executing further payloads.

## Description

Windows Defender Antivirus is the default endpoint protection in modern Windows versions, providing real-time scanning, behavioral analysis, and cloud-backed threat intelligence. Attackers often need to discover its status to assess evasion requirements and then impair it to prevent detection of malicious activities. This procedure uses PowerShell cmdlets from the MpPreference module to query status, disable protections, add exclusions, and purge signatures via MpCmdRun.exe. It targets Windows 10/11/Server environments with administrative privileges. Success reduces the likelihood of malware detection but may trigger alerts if monitoring is in place. Note: Enabling scans can be used post-impairment to verify changes or simulate normal activity.

## Requirements

1. Administrative privileges on the target Windows system (local or domain admin).
2. PowerShell execution policy allowing script execution (bypass if needed via Set-ExecutionPolicy).
3. Access to the Windows Defender installation path (typically C:\Program Files\Windows Defender).
4. Windows 10 build 1709 or later, or Windows Server 2019+ with Defender enabled.

## Defense

- Enable advanced auditing for PowerShell and process creation to log MpPreference changes.
- Use Group Policy to restrict modifications to Defender settings and require approval for exclusions.
- Monitor for anomalous Defender status changes via Sysmon or EDR tools like Microsoft Defender for Endpoint.
- Regularly update signatures and review exclusion lists for unauthorized entries.

## Objectives

1. Identify if Windows Defender is active and its current protection levels.
2. Disable real-time scanning and script protection to allow payload execution.
3. Exclude specific paths and processes from scanning to protect tools and C2 infrastructure.
4. Remove signature definitions to clear known threat matches.
5. Optionally run scans to validate impairment or blend in with legitimate activity.

## Instructions

### Step 1: Check Windows Defender Status

**Context**: Begin by querying the current status of Windows Defender to determine if real-time protection is enabled, signature versions, and overall health. This helps assess the evasion needs.

**Command** ([[commands/get-mpcomputerstatus-check-defender-status]]):

```powershell
Get-MpComputerStatus
```

> This cmdlet returns details like AntivirusEnabled, RealTimeProtectionEnabled, and SignatureVersion. Use it to confirm if impairment is necessary.

### Step 2: Disable Real-Time Monitoring and Script Scanning

**Context**: Disable reactive protections like real-time file scanning and Antimalware Scan Interface (AMSI) to prevent immediate detection of scripts or downloads. This is a key evasion step before deploying payloads.

**Command** ([[commands/set-mppreference-disable-realtime-monitoring]]):

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisableScriptScanning $true
Get-MpComputerStatus
```

> Verify changes with the status check at the end. RealTimeProtectionEnabled should show False.

### Step 3: Exclude Paths and Processes from Scanning

**Context**: Add exclusions for directories containing tools (e.g., C:\Temp for payloads) and processes (e.g., word.exe for LOLBins) to avoid scans on critical files.

**Command** ([[commands/set-mppreference-exclude-paths-and-processes]]):

```powershell
Add-MpPreference -ExclusionPath "C:\Temp"
Add-MpPreference -ExclusionPath "C:\Windows\Tasks"
Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"
```

> Confirm exclusions via Get-MpPreference | Select ExclusionPath, ExclusionProcess. This prevents scanning of specified items.

### Step 4: Remove Signature Definitions

**Context**: Purge all antivirus signatures to eliminate matches for known malware. Note: If connected to the internet, signatures may redownload; disconnect or block updates first.

**Command** ([[commands/mpcmdrun-remove-definitions]]):

```powershell
& "C:\ProgramData\Microsoft\Windows Defender\Platform\*\MpCmdRun.exe" -RemoveDefinitions -All
& "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```

> Use the wildcard for the latest platform version. Expected output confirms removal; check status afterward to see SignatureVersion reset.

### Step 5: (Optional) Run Quick or Full Scan for Verification

**Context**: After impairment, run a scan to confirm no detections occur on test files, or to simulate benign activity.

**Command** ([[commands/start-mpscan-quick-scan]]):

```powershell
Start-MpScan -ScanType QuickScan
```

> Monitors common areas; should complete without threats if impairments worked.

**Command** ([[commands/start-mpscan-full-scan]]):

```powershell
Start-MpScan -ScanType FullScan
```

> Scans entire system; use cautiously as it may take time and could alert if partial protections remain.

### Step 6: (Optional) Re-Enable Protections Post-Testing

**Context**: For opsec, re-enable after use to avoid suspicion.

**Command** ([[commands/set-mppreference-enable-realtime-protection]]):

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -DisableScriptScanning $false
Get-MpComputerStatus
```

> Confirms protections are restored.
