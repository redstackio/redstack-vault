---
id: 4ca46afa-1ad4-4dfa-a1b6-5626d5c4f839
name: Component Object Model
type: sub-technique
mitre_id: T1559.001
mitre_url: null
created_at: '2023-04-06T00:31:25.832061+00:00'
updated_at: '2023-04-06T00:31:25.832061+00:00'
parent_technique: '[[Inter-Process Communication|T1559 - Inter-Process Communication]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
---

# Component Object Model

**MITRE ID**: T1559.001

**Parent Technique**: [[Inter-Process Communication|T1559 - Inter-Process Communication]]

This is a sub-technique of T1559 - Inter-Process Communication.

## Summary

Adversaries may use the Windows Component Object Model (COM) for local code execution. COM is an inter-process communication (IPC) component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more

## Description

Adversaries may use the Windows Component Object Model (COM) for local code execution. COM is an inter-process communication (IPC) component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces.(Citation: Fireeye Hunting COM June 2019) Through COM, a client object can call methods of server objects, which are typically binary Dynamic Link Libraries (DLL) or executables (EXE).(Citation: Microsoft COM) Remote COM execution is facilitated by [Remote Services](https://attack.mitre.org/techniques/T1021) such as  [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) (DCOM).(Citation: Fireeye Hunting COM June 2019)

Various COM interfaces are exposed that can be abused to invoke arbitrary execution via a variety of programming languages such as C, C++, Java, and [Visual Basic](https://attack.mitre.org/techniques/T1059/005).(Citation: Microsoft COM) Specific COM objects also exist to directly perform functions beyond code execution, such as creating a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), fileless download/execution, and other adversary behaviors related to privilege escalation and persistence.(Citation: Fireeye Hunting COM June 2019)(Citation: ProjectZero File Write EoP Apr 2018)

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]
