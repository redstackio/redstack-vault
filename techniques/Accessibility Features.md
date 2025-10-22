---
id: 401383de-3d2d-4b03-a47f-5a485da95a42
name: Accessibility Features
type: technique
mitre_id: T1015
mitre_url: null
created_at: '2019-08-28T21:17:38.028958+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Werkzeug Debugger Panel Read/Write RCE]]'
- '[[Windows - Elevated RDP Backdoor with Sticky Keys]]'
- '[[Windows - RDP Backdoor using utilman.exe]]'
- '[[Windows Registry HKLM Winlogon Helper DLL Persistence]]'
- '[[Windows Sticky Keys Persistence]]'
---

# Accessibility Features

**MITRE ID**: T1015

## Description

Windows contains accessibility features that may be launched with a key combination before a user has logged in (for example, when the user is on the Windows logon screen). An adversary can modify the way these programs are launched to get a command prompt or backdoor without logging in to the system.Two common accessibility programs are C:\Windows\System32\sethc.exe, launched when the shift key is pressed five times and C:\Windows\System32\utilman.exe, launched when the Windows + U key combination is pressed. The sethc.exe program is often referred to as "sticky keys", and has been used by adversaries for unauthenticated access through a remote desktop login screen. [1]Depending on the version of Windows, an adversary may take advantage of these features in different ways because of code integrity enhancements. In newer versions of Windows, the replaced binary needs to be digitally signed for x64 systems, the binary must reside in %systemdir%\, and it must be protected by Windows File or Resource Protection (WFP/WRP). [2] The debugger method was likely discovered as a potential workaround because it does not require the corresponding accessibility feature binary to be replaced. Examples for both methods:For simple binary replacement on Windows XP and later as well as and Windows Server 2003/R2 and later, for example, the program (e.g., C:\Windows\System32\utilman.exe) may be replaced with "cmd.exe" (or another program that provides backdoor access). Subsequently, pressing the appropriate key combination at the login screen while sitting at the keyboard or when connected over Remote Desktop Protocol will cause the replaced file to be executed with SYSTEM privileges. [3]For the debugger method on Windows Vista and later as well as Windows Server 2008 and later, for example, a Registry key may be modified that configures "cmd.exe," or another program that provides backdoor access, as a "debugger" for the accessibility program (e.g., "utilman.exe"). After the Registry is modified, pressing the appropriate key combination at the login screen while at the keyboard or when connected with RDP will cause the "debugger" program to be executed with SYSTEM privileges. [3]Other accessibility features exist that may also be leveraged in a similar fashion: [2]On-Screen Keyboard: C:\Windows\System32\osk.exeMagnifier: C:\Windows\System32\Magnify.exeNarrator: C:\Windows\System32\Narrator.exeDisplay Switcher: C:\Windows\System32\DisplaySwitch.exeApp Switcher: C:\Windows\System32\AtBroker.exe

# Detection

Changes to accessibility utility binaries or binary paths that do not correlate with known software, patch cycles, etc., are suspicious. Command line invocation of tools capable of modifying the Registry for associated keys are also suspicious. Utility arguments and the binaries themselves should be monitored for changes. Monitor Registry keys within HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options.

# Mitigation

To use this technique remotely, an adversary must use it in conjunction with RDP. Ensure that Network Level Authentication is enabled to force the remote desktop session to authenticate before the session is created and the login screen displayed. It is enabled by default on Windows Vista and later. [10]

If possible, use a Remote Desktop Gateway to manage connections and security configuration of RDP within a network. [11]

Identify and block potentially malicious software that may be executed by an adversary with this technique by using whitelisting [12] tools, like AppLocker, [13] [14] or Software Restriction Policies [15] where appropriate. [16]

# Footnotes

[1] Glyer, C., Kazanciyan, R. (2012, August 20). THE “HIKIT” ROOTKIT: ADVANCED AND PERSISTENT ATTACK TECHNIQUES (PART 1). Retrieved June 6, 2016.

[2] Maldonado, D., McGuffin, T. (2016, August 6). Sticky Keys to the Kingdom. Retrieved July 5, 2017.

[3] Tilbury, C. (2014, August 28). Registry Analysis with CrowdResponse. Retrieved November 12, 2014.

[4] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[5] Dunwoody, M. (2017, March 27). APT29 Domain Fronting With TOR. Retrieved March 27, 2017.

[6] valsmith. (2012, September 21). More on APTSim. Retrieved September 28, 2017.

[7] Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.

[8] RSA Incident Response. (2014, January). RSA Incident Response Emerging Threat Profile: Shell Crew. Retrieved January 14, 2016.

[9] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[10] Microsoft. (n.d.). Configure Network Level Authentication for Remote Desktop Services Connections. Retrieved June 6, 2016.

[11] Microsoft. (n.d.). Overview of Remote Desktop Gateway. Retrieved June 6, 2016.

[12] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[13] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[14] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[15] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[16] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

To use this technique remotely, an adversary must use it in conjunction with RDP. Ensure that Network Level Authentication is enabled to force the remote desktop session to authenticate before the session is created and the login screen displayed. It is e

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (5)

- [[Werkzeug Debugger Panel Read/Write RCE]]
- [[Windows - Elevated RDP Backdoor with Sticky Keys]]
- [[Windows - RDP Backdoor using utilman.exe]]
- [[Windows Registry HKLM Winlogon Helper DLL Persistence]]
- [[Windows Sticky Keys Persistence]]
