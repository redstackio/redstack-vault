---
id: 6c1b0c09-93fd-44e0-ada5-5cefc39b5a84
name: Authentication Package
type: technique
mitre_id: T1131
mitre_url: null
created_at: '2019-08-28T21:17:24.698943+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Authentication Package

**MITRE ID**: T1131

## Description

Windows Authentication Package DLLs are loaded by the Local Security Authority (LSA) process at system start. They provide support for multiple logon processes and multiple security protocols to the operating system. [1]Adversaries can use the autostart mechanism provided by LSA Authentication Packages for persistence by placing a reference to a binary in the Windows Registry location HKLM\SYSTEM\CurrentControlSet\Control\Lsa\ with the key value of "Authentication Packages"=. The binary will then be executed by the system when the authentication packages are loaded.

# Detection

Monitor the Registry for changes to the LSA Registry keys. Monitor the LSA process for DLL loads. Windows 8.1 and Windows Server 2012 R2 may generate events when unsigned DLLs try to load into the LSA by setting the Registry key HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\LSASS.exe with AuditLevel = 8. [3] [4]

# Mitigation

Windows 8.1, Windows Server 2012 R2, and later versions, may make LSA run as a Protected Process Light (PPL) by setting the Registry key HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL, which requires all DLLs loaded by LSA to be signed by Microsoft. [3] [4]

# Footnotes

[1] Microsoft. (n.d.). Authentication Packages. Retrieved March 1, 2017.

[2] sKyWIper Analysis Team. (2012, May 31). sKyWIper (a.k.a. Flame a.k.a. Flamer):  A complex malware for targeted attacks. Retrieved September 6, 2018.

[3] Graeber, M. (2014, October). Analysis of Malicious Security Support Provider DLLs. Retrieved March 1, 2017.

[4] Microsoft. (2013, July 31). Configuring Additional LSA Protection. Retrieved June 24, 2015.

## Defense

Windows 8.1, Windows Server 2012 R2, and later versions, may make LSA run as a Protected Process Light (PPL) by setting the Registry key <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL</code>, which requires all DLLs loaded by LSA to be signed by

## Tactics

- [[Persistence|TA0003 - Persistence]]
