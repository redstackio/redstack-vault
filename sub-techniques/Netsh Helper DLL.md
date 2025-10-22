---
id: 4136818e-5680-461a-8a7f-dbb5042b31dd
name: Netsh Helper DLL
type: sub-technique
mitre_id: T1546.007
mitre_url: null
created_at: '2023-04-06T00:31:27.203194+00:00'
updated_at: '2023-04-06T00:31:27.203194+00:00'
parent_technique: '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Netsh Helper DLL

**MITRE ID**: T1546.007

**Parent Technique**: [[Event Triggered Execution|T1546 - Event Triggered Execution]]

This is a sub-technique of T1546 - Event Triggered Execution.

## Summary

Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs. Netsh.exe (also referred to as Netshell) is a command-line scripting utility used to interact with the network configuration of a system. It contains functionality to add helper DLLs for extending fu

## Description

Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs. Netsh.exe (also referred to as Netshell) is a command-line scripting utility used to interact with the network configuration of a system. It contains functionality to add helper DLLs for extending functionality of the utility.(Citation: TechNet Netsh) The paths to registered netsh.exe helper DLLs are entered into the Windows Registry at <code>HKLM\SOFTWARE\Microsoft\Netsh</code>.

Adversaries can use netsh.exe helper DLLs to trigger execution of arbitrary code in a persistent manner. This execution would take place anytime netsh.exe is executed, which could happen automatically, with another persistence technique, or if other software (ex: VPN) is present on the system that executes netsh.exe as part of its normal functionality.(Citation: Github Netsh Helper CS Beacon)(Citation: Demaske Netsh Persistence)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
