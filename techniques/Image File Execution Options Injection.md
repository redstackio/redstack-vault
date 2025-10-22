---
id: dc7d574a-19a6-456a-84dd-379b0de97828
name: Image File Execution Options Injection
type: technique
mitre_id: T1183
mitre_url: null
created_at: '2019-08-28T21:17:20.057831+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[JSON POST CSRF to Set Admin Role]]'
- '[[JSON POST CSRF to Set Admin Role]]'
- '[[Windows - Password Looting via Alternate Data Stream]]'
---

# Image File Execution Options Injection

**MITRE ID**: T1183

## Description

Image File Execution Options (IFEO) enable a developer to attach a debugger to an application. When a process is created, a debugger present in an application’s IFEO will be prepended to the application’s name, effectively launching the new process under the debugger (e.g., "C:\dbg\ntsd.exe -g  notepad.exe"). [1]IFEOs can be set directly via the Registry or in Global Flags via the GFlags tool. [2] IFEOs are represented as Debugger values in the Registry under HKLM\SOFTWARE{\Wow6432Node}\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ where  is the binary on which the debugger is attached. [1]IFEOs can also enable an arbitrary monitor program to be launched when a specified program silently exits (i.e. is prematurely terminated by itself or a second, non kernel-mode process). [3] [4] Similar to debuggers, silent exit monitoring can be enabled through GFlags and/or by directly modifying IEFO and silent process exit Registry values in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\. [3] [4]An example where the evil.exe process is started when notepad.exe exits: [4]reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\evil.exe"Similar to Process Injection, these values may be abused to obtain persistence and privilege escalation by causing a malicious executable to be loaded and run in the context of separate processes on the computer. [5] Installing IFEO mechanisms may also provide Persistence via continuous invocation.Malware may also use IFEO for Defense Evasion by registering invalid debuggers that redirect and effectively disable various system and security applications. [6] [7]

# Detection

Monitor for common processes spawned under abnormal parents and/or with creation flags indicative of debugging such as DEBUG_PROCESS and DEBUG_ONLY_THIS_PROCESS. [1]

Monitor Registry values associated with IFEOs, as well as silent process exit monitoring, for modifications that do not correlate with known software, patch cycles, etc. Monitor and analyze application programming interface (API) calls that are indicative of Registry edits such as RegCreateKeyEx and RegSetValueEx. [5]

# Mitigation

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating all IFEO will likely have unintended side effects, such as preventing legitimate software (i.e., security products) from operating properly. [9] Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior.

Identify and block potentially malicious software that may be executed through IFEO by using whitelisting [10] tools, like AppLocker, [11] [12] that are capable of auditing and/or blocking unknown executables.

# Footnotes

[1] Shanbhag, M. (2010, March 24). Image File Execution Options (IFEO). Retrieved December 18, 2017.

[2] Microsoft. (2017, May 23). GFlags Overview. Retrieved December 18, 2017.

[3] Marshall, D. & Griffin, S. (2017, November 28). Monitoring Silent Process Exit. Retrieved June 27, 2018.

[4] Moe, O. (2018, April 10). Persistence using GlobalFlags in Image File Execution Options - Hidden from Autoruns.exe. Retrieved June 27, 2018.

[5] Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.

[6] FSecure. (n.d.). Backdoor - W32/Hupigon.EMV - Threat Description. Retrieved December 18, 2017.

[7] Symantec. (2008, June 28). Trojan.Ushedix. Retrieved December 18, 2017.

[8] Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.

[9] Microsoft. (2015, July 30). Part of Windows 10 or really Malware?. Retrieved December 18, 2017.

[10] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[11] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[12] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

## Defense

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating all IFEO will likely have unintended side effects, such as preventing legitimate 

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (3)

- [[JSON POST CSRF to Set Admin Role]]
- [[JSON POST CSRF to Set Admin Role]]
- [[Windows - Password Looting via Alternate Data Stream]]
