---
id: eb386478-eacb-4197-8fd6-e2a55d9bc732
name: Verclsid
type: sub-technique
mitre_id: T1218.012
mitre_url: null
created_at: '2023-04-06T00:31:26.474232+00:00'
updated_at: '2023-04-06T00:31:26.474232+00:00'
parent_technique: '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
---

# Verclsid

**MITRE ID**: T1218.012

**Parent Technique**: [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

This is a sub-technique of T1218 - Signed Binary Proxy Execution.

## Summary

Adversaries may abuse verclsid.exe to proxy execution of malicious code. Verclsid.exe is known as the Extension CLSID Verification Host and is responsible for verifying each shell extension before they are used by Windows Explorer or the Windows Shell.(Citation: WinOSBite verclsid.exe)

Adversaries 

## Description

Adversaries may abuse verclsid.exe to proxy execution of malicious code. Verclsid.exe is known as the Extension CLSID Verification Host and is responsible for verifying each shell extension before they are used by Windows Explorer or the Windows Shell.(Citation: WinOSBite verclsid.exe)

Adversaries may abuse verclsid.exe to execute malicious payloads. This may be achieved by running <code>verclsid.exe /S /C {CLSID}</code>, where the file is referenced by a Class ID (CLSID), a unique identification number used to identify COM objects. COM payloads executed by verclsid.exe may be able to perform various malicious actions, such as loading and executing COM scriptlets (SCT) from remote servers (similar to [Regsvr32](https://attack.mitre.org/techniques/T1218/010)). Since the binary may be signed and/or native on Windows systems, proxying execution via verclsid.exe may bypass application control solutions that do not account for its potential abuse.(Citation: LOLBAS Verclsid)(Citation: Red Canary Verclsid.exe)(Citation: BOHOPS Abusing the COM Registry)(Citation: Nick Tyrer GitHub) 

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
