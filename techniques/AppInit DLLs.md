---
id: a72c84b2-61e0-4fe3-ad14-03a45dcde0fe
name: AppInit DLLs
type: technique
mitre_id: T1103
mitre_url: null
created_at: '2019-08-28T21:17:32.792646+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[SSH Key Persistence]]'
---

# AppInit DLLs

**MITRE ID**: T1103

## Description

Dynamic-link libraries (DLLs) that are specified in the AppInit_DLLs value in the Registry keys HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows or HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows are loaded by user32.dll into every process that loads user32.dll. In practice this is nearly every program, since user32.dll is a very common library. [1] Similar to Process Injection, these values can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. [2]The AppInit DLL functionality is disabled in Windows 8 and later versions when secure boot is enabled. [3]

# Detection

Monitor DLL loads by processes that load user32.dll and look for DLLs that are not recognized or not normally loaded into a process. Monitor the AppInit_DLLs Registry values for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as RegCreateKeyEx and RegSetValueEx. [1] Tools such as Sysinternals Autoruns may also be used to detect system changes that could be attempts at persistence, including listing current AppInit DLLs. [9] 

Look for abnormal process behavior that may be due to a process loading a malicious DLL. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as making network connections for Command and Control, learning details about the environment through Discovery, and conducting Lateral Movement.

# Mitigation

Upgrade to Windows 8 or later and enable secure boot.

Identify and block potentially malicious software that may be executed through AppInit DLLs by using whitelisting [6] tools, like AppLocker, [7] [8] that are capable of auditing and/or blocking unknown DLLs.

# Footnotes

[1] Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.

[2] Microsoft. (2006, October). Working with the AppInit_DLLs registry value. Retrieved July 15, 2015.

[3] Microsoft. (n.d.). AppInit DLLs and Secure Boot. Retrieved July 15, 2015.

[4] Merritt, E.. (2015, November 16). Shining the Spotlight on Cherry Picker PoS Malware. Retrieved April 20, 2016.

[5] Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.

[6] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[7] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[8] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[9] Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.

## Defense

Upgrade to Windows 8 or later and enable secure boot.

Identify and block potentially malicious software that may be executed through AppInit DLLs by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands JPCERT) (C

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (1)

- [[SSH Key Persistence]]
