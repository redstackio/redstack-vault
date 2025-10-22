---
id: a029b831-f473-426f-9105-f9ae36487c13
name: Bypass User Account Control
type: technique
mitre_id: T1088
mitre_url: null
created_at: '2019-08-28T21:17:28.796851+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Active Directory Certificate Services ESC9 Attack]]'
- '[[Antivirus Enumeration - Windows Privilege Escalation]]'
- '[[Linux - Privilege Escalation via Capabilities]]'
- '[[Local Administrator to NT SYSTEM Privilege Escalation]]'
- '[[Meterpreter Get System]]'
- '[[Misconfigured Certificate Templates]]'
- '[[Pass-The-Certificate Attack]]'
- '[[Reflection Method with WMF5 Autologging Bypass]]'
- '[[Windows Privilege Escalation - Powershell History Looting]]'
- '[[Windows Startup Elevated Persistence via User Startup Folder]]'
---

# Bypass User Account Control

**MITRE ID**: T1088

## Description

Windows User Account Control (UAC) allows a program to elevate its privileges to perform a task under administrator-level permissions by prompting the user for confirmation. The impact to the user ranges from denying the operation under high enforcement to allowing the user to perform the action if they are in the local administrators group and click through the prompt or allowing them to enter an administrator password to complete the action. [1]If the UAC protection level of a computer is set to anything but the highest level, certain Windows programs are allowed to elevate privileges or execute some elevated COM objects without prompting the user through the UAC notification box. [2] [3] An example of this is use of rundll32.exe to load a specifically crafted DLL which loads an auto-elevated COM object and performs a file operation in a protected directory which would typically require elevated access. Malicious software may also be injected into a trusted process to gain elevated privileges without prompting a user. [4] Adversaries can use these techniques to elevate privileges to administrator if the target process is unprotected.Many methods have been discovered to bypass UAC. The Github readme page for UACMe contains an extensive list of methods [5] that have been discovered and implemented within UACMe, but may not be a comprehensive list of bypasses. Additional bypass methods are regularly discovered and some used in the wild, such as:eventvwr.exe can auto-elevate and execute a specified binary or script. [6] [7]Another bypass is possible through some Lateral Movement techniques if credentials for an account with administrator privileges are known, since UAC is a single system security mechanism, and the privilege or integrity of a process running on one system will be unknown on lateral systems and default to high integrity. [8]

# Detection

There are many ways to perform UAC bypasses when a user is in the local administrator group on a system, so it may be difficult to target detection on all variations. Efforts should likely be placed on mitigation and collecting enough information on process launches and actions that could be performed before and after a UAC bypass is performed. Monitor process API calls for behavior that may be indicative of Process Injection and unusual loaded DLLs through DLL Search Order Hijacking, which indicate attempts to gain access to higher privileged processes.

Some UAC bypass methods rely on modifying specific, user-accessible Registry settings. For example:

The eventvwr.exe bypass uses the [HKEY_CURRENT_USER]\Software\Classes\mscfile\shell\open\command Registry key. [6]The sdclt.exe bypass uses the [HKEY_CURRENT_USER]\Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe and [HKEY_CURRENT_USER]\Software\Classes\exefile\shell\runas\command\isolatedCommand Registry keys. [34] [35]

Analysts should monitor these Registry settings for unauthorized changes.

# Mitigation

Remove users from the local administrator group on systems. Although UAC bypass techniques exist, it is still prudent to use the highest enforcement level for UAC when possible and mitigate bypass opportunities that exist with techniques such as DLL Search Order Hijacking. 

Check for common UAC bypass weaknesses on Windows systems to be aware of the risk posture and address issues where appropriate. [5]

# Footnotes

[1] Lich, B. (2016, May 31). How User Account Control Works. Retrieved June 3, 2016.

[2] Russinovich, M. (2009, July). User Account Control: Inside Windows 7 User Account Control. Retrieved July 26, 2016.

[3] Microsoft. (n.d.). The COM Elevation Moniker. Retrieved July 26, 2016.

[4] Davidson, L. (n.d.). Windows 7 UAC whitelist. Retrieved November 12, 2014.

[5] UACME Project. (2016, June 16). UACMe. Retrieved July 26, 2016.

[6] Nelson, M. (2016, August 15). "Fileless" UAC Bypass using eventvwr.exe and Registry Hijacking. Retrieved December 27, 2016.

[7] Salvio, J., Joven, R. (2016, December 16). Malicious Macro Bypasses UAC to Elevate Privilege for Fareit Malware. Retrieved December 27, 2016.

[8] Medin, T. (2013, August 8). PsExec UAC Bypass. Retrieved June 3, 2016.

[9] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[10] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[11] F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.

[12] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[13] Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.

[14] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[15] ESET. (2016, October). En Route with Sednit - Part 3: A Mysterious Downloader. Retrieved November 21, 2016.

[16] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[17] FinFisher. (n.d.). Retrieved December 20, 2017.

[18] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[19] Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved September 26, 2016.

[20] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[21] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[22] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[23] ClearSky Cyber Security. (2018, November). MuddyWater Operations in Lebanon and Oman: Using an Israeli compromised domain for a two-stage campaign. Retrieved November 29, 2018.

[24] Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved August 3, 2016.

[25] Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.

[26] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[27] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[28] Bacurio, F., Salvio, J. (2017, February 14). REMCOS: A New RAT In The Wild. Retrieved November 6, 2018.

[29] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[30] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, July 30). Sakula Malware Family. Retrieved January 26, 2016.

[31] Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.

[32] Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.

[33] Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.

[34] Nelson, M. (2017, March 14). Bypassing UAC using App Paths. Retrieved May 25, 2017.

[35] Nelson, M. (2017, March 17). "Fileless" UAC Bypass Using sdclt.exe. Retrieved May 25, 2017.

## Defense

Remove users from the local administrator group on systems. Although UAC bypass techniques exist, it is still prudent to use the highest enforcement level for UAC when possible and mitigate bypass opportunities that exist with techniques such as [DLL Sear

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (10)

- [[Active Directory Certificate Services ESC9 Attack]]
- [[Antivirus Enumeration - Windows Privilege Escalation]]
- [[Linux - Privilege Escalation via Capabilities]]
- [[Local Administrator to NT SYSTEM Privilege Escalation]]
- [[Meterpreter Get System]]
- [[Misconfigured Certificate Templates]]
- [[Pass-The-Certificate Attack]]
- [[Reflection Method with WMF5 Autologging Bypass]]
- [[Windows Privilege Escalation - Powershell History Looting]]
- [[Windows Startup Elevated Persistence via User Startup Folder]]
