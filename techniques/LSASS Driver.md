---
id: 23c9261a-3041-44cc-9959-54b8a72a560b
name: LSASS Driver
type: technique
mitre_id: T1177
mitre_url: null
created_at: '2019-08-28T21:17:29.297142+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[PHP Object Injection for Arbitrary Code Execution]]'
---

# LSASS Driver

**MITRE ID**: T1177

## Description

The Windows security subsystem is a set of components that manage and enforce the security policy for a computer or domain. The Local Security Authority (LSA) is the main component responsible for local security policy and user authentication. The LSA includes multiple dynamic link libraries (DLLs) associated with various other security functions, all of which run in the context of the LSA Subsystem Service (LSASS) lsass.exe process. [1]Adversaries may target lsass.exe drivers to obtain execution and/or persistence. By either replacing or adding illegitimate drivers (e.g., DLL Side-Loading or DLL Search Order Hijacking), an adversary can achieve arbitrary code execution triggered by continuous LSA operations.

# Detection

With LSA Protection enabled, monitor the event logs (Events 3033 and 3063) for failed attempts to load LSA plug-ins and drivers. [5]

Utilize the Sysinternals Autoruns/Autorunsc utility [9] to examine loaded drivers associated with the LSA.

Utilize the Sysinternals Process Monitor utility to monitor DLL load operations in lsass.exe. [8]

# Mitigation

On Windows 8.1 and Server 2012 R2, enable LSA Protection by setting the Registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL to dword:00000001. [5] LSA Protection ensures that LSA plug-ins and drivers are only loaded if they are digitally signed with a Microsoft signature and adhere to the Microsoft Security Development Lifecycle (SDL) process guidance.

On Windows 10 and Server 2016, enable Windows Defender Credential Guard [6] to run lsass.exe in an isolated virtualized environment without any device drivers. [7]

Ensure safe DLL search mode is enabled HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode to mitigate risk that lsass.exe loads a malicious code library. [8]

# Footnotes

[1] Microsoft. (n.d.). Security Subsystem Architecture. Retrieved November 27, 2017.

[2] Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.

[3] Anthe, C. et al. (2016, December 14). Microsoft Security Intelligence Report Volume 21. Retrieved November 27, 2017.

[4] Microsoft. (2017, November 9). Backdoor:Win32/Wingbird.A!dha. Retrieved November 27, 2017.

[5] Microsoft. (2014, March 12). Configuring Additional LSA Protection. Retrieved November 27, 2017.

[6] Lich, B., Tobin, J., Hall, J. (2017, April 5). Manage Windows Defender Credential Guard. Retrieved November 27, 2017.

[7] Lich, B., Tobin, J. (2017, April 5). How Windows Defender Credential Guard works. Retrieved November 27, 2017.

[8] Microsoft. (n.d.). Dynamic-Link Library Security. Retrieved November 27, 2017.

[9] Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.

## Defense

On Windows 8.1 and Server 2012 R2, enable LSA Protection by setting the Registry key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL</code> to <code>dword:00000001</code>. (Citation: Microsoft LSA Protection Mar 2014) LSA Protection

## Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures (1)

- [[PHP Object Injection for Arbitrary Code Execution]]
