---
type: procedure
description: >-
  Enumerates the effective AppLocker policy on a Windows system to identify
  application restrictions and potential weaknesses.
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.394472+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - '[[tags/AppLocker]]'
  - '[[tags/Windows - Defenses]]'
commands:
  - '[[commands/powershell-get-applockerpolicy-rulecollections]]'
  - '[[commands/powershell-get-applockerpolicy-xml]]'
  - '[[commands/powershell-enumerate-applocker-registry-keys]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
---

# AppLocker-Policy-Enumeration

## Summary

This procedure enumerates the effective AppLocker policy on a Windows system, revealing which applications, scripts, and executables are permitted to run. By identifying allowed paths, publishers, and file hashes, attackers can assess restrictions and locate bypass opportunities, such as unmonitored directories or weak rules, aiding in planning subsequent execution or persistence actions.

## Description

AppLocker is a Windows security feature that enforces application control through whitelisting rules based on file paths, hashes, publishers, or extensions. It operates via Group Policy and is commonly deployed in enterprise environments to prevent unauthorized software execution. This procedure uses native PowerShell cmdlets and registry queries to retrieve the effective policy without requiring external tools. The output provides insights into rule collections for executables (Exe), DLLs, scripts (Script), MSI installers, and packaged apps (Appx). In an attack scenario, this enumeration occurs during discovery phases on compromised hosts to understand defensive postures and identify viable payload deployment paths. Prerequisites include local or remote access with sufficient privileges to query system policies, typically non-admin but may require elevated rights for full registry access. Expected outcomes include a list of enforced rules, enabling attackers to craft compliant payloads or exploit gaps.

## Requirements

1. Access to a Windows system (Windows 7+ Enterprise/Ultimate editions or Server 2008 R2+ where AppLocker is enabled).
2. PowerShell execution permissions (bypass execution policy if restricted).
3. Local or remote shell access (e.g., via WinRM, RDP, or existing foothold).
4. Optional: Administrative privileges for complete registry enumeration if policies are locked.

## Defense

Defensive measures and detection strategies:

- Enable and properly configure AppLocker with strict whitelisting rules, regularly auditing for gaps.
- Implement least privilege principles to restrict PowerShell and registry access on sensitive systems.
- Monitor PowerShell execution logs (Module Logging, Script Block Logging) for Get-AppLockerPolicy invocations and registry queries to HKLM:\SOFTWARE\Policies\Microsoft\Windows\SrpV2.
- Use endpoint detection tools to alert on enumeration of security policies (e.g., via Sysmon Event ID 1 for process creation of powershell.exe with suspicious arguments).

## Objectives

1. Retrieve the effective AppLocker policy details from the target system.
2. Identify weaknesses such as overly permissive rules, unmonitored paths, or missing rule types.
3. Inform attack planning by determining allowable execution contexts for payloads or tools.

## Instructions

### Step 1: Retrieve AppLocker Rule Collections

**Context**: This step fetches the core rule collections from the effective policy, showing high-level restrictions for different file types like executables and scripts. It helps quickly assess the breadth of enforcement without parsing XML.

**Command** ([[commands/powershell-get-applockerpolicy-rulecollections]]):
```powershell
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
```

> This command queries the active policy and expands the RuleCollections property, displaying individual rules. If no policy is enforced, it returns empty or default results. Use this to verify if AppLocker is active and review rule enforcement levels (e.g., Allow or Deny).

### Step 2: Export AppLocker Policy to XML

**Context**: For a detailed, parseable view of the policy, including conditions and exceptions, export it in XML format. This is useful for offline analysis or scripting further enumeration.

**Command** ([[commands/powershell-get-applockerpolicy-xml]]):
```powershell
Get-AppLockerPolicy -Effective -Xml
```

> The output is a complete XML representation of the policy, including <RuleCollection> elements for each type (Exe, Dll, etc.). Success is indicated by valid XML without errors; pipe to a file (e.g., | Out-File policy.xml) for review. This reveals granular details like publisher certificates or hash values not visible in the summary view.

### Step 3: Enumerate AppLocker Registry Keys

**Context**: AppLocker configurations are stored in the registry under SrpV2 keys. Querying these directly provides raw policy data, especially useful if PowerShell cmdlets are blocked or for scripting automation. Check subkeys for specific rule types to identify allowed paths or exceptions.

**Command** ([[commands/powershell-enumerate-applocker-registry-keys]]):
```powershell
Get-ChildItem -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\SrpV2"
```

> This lists top-level keys (e.g., Appx, Dll, Exe, Msi, Script). For each, run Get-ItemProperty or Get-ChildItem on subpaths (e.g., Exe\Rules) to view specific rules. Expected output includes key names and values indicating enforcement (e.g., Levels DWORD for policy mode). If keys are absent, AppLocker may not be configured. Repeat for each subkey to map full restrictions; decision point: If a key like Exe shows permissive paths (e.g., %OSDRIVE%\Program Files), target those for payload placement.
