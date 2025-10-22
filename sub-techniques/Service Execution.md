---
id: 37e3ea29-3221-43c7-8654-7c5ad1c66aa4
name: Service Execution
type: sub-technique
mitre_id: T1569.002
mitre_url: null
created_at: '2023-04-06T00:31:27.165722+00:00'
updated_at: '2023-04-06T00:31:27.165722+00:00'
parent_technique: '[[System Services|T1569 - System Services]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
---

# Service Execution

**MITRE ID**: T1569.002

**Parent Technique**: [[System Services|T1569 - System Services]]

This is a sub-technique of T1569 - System Services.

## Summary

Adversaries may abuse the Windows service control manager to execute malicious commands or payloads. The Windows service control manager (<code>services.exe</code>) is an interface to manage and manipulate services.(Citation: Microsoft Service Control Manager) The service control manager is accessib

## Description

Adversaries may abuse the Windows service control manager to execute malicious commands or payloads. The Windows service control manager (<code>services.exe</code>) is an interface to manage and manipulate services.(Citation: Microsoft Service Control Manager) The service control manager is accessible to users via GUI components as well as system utilities such as <code>sc.exe</code> and [Net](https://attack.mitre.org/software/S0039).

[PsExec](https://attack.mitre.org/software/S0029) can also be used to execute commands or payloads via a temporary Windows service created through the service control manager API.(Citation: Russinovich Sysinternals) Tools such as [PsExec](https://attack.mitre.org/software/S0029) and <code>sc.exe</code> can accept remote servers as arguments and may be used to conduct remote execution.

Adversaries may leverage these mechanisms to execute malicious content. This can be done by either executing a new or modified service. This technique is the execution used in conjunction with [Windows Service](https://attack.mitre.org/techniques/T1543/003) during service persistence or privilege escalation.

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]
