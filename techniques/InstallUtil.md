---
id: 935e5645-d305-48b2-88a1-419a8f19c45c
name: InstallUtil
type: technique
mitre_id: T1118
mitre_url: null
created_at: '2019-08-28T21:17:29.178431+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
---

# InstallUtil

**MITRE ID**: T1118

## Description

InstallUtil is a command-line utility that allows for installation and uninstallation of resources by executing specific installer components specified in .NET binaries. [1] InstallUtil is located in the .NET directories on a Windows system: C:\Windows\Microsoft.NET\Framework\v\InstallUtil.exe and C:\Windows\Microsoft.NET\Framework64\v\InstallUtil.exe. InstallUtil.exe is digitally signed by Microsoft.Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil may also be used to bypass process whitelisting through use of attributes within the binary that execute the class decorated with the attribute [System.ComponentModel.RunInstaller(true)]. [2]

# Detection

Use process monitoring to monitor the execution and arguments of InstallUtil.exe. Compare recent invocations of InstallUtil.exe with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after the InstallUtil.exe invocation may also be useful in determining the origin and purpose of the binary being executed.

# Mitigation

InstallUtil may not be necessary within a given environment. Use application whitelisting configured to block execution of InstallUtil.exe if it is not required for a given system or network to prevent potential misuse by adversaries.

# Footnotes

[1] Microsoft. (n.d.). Installutil.exe (Installer Tool). Retrieved July 1, 2016.

[2] Smith, C. (2016, August 17). Includes 5 Known Application Whitelisting/ Application Control Bypass Techniques in One File. Retrieved June 30, 2017.

## Defense

InstallUtil may not be necessary within a given environment. Use application whitelisting configured to block execution of InstallUtil.exe if it is not required for a given system or network to prevent potential misuse by adversaries.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (1)

- [[Linux Privilege Escalation - Writable Files Escalation]]
