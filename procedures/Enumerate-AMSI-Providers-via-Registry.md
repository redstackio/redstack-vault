---
id: 3b6879a1-3806-4d09-99d2-dc09487e10d2
name: Enumerate-AMSI-Providers-via-Registry
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.873815+00:00'
updated_at: '2023-04-10T20:36:15.809810+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Software Discovery|T1518 - Software Discovery]]'
sub_techniques: []
tags:
  - '[[tags/AMSI Bypass]]'
  - '[[tags/List AMSI Providers]]'
commands:
  - '[[codes/get-clsid-registry-info-powershell]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-AMSI-Providers-via-Registry

## Summary

This procedure enumerates the Anti-Malware Scan Interface (AMSI) providers installed on a Windows system by querying the registry for the specific CLSID associated with AMSI hosting applications. It reveals details such as the DLL path used by the provider, helping attackers identify active security software like Windows Defender for potential bypass strategies during post-exploitation or evasion phases.

## Description

AMSI is a Windows interface that enables applications to integrate with antimalware products for scanning scripts and content in real-time. The CLSID {2781761E-28E0-4109-99FE-B9D127C57AFE} corresponds to the AMSI provider interface, and querying its registry key under HKLM:\SOFTWARE\Classes\CLSID exposes information about registered providers, including the InprocServer32 path to the scanning DLL (e.g., MpOav.dll for Windows Defender). This discovery technique is useful in red team engagements to map the target's endpoint protection landscape, assess bypass viability (e.g., via DLL unloading or patching), and tailor subsequent attacks to evade detection. It requires local execution on the target and assumes no advanced EDR blocking PowerShell registry access. In a full attack chain, this fits after initial access and before script-based execution or persistence.

## Requirements

1. Local execution access on a Windows target (e.g., via compromised user or admin shell).
2. PowerShell 3.0 or later available on the system.
3. Administrative privileges may be needed for full registry read access, though standard users can often query HKLM.
4. No external tools required; uses built-in PowerShell.

## Defense

- Keep antimalware solutions like Windows Defender updated to patch known bypasses and monitor for registry queries targeting AMSI CLSIDs.
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to detect anomalous registry access.
- Implement application whitelisting (e.g., AppLocker) to restrict PowerShell execution from untrusted contexts.
- Monitor for process creation events involving PowerShell accessing security-related registry keys.

## Objectives

1. Identify installed AMSI providers and their DLL paths to understand the target's scanning capabilities.
2. Assess potential AMSI bypass opportunities based on the detected provider (e.g., targeting Windows Defender specifics).
3. Gather intelligence for evasion in subsequent attack steps, such as loading malicious scripts.

## Instructions

### Step 1: Query AMSI CLSID Registry Key

**Context**: Retrieve the registry details for the AMSI provider CLSID to list hosting applications and the associated scanning DLL. This step exposes the active provider without triggering scans, as it's a passive read operation.

**Command** ([[codes/get-clsid-registry-info-powershell]]):
```powershell
Get-ChildItem -Path 'HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}'
```

> This PowerShell cmdlet uses Get-ChildItem to enumerate subkeys under the specified CLSID path in the HKLM hive. The 'Hosts' property lists scanned applications, while 'InprocServer32' reveals the DLL path (e.g., for MpOav.dll in Windows Defender). Run this in an interactive PowerShell session or script. If the key exists, it confirms AMSI integration; absence may indicate a tampered or unsupported system.

**Expected Output**:
```
Name                           Property
----                           --------
Hosts                          (default) : Scanned Hosting Applications
InprocServer32                 (default) : "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2210.4-0\MpOav.dll"
```

### Step 2: Interpret and Verify Results

**Context**: Analyze the output to confirm the provider and plan next actions. Cross-reference the DLL path with known providers (e.g., search for the file version or signature) to identify the exact antimalware product.

**Instructions**: If the output shows a Defender path, note the version for targeted bypass research. Use additional commands like Get-ItemProperty on the InprocServer32 subkey for more details if needed. Verify by checking if the DLL exists on disk with Test-Path 'C:\ProgramData\Microsoft\Windows Defender\Platform\*\MpOav.dll'.

**Expected Output**: Confirmation of DLL existence and version, e.g., file properties indicating Windows Defender integration.

**Success Indicators**:
- Registry key found with non-empty InprocServer32 property.
- DLL path points to a recognizable antimalware component (e.g., Defender, third-party AV).
