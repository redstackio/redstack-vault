---
id: 48fc38ca-9f70-40b7-a7e1-8cba0a433d6a
name: Security Support Provider
type: technique
mitre_id: T1101
mitre_url: null
created_at: '2019-08-28T21:17:46.415406+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[HTAccess and PHP Shell Upload]]'
- '[[JavaScript Alert WAF Bypass]]'
- '[[SQL Injection - Bypassing Space Filter and Selecting All Users]]'
- '[[SQL Injection WAF Bypass using Case Modification]]'
---

# Security Support Provider

**MITRE ID**: T1101

## Description

Windows Security Support Provider (SSP) DLLs are loaded into the Local Security Authority (LSA) process at system start. Once loaded into the LSA, SSP DLLs have access to encrypted and plaintext passwords that are stored in Windows, such as any logged-on user's Domain password or smart card PINs. The SSP configuration is stored in two Registry keys: HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages and HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages. An adversary may modify these Registry keys to add new SSPs, which will be loaded the next time the system boots, or when the AddSecurityPackage Windows API function is called. [1]

# Detection

Monitor the Registry for changes to the SSP Registry keys. Monitor the LSA process for DLL loads. Windows 8.1 and Windows Server 2012 R2 may generate events when unsigned SSP DLLs try to load into the LSA by setting the Registry key HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\LSASS.exe with AuditLevel = 8. [1] [6]

# Mitigation

Windows 8.1, Windows Server 2012 R2, and later versions may make LSA run as a Protected Process Light (PPL) by setting the Registry key HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL, which requires all SSP DLLs to be signed by Microsoft. [1] [6]

# Footnotes

[1] Graeber, M. (2014, October). Analysis of Malicious Security Support Provider DLLs. Retrieved March 1, 2017.

[2] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[3] Deply, B. (n.d.). Mimikatz. Retrieved September 29, 2015.

[4] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[5] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[6] Microsoft. (2013, July 31). Configuring Additional LSA Protection. Retrieved June 24, 2015.

## Defense

Windows 8.1, Windows Server 2012 R2, and later versions may make LSA run as a Protected Process Light (PPL) by setting the Registry key <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL</code>, which requires all SSP DLLs to be signed by Microsoft.

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (4)

- [[HTAccess and PHP Shell Upload]]
- [[JavaScript Alert WAF Bypass]]
- [[SQL Injection - Bypassing Space Filter and Selecting All Users]]
- [[SQL Injection WAF Bypass using Case Modification]]
