---
id: 3493263e-b24d-4c00-b133-c94a903d4be7
name: Trusted Developer Utilities
type: technique
mitre_id: T1127
mitre_url: null
created_at: '2019-08-28T21:17:46.446617+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Msbuild Preprocessing Execution]]'
- '[[MSBuild Shellcode Execution]]'
- '[[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]'
- '[[Windows AppLocker Whitelist Bypass (MSBuild.exe)]]'
---

# Trusted Developer Utilities

**MITRE ID**: T1127

## Description

There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering. These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application whitelisting defensive solutions.MSBuildMSBuild.exe (Microsoft Build Engine) is a software build platform used by Visual Studio. It takes XML formatted project files that define requirements for building various platforms and configurations. [1] Adversaries can use MSBuild to proxy execution of code through a trusted Windows utility. The inline task capability of MSBuild that was introduced in .NET version 4 allows for C# code to be inserted into the XML project file. [1] Inline Tasks MSBuild will compile and execute the inline task. MSBuild.exe is a signed Microsoft binary, so when it is used this way it can execute arbitrary code and bypass application whitelisting defenses that are configured to allow MSBuild.exe execution. [2]DNXThe .NET Execution Environment (DNX), dnx.exe, is a software development kit packaged with Visual Studio Enterprise. It was retired in favor of .NET Core CLI in 2016. [3] DNX is not present on standard builds of Windows and may only be present on developer workstations using older versions of .NET Core and ASP.NET Core 1.0. The dnx.exe executable is signed by Microsoft. An adversary can use dnx.exe to proxy execution of arbitrary code to bypass application whitelist policies that do not account for DNX. [4]RCSIThe rcsi.exe utility is a non-interactive command-line interface for C# that is similar to csi.exe. It was provided within an early version of the Roslyn .NET Compiler Platform but has since been deprecated for an integrated solution. [5] The rcsi.exe binary is signed by Microsoft. [6]C# .csx script files can be written and executed with rcsi.exe at the command-line. An adversary can use rcsi.exe to proxy execution of arbitrary code to bypass application whitelisting policies that do not account for execution of rcsi.exe. [6]WinDbg/CDBWinDbg is a Microsoft Windows kernel and user-mode debugging utility. The Microsoft Console Debugger (CDB) cdb.exe is also user-mode debugger. Both utilities are included in Windows software development kits and can be used as standalone tools. [7] They are commonly used in software development and reverse engineering and may not be found on typical Windows systems. Both WinDbg.exe and cdb.exe binaries are signed by Microsoft.An adversary can use WinDbg.exe and cdb.exe to proxy execution of arbitrary code to bypass application whitelist policies that do not account for execution of those utilities. [8]It is likely possible to use other debuggers for similar purposes, such as the kernel-mode debugger kd.exe, which is also signed by Microsoft.TrackerThe file tracker utility, tracker.exe, is included with the .NET framework as part of MSBuild. It is used for logging calls to the Windows file system. [9]An adversary can use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed it can be used to bypass application whitelisting solutions. [10]

# Detection

The presence of these or other utilities that enable proxy execution that are typically used for development, debugging, and reverse engineering on a system that is not used for these purposes may be suspicious.

Use process monitoring to monitor the execution and arguments of MSBuild.exe, dnx.exe, rcsi.exe, WinDbg.exe, cdb.exe, and tracker.exe. Compare recent invocations of those binaries with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. It is likely that these utilities will be used by software developers or for other software development related tasks, so if it exists and is used outside of that context, then the event may be suspicious. Command arguments used before and after invocation of the utilities may also be useful in determining the origin and purpose of the binary being executed.

# Mitigation

MSBuild.exe, dnx.exe, rcsi.exe, WinDbg.exe, cdb.exe, and tracker.exe may not be necessary within a given environment and should be removed if not used.

Use application whitelisting configured to block execution of MSBuild.exe, dnx.exe, rcsi.exe, WinDbg.exe, and cdb.exe if they are not required for a given system or network to prevent potential misuse by adversaries. [13] [14] [15] [16]

# Footnotes

[1] Microsoft. (n.d.). MSBuild1. Retrieved November 30, 2016.

[2] Smith, C. (2016, August 17). Includes 5 Known Application Whitelisting/ Application Control Bypass Techniques in One File. Retrieved June 30, 2017.

[3] Knezevic, Z., Wenzel, M. Latham, L. (2016, June 20). Migrating from DNX to .NET Core CLI (project.json). Retrieved June 28, 2017.

[4] Nelson, M. (2017, November 17). Bypassing Application Whitelisting By Using dnx.exe. Retrieved May 25, 2017.

[5] Osenkov, K. (2011, October 19). Introducing the Microsoft “Roslyn” CTP. Retrieved June 28, 2017.

[6] Nelson, M. (2016, November 21). Bypassing Application Whitelisting By Using rcsi.exe. Retrieved May 26, 2017.

[7] Marshall, D. (2017, May 23). Debugging Tools for Windows (WinDbg, KD, CDB, NTSD). Retrieved June 29, 2017.

[8] Graeber, M. (2016, August 15). Bypassing Application Whitelisting by using WinDbg/CDB as a Shellcode Runner. Retrieved May 26, 2017.

[9] B, M., Brown, K., Cai, S., Hogenson, G., Warren, G. (2016, November 4). File Tracking. Retrieved November 1, 2017.

[10] Smith, C. (2016, October 31). SubTee Twitter Status. Retrieved November 1, 2017.

[11] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[12] Lancaster, T. and Idrizovic, E.. (2017, June 27). Paranoid PlugX. Retrieved July 13, 2017.

[13] Microsoft. (2017, June 16). Deploy code integrity policies: steps. Retrieved June 28, 2017.

[14] Graeber, M. (2016, September 8). Using Device Guard to Mitigate Against Device Guard Bypasses. Retrieved September 13, 2016.

[15] Graeber, M. (2016, November 13). DeviceGuardBypassMitigationRules. Retrieved November 30, 2016.

[16] Smith, C. (2016, September 13). Bypassing Application Whitelisting using MSBuild.exe - Device Guard Example and Mitigations. Retrieved September 13, 2016.

## Defense

MSBuild.exe, dnx.exe, rcsi.exe, WinDbg.exe, cdb.exe, and tracker.exe may not be necessary within a given environment and should be removed if not used.

Use application whitelisting configured to block execution of MSBuild.exe, dnx.exe, rcsi.exe, WinDbg.e

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (4)

- [[Msbuild Preprocessing Execution]]
- [[MSBuild Shellcode Execution]]
- [[PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets]]
- [[Windows AppLocker Whitelist Bypass (MSBuild.exe)]]
