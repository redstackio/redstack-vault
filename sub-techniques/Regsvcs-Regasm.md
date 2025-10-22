---
id: 8123df65-1909-4831-bb67-fc8b80d8d490
name: Regsvcs/Regasm
type: sub-technique
mitre_id: T1218.009
mitre_url: null
created_at: '2023-04-06T00:31:26.891206+00:00'
updated_at: '2023-04-06T00:31:26.891206+00:00'
parent_technique: '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
---

# Regsvcs/Regasm

**MITRE ID**: T1218.009

**Parent Technique**: [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

This is a sub-technique of T1218 - Signed Binary Proxy Execution.

## Summary

Adversaries may abuse Regsvcs and Regasm to proxy execution of code through a trusted Windows utility. Regsvcs and Regasm are Windows command-line utilities that are used to register .NET [Component Object Model](https://attack.mitre.org/techniques/T1559/001) (COM) assemblies. Both are binaries that

## Description

Adversaries may abuse Regsvcs and Regasm to proxy execution of code through a trusted Windows utility. Regsvcs and Regasm are Windows command-line utilities that are used to register .NET [Component Object Model](https://attack.mitre.org/techniques/T1559/001) (COM) assemblies. Both are binaries that may be digitally signed by Microsoft. (Citation: MSDN Regsvcs) (Citation: MSDN Regasm)

Both utilities may be used to bypass application control through use of attributes within the binary to specify code that should be run before registration or unregistration: <code>[ComRegisterFunction]</code> or <code>[ComUnregisterFunction]</code> respectively. The code with the registration and unregistration attributes will be executed even if the process is run under insufficient privileges and fails to execute. (Citation: LOLBAS Regsvcs)(Citation: LOLBAS Regasm)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
