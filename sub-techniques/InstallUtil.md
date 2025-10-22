---
id: 07244153-a31d-45c3-afe9-e254411f17b6
name: InstallUtil
type: sub-technique
mitre_id: T1218.004
mitre_url: null
created_at: '2023-04-06T00:31:25.806290+00:00'
updated_at: '2023-04-06T00:31:25.806290+00:00'
parent_technique: '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
---

# InstallUtil

**MITRE ID**: T1218.004

**Parent Technique**: [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

This is a sub-technique of T1218 - Signed Binary Proxy Execution.

## Summary

Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil is a command-line utility that allows for installation and uninstallation of resources by executing specific installer components specified in .NET binaries. (Citation: MSDN InstallUtil) The Ins

## Description

Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil is a command-line utility that allows for installation and uninstallation of resources by executing specific installer components specified in .NET binaries. (Citation: MSDN InstallUtil) The InstallUtil binary may also be digitally signed by Microsoft and located in the .NET directories on a Windows system: <code>C:\Windows\Microsoft.NET\Framework\v<version>\InstallUtil.exe</code> and <code>C:\Windows\Microsoft.NET\Framework64\v<version>\InstallUtil.exe</code>.

InstallUtil may also be used to bypass application control through use of attributes within the binary that execute the class decorated with the attribute <code>[System.ComponentModel.RunInstaller(true)]</code>. (Citation: LOLBAS Installutil)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
