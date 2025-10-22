---
id: 3b6879a1-3806-4d09-99d2-dc09487e10d2
name: AMSI Provider Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.873815+00:00'
updated_at: '2023-04-10T20:36:15.809810+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Software Discovery|T1518 - Software Discovery]]'
tags:
- '[[AMSI Bypass]]'
- '[[List AMSI Providers]]'
commands:
- '[[Retrieve registry information for CLSID {2781761E-28E0-4109-99FE-B9D127C57AFE}]]'
---

# AMSI Provider Enumeration

## Summary

The AMSI Provider Enumeration procedure involves listing the Anti-Malware Scan Interface (AMSI) providers installed on a system. This technique can be used by an attacker to identify the security software running on a target machine and potentially bypass it. By identifying the specific AMSI provid

## Description

# Description

The AMSI Provider Enumeration procedure involves listing the Anti-Malware Scan Interface (AMSI) providers installed on a system. This technique can be used by an attacker to identify the security software running on a target machine and potentially bypass it. By identifying the specific AMSI providers installed, an attacker can determine which AMSI bypass techniques will be successful. This procedure can be used as part of a larger attack campaign to evade detection and compromise a target system.

Technical Explanation: AMSI is a Windows feature that allows applications to integrate with antivirus and other security software to scan for malicious code. AMSI is designed to provide a standard interface for scanning scripts and other code, allowing security software to detect and prevent malicious activity. However, attackers can potentially bypass AMSI by disabling or modifying the AMSI providers on a system. By listing the AMSI providers installed, an attacker can determine which bypass techniques are likely to be successful.

Business Value: This procedure can be used by attackers to evade detection and compromise a target system. By identifying the specific AMSI providers installed, an attacker can determine which AMSI bypass techniques will be successful, allowing them to avoid detection by security software. Successful compromise of a target system can result in data theft, financial loss, and reputational damage.

## Requirements

1. Access to the target system

1. Privileged access to execute commands

1. PowerShell or other scripting tools

## Defense

1. Ensure that security software is up-to-date and configured to detect and prevent AMSI bypass techniques

1. Implement security controls to prevent unauthorized access to systems and sensitive data

1. Monitor for suspicious activity, such as attempts to modify or disable AMSI providers

## Objectives

1. Identify the AMSI providers installed on a target system

1. Determine which AMSI bypass techniques are likely to be successful

# Instructions

1. Use this command to retrieve information about software from a CLSID.

**Code**: [[Get-ChildItem -Path 'HKLM:\SOFTWARE\Classes\CLSID\]]

> The CLSID (Class ID) is a unique identifier assigned by Microsoft to identify a software component. This command retrieves information about a software component from its CLSID. The command uses the Get-ChildItem cmdlet to retrieve information from the registry path 'HKLM:\SOFTWARE\Classes\CLSID\{CLSID}'. The returned information includes the name and property of the software component. This command can be useful in troubleshooting issues related to software components.

**Command** ([[Retrieve registry information for CLSID {2781761E-28E0-4109-99FE-B9D127C57AFE}]]):

```bash
Get-ChildItem -Path 'HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}'
Name                           Property
----                           --------
Hosts                          (default) : Scanned Hosting Applications
InprocServer32                 (default) : "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2210.4-0\MpOav.dll"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Software Discovery|T1518 - Software Discovery]]

## Commands Used

- [[Retrieve registry information for CLSID {2781761E-28E0-4109-99FE-B9D127C57AFE}]]

## Tags

- [[AMSI Bypass]]
- [[List AMSI Providers]]
