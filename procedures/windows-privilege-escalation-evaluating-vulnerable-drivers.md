---
id: 2492177b-707f-4d70-9e06-992f79543cb1
name: windows-privilege-escalation-evaluating-vulnerable-drivers
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.805756+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - '[[tags/eop-evaluating-vulnerable-drivers]]'
  - '[[tags/windows-privilege-escalation]]'
commands:
  - '[[commands/driverquery-list-drivers-table-format]]'
  - '[[commands/driverquery-custom-enumerate-non-msft-drivers]]'
platforms:
  - Windows
tools:
  - '[[tools/OffensiveCSharp-DriverQuery]]'
validated: true
---

# windows-privilege-escalation-evaluating-vulnerable-drivers

## Summary

This procedure identifies potentially vulnerable third-party drivers on a Windows system that could be exploited for privilege escalation. By enumerating installed drivers and verifying their digital signatures, attackers can spot unsigned or outdated drivers known to have exploitable flaws, enabling kernel-level access from a low-privilege context.

## Description

Evaluating vulnerable drivers is a common privilege escalation technique in Windows environments, targeting kernel-mode drivers that run with high privileges. Attackers with initial low-privilege access (e.g., via user account) enumerate the driver list to identify non-Microsoft drivers, check for valid signatures, and research known vulnerabilities (e.g., via CVE databases). Exploitable drivers allow arbitrary code execution in kernel space, bypassing user-mode restrictions. This procedure focuses on discovery and evaluation, assuming subsequent exploitation via tools like those in the PrintNightmare or similar driver vuln chains. It requires command-line access and is effective on unpatched enterprise systems with legacy hardware drivers.

## Requirements

1. Low-privilege shell access on a Windows target (e.g., standard user account).
2. Ability to execute built-in Windows commands (driverquery.exe) and custom binaries (DriverQuery.exe).
3. Network access optional for downloading the custom tool if not pre-staged.
4. Administrative privileges not required for enumeration, but needed for exploitation post-evaluation.

## Defense

- Regularly scan and update third-party drivers using tools like Windows Update or vendor patches to close known vulnerabilities.
- Implement driver signature enforcement via Group Policy (e.g., enable Secure Boot and disable test signing) to block unsigned drivers.
- Monitor for anomalous driver loads using EDR solutions like Sysmon (Event ID 6 for driver loads) or Windows Defender ATP, alerting on unsigned or mismatched signatures.
- Apply least privilege by restricting driver installations to admins and using AppLocker to whitelist approved drivers.

## Objectives

1. Enumerate all installed drivers to establish a baseline of system drivers.
2. Identify and analyze non-Microsoft drivers for missing or invalid signatures indicating potential vulnerabilities.
3. Flag drivers for further research into exploitable CVEs to enable privilege escalation paths.

## Instructions

### Step 1: Enumerate All Installed Drivers

**Context**: Start by using the built-in Windows utility to list all drivers in a readable table format, including signature information. This provides an overview of kernel and user-mode drivers, helping identify third-party ones for deeper analysis. The /si flag includes signature details to spot any immediately suspicious entries.

**Command** ([[commands/driverquery-list-drivers-table-format]]):
```cmd
driverquery.exe /fo table /si
```

> This command outputs a table with module names, display names, driver types, link dates, and signature status. Look for non-Microsoft drivers (e.g., those from Citrix, hardware vendors) with 'Unsigned' or expired certs. Redirect output to a file for offline review if needed: `driverquery.exe /fo table /si > drivers.txt`. Success is confirmed by a complete table without errors; incomplete output may indicate restricted access.

### Step 2: Analyze Non-Microsoft Drivers for Signatures

**Context**: Use a custom enumeration tool to filter out Microsoft-signed drivers and perform detailed signature verification on third-party ones. This step reveals service names, file paths, versions, and certificate details, making it easier to cross-reference with vulnerability databases like Exploit-DB or NVD for known exploits (e.g., CVE-2021-21551 for Dell drivers).

**Tool** ([[tools/OffensiveCSharp-DriverQuery]]): Ensure the DriverQuery.exe binary is available in your working directory or PATH.

**Command** ([[commands/driverquery-custom-enumerate-non-msft-drivers]]):
```cmd
DriverQuery.exe --no-msft
```

> The --no-msft flag excludes built-in Microsoft drivers, focusing on potentially vulnerable third-party ones. Expected output includes details like service name, path, version, creation time, cert issuer, and signer for each driver. For example, a Citrix driver might show: 'Service Name: ctxusbm, Path: C:\Windows\system32\DRIVERS\ctxusbm.sys, Signer: Citrix Systems, Inc.'. Manually review for outdated versions or self-signed certs. If a driver lacks a valid signature or matches a known vuln, note it for exploitation (e.g., load a malicious DLL via the driver).

### Step 3: Validate and Research Identified Drivers

**Context**: Cross-check suspicious drivers against public resources to confirm exploitability. This decision point determines if escalation is viable; if no vulns found, pivot to other privesc methods like token impersonation.

**Instructions**: From the outputs of Steps 1 and 2, extract driver names/versions (e.g., ctxusbm.sys v14.11.0.138). Search online (e.g., 'ctxusbm.sys vulnerability') or use tools like WinPEAS for automated vuln checks. If a CVE is found (e.g., buffer overflow allowing ring0 shellcode), proceed to exploit development or use existing PoCs.

> No specific command here, but verify by confirming at least one driver with a known exploit path. Success: List of 1+ candidate drivers with CVE references; failure: All drivers patched/signed, requiring alternative tactics.
