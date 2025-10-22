---
id: 037563e7-dc6a-457f-83a3-c8cd85f1f9c7
name: DLL Search Order Hijacking
type: technique
mitre_id: T1038
mitre_url: null
created_at: '2019-08-28T21:17:37.442274+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abusing DNSAdmins Group to Change DNS Service DLL]]'
- '[[Enumerate Windows for Privilege Escalation (PowerUp)]]'
- '[[Windows - Privileged File Write via UsoDLLLoader]]'
- '[[Windows Privilege Escalation - Unquoted Service Paths]]'
- '[[Windows Unquoted Service Path Enumeration Vulnerability]]'
- '[[Windows - Unquoted Service Path Privilege Escalation]]'
---

# DLL Search Order Hijacking

**MITRE ID**: T1038

## Description

Windows systems use a common method to look for required DLLs to load into a program. [1] Adversaries may take advantage of the Windows DLL search order and programs that ambiguously specify DLLs to gain privilege escalation and persistence. Adversaries may perform DLL preloading, also called binary planting attacks, [2] by placing a malicious DLL with the same name as an ambiguously specified DLL in a location that Windows searches before the legitimate DLL. Often this location is the current working directory of the program. Remote DLL preloading attacks occur when a program sets its current directory to a remote location such as a Web share before loading a DLL. [3] Adversaries may use this behavior to cause the program to load a malicious DLL. Adversaries may also directly modify the way a program loads DLLs by replacing an existing DLL or modifying a .manifest or .local redirection file, directory, or junction to cause the program to load a different DLL to maintain persistence or privilege escalation. [4] [5] [6]If a search order-vulnerable program is configured to run at a higher privilege level, then the adversary-controlled DLL that is loaded will also be executed at the higher level. In this case, the technique could be used for privilege escalation from user to administrator or SYSTEM or from administrator to SYSTEM, depending on the program.Programs that fall victim to path hijacking may appear to behave normally because malicious DLLs may be configured to also load the legitimate DLLs they were meant to replace.

# Detection

Monitor file systems for moving, renaming, replacing, or modifying DLLs. Changes in the set of DLLs that are loaded by a process (compared with past behavior) that do not correlate with known software, patches, etc., are suspicious. Monitor DLLs loaded into a process and detect DLLs that have the same file name but abnormal paths. Modifications to or creation of .manifest and .local redirection files that do not correlate with software updates are suspicious.

# Mitigation

Disallow loading of remote DLLs. [21] This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+. [1] Path Algorithm

Enable Safe DLL Search Mode to force search for system DLLs in directories with greater restrictions (e.g. %SYSTEMROOT%)to be used before local directory DLLs (e.g. a user's home directory). The Safe DLL Search Mode can be enabled via Group Policy at Computer Configuration > [Policies] > Administrative Templates > MSS (Legacy): MSS: (SafeDllSearchMode) Enable Safe DLL search mode. The associated Windows Registry key for this is located at HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode [1]

Use auditing tools capable of detecting DLL search order hijacking opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for DLL hijacking weaknesses. [22]

Identify and block potentially malicious software that may be executed through search order hijacking by using whitelisting [23] tools like AppLocker [24] [25] that are capable of auditing and/or blocking unknown DLLs.

# Footnotes

[1] Microsoft. (n.d.). Dynamic-Link Library Search Order. Retrieved November 30, 2014.

[2] OWASP. (2013, January 30). Binary planting. Retrieved June 7, 2016.

[3] Microsoft. (2010, August 22). Microsoft Security Advisory 2269637 Released. Retrieved December 5, 2014.

[4] Microsoft. (n.d.). Dynamic-Link Library Redirection. Retrieved December 5, 2014.

[5] Microsoft. (n.d.). Manifests. Retrieved December 5, 2014.

[6] Mandiant. (2010, August 31). DLL Search Order Hijacking Revisited. Retrieved December 5, 2014.

[7] ESET. (2016, October). En Route with Sednit - Part 3: A Mysterious Downloader. Retrieved November 21, 2016.

[8] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[9] FinFisher. (n.d.). Retrieved December 20, 2017.

[10] Kaspersky Lab's Global Research & Analysis Team. (2017, October 16). BlackOasis APT and new targeted attacks leveraging zero-day exploit. Retrieved February 15, 2018.

[11] Desai, D.. (2015, August 14). Chinese cyber espionage APT group leveraging recently leaked Hacking Team exploits to target a Financial Services Firm. Retrieved January 26, 2016.

[12] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[13] PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.

[14] Rosenberg, J. (2018, June 14). MirageFox: APT15 Resurfaces With New Tools Based On Old Ones. Retrieved September 21, 2018.

[15] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[16] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[17] Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.

[18] FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.

[19] Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.

[20] Mandiant. (n.d.). Appendix C (Digital) - The Malware Arsenal. Retrieved July 18, 2016.

[21] Microsoft. (2010, August 12). More information about the DLL Preloading remote attack vector. Retrieved December 5, 2014.

[22] PowerSploit. (n.d.). Retrieved December 4, 2014.

[23] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[24] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[25] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

## Defense

Disallow loading of remote DLLs. (Citation: Microsoft DLL Preloading) This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+. (Citation: Microsoft DLL Search) Path Algorithm

Enable Safe DLL Search Mode to f

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (6)

- [[Abusing DNSAdmins Group to Change DNS Service DLL]]
- [[Enumerate Windows for Privilege Escalation (PowerUp)]]
- [[Windows - Privileged File Write via UsoDLLLoader]]
- [[Windows Privilege Escalation - Unquoted Service Paths]]
- [[Windows Unquoted Service Path Enumeration Vulnerability]]
- [[Windows - Unquoted Service Path Privilege Escalation]]
