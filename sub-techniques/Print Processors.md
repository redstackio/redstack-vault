---
id: 7a048474-95ef-4c27-adab-6738e9787569
name: Print Processors
type: sub-technique
mitre_id: T1547.012
mitre_url: null
created_at: '2023-04-06T00:31:25.817352+00:00'
updated_at: '2023-04-06T00:31:25.817352+00:00'
parent_technique: '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart
  Execution]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abuse Group Policy Objects with pyGPOAbuse]]'
- '[[Windows VM Persistence with VirtualBox and VHD]]'
---

# Print Processors

**MITRE ID**: T1547.012

**Parent Technique**: [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]

This is a sub-technique of T1547 - Boot or Logon Autostart Execution.

## Summary

Adversaries may abuse print processors to run malicious DLLs during system boot for persistence and/or privilege escalation. Print processors are DLLs that are loaded by the print spooler service, spoolsv.exe, during boot. 

Adversaries may abuse the print spooler service by adding print processors 

## Description

Adversaries may abuse print processors to run malicious DLLs during system boot for persistence and/or privilege escalation. Print processors are DLLs that are loaded by the print spooler service, spoolsv.exe, during boot. 

Adversaries may abuse the print spooler service by adding print processors that load malicious DLLs at startup. A print processor can be installed through the <code>AddPrintProcessor</code> API call with an account that has <code>SeLoadDriverPrivilege</code> enabled. Alternatively, a print processor can be registered to the print spooler service by adding the <code>HKLM\SYSTEM\\[CurrentControlSet or ControlSet001]\Control\Print\Environments\\[Windows architecture: e.g., Windows x64]\Print Processors\\[user defined]\Driver</code> Registry key that points to the DLL. For the print processor to be correctly installed, it must be located in the system print-processor directory that can be found with the <code>GetPrintProcessorDirectory</code> API call.(Citation: Microsoft AddPrintProcessor May 2018) After the print processors are installed, the print spooler service, which starts during boot, must be restarted in order for them to run.(Citation: ESET PipeMon May 2020) The print spooler service runs under SYSTEM level permissions, therefore print processors installed by an adversary may run under elevated privileges.

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Abuse Group Policy Objects with pyGPOAbuse]]
- [[Windows VM Persistence with VirtualBox and VHD]]
