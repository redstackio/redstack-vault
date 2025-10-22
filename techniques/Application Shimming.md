---
id: 750d805d-7fc1-49af-bbc9-2636fca87766
name: Application Shimming
type: technique
mitre_id: T1138
mitre_url: null
created_at: '2019-08-28T21:17:37.042063+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[POP Gadget .NET Serialization]]'
---

# Application Shimming

**MITRE ID**: T1138

## Description

The Microsoft Windows Application Compatibility Infrastructure/Framework (Application Shim) was created to allow for backward compatibility of software as the operating system codebase changes over time. For example, the application shimming feature allows developers to apply fixes to applications (without rewriting code) that were created for Windows XP so that it will work with Windows 10. [1] Within the framework, shims are created to act as a buffer between the program (or more specifically, the Import Address Table) and the Windows OS. When a program is executed, the shim cache is referenced to determine if the program requires the use of the shim database (.sdb). If so, the shim database uses Hooking to redirect the code as necessary in order to communicate with the OS. A list of all shims currently installed by the default Windows installer (sdbinst.exe) is kept in:%WINDIR%\AppPatch\sysmain.sdbhklm\software\microsoft\windows nt\currentversion\appcompatflags\installedsdbCustom databases are stored in:%WINDIR%\AppPatch\custom & %WINDIR%\AppPatch\AppPatch64\Customhklm\software\microsoft\windows nt\currentversion\appcompatflags\customTo keep shims secure, Windows designed them to run in user mode so they cannot modify the kernel and you must have administrator privileges to install a shim. However, certain shims can be used to Bypass User Account Control (UAC) (RedirectEXE), inject DLLs into processes (InjectDLL), disable Data Execution Prevention (DisableNX) and Structure Exception Handling (DisableSEH), and intercept memory addresses (GetProcAddress). Similar to Hooking, utilizing these shims may allow an adversary to perform several malicious acts such as elevate privileges, install backdoors, disable defenses like Windows Defender, etc.

# Detection

There are several public tools available that will detect shims that are currently available [3]:

Shim-Process-Scanner - checks memory of every running process for any Shim flagsShim-Detector-Lite - detects installation of custom shim databasesShim-Guard - monitors registry for any shim installationsShimScanner - forensic tool to find active shims in memoryShimCacheMem - Volatility plug-in that pulls shim cache from memory (note: shims are only cached after reboot)

Monitor process execution for sdbinst.exe and command-line arguments for potential indications of application shim abuse.

# Mitigation

There currently aren't a lot of ways to mitigate application shimming. Disabling the Shim Engine isn't recommended because Windows depends on shimming for interoperability and software may become unstable or not work. Microsoft released an optional patch update - KB3045645 - that will remove the "auto-elevate" flag within the sdbinst.exe. This will prevent use of application shimming to bypass UAC. 

Changing UAC settings to "Always Notify" will give the user more visibility when UAC elevation is requested, however, this option will not be popular among users due to the constant UAC interruptions.

# Footnotes

[1] Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.

[2] Erickson, J., McWhirt, M., Palombo, D. (2017, May 3). To SDB, Or Not To SDB: FIN7 Leveraging Shim Databases for Persistence. Retrieved July 18, 2017.

[3] Pierce, Sean. (2015, November). Defending Against Malicious Application Compatibility Shims. Retrieved June 22, 2017.

## Defense

There currently aren't a lot of ways to mitigate application shimming. Disabling the Shim Engine isn't recommended because Windows depends on shimming for interoperability and software may become unstable or not work. Microsoft released an optional patch 

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (1)

- [[POP Gadget .NET Serialization]]
