---
id: f69ed6d1-2d83-48cf-8f12-c414714189f3
name: MSBuild
type: sub-technique
mitre_id: T1127.001
mitre_url: null
created_at: '2023-04-06T00:31:26.920159+00:00'
updated_at: '2023-04-06T00:31:26.920159+00:00'
parent_technique: '[[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Msbuild Preprocessing Execution]]'
---

# MSBuild

**MITRE ID**: T1127.001

**Parent Technique**: [[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]

This is a sub-technique of T1127 - Trusted Developer Utilities.

## Summary

Adversaries may use MSBuild to proxy execution of code through a trusted Windows utility. MSBuild.exe (Microsoft Build Engine) is a software build platform used by Visual Studio. It handles XML formatted project files that define requirements for loading and building various platforms and configurat

## Description

Adversaries may use MSBuild to proxy execution of code through a trusted Windows utility. MSBuild.exe (Microsoft Build Engine) is a software build platform used by Visual Studio. It handles XML formatted project files that define requirements for loading and building various platforms and configurations.(Citation: MSDN MSBuild)

Adversaries can abuse MSBuild to proxy execution of malicious code. The inline task capability of MSBuild that was introduced in .NET version 4 allows for C# or Visual Basic code to be inserted into an XML project file.(Citation: MSDN MSBuild)(Citation: Microsoft MSBuild Inline Tasks 2017) MSBuild will compile and execute the inline task. MSBuild.exe is a signed Microsoft binary, so when it is used this way it can execute arbitrary code and bypass application control defenses that are configured to allow MSBuild.exe execution.(Citation: LOLBAS Msbuild)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Msbuild Preprocessing Execution]]
