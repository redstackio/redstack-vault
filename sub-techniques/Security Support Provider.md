---
id: 02061b8c-b744-474a-97d6-9995d5c979b9
name: Security Support Provider
type: sub-technique
mitre_id: T1547.005
mitre_url: null
created_at: '2023-04-06T00:31:26.098156+00:00'
updated_at: '2023-04-06T00:31:26.098156+00:00'
parent_technique: '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart
  Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Security Support Provider

**MITRE ID**: T1547.005

**Parent Technique**: [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]

This is a sub-technique of T1547 - Boot or Logon Autostart Execution.

## Summary

Adversaries may abuse security support providers (SSPs) to execute DLLs when the system boots. Windows SSP DLLs are loaded into the Local Security Authority (LSA) process at system start. Once loaded into the LSA, SSP DLLs have access to encrypted and plaintext passwords that are stored in Windows, 

## Description

Adversaries may abuse security support providers (SSPs) to execute DLLs when the system boots. Windows SSP DLLs are loaded into the Local Security Authority (LSA) process at system start. Once loaded into the LSA, SSP DLLs have access to encrypted and plaintext passwords that are stored in Windows, such as any logged-on user's Domain password or smart card PINs.

The SSP configuration is stored in two Registry keys: <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages</code> and <code>HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages</code>. An adversary may modify these Registry keys to add new SSPs, which will be loaded the next time the system boots, or when the AddSecurityPackage Windows API function is called.(Citation: Graeber 2014)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
