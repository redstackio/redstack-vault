---
id: 6e77171a-7ae1-4003-9dd6-09435160cb17
name: Services File Permissions Weakness
type: sub-technique
mitre_id: T1574.010
mitre_url: null
created_at: '2023-04-06T00:31:26.639443+00:00'
updated_at: '2023-04-06T00:31:26.639443+00:00'
parent_technique: '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Services File Permissions Weakness

**MITRE ID**: T1574.010

**Parent Technique**: [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]

This is a sub-technique of T1574 - Hijack Execution Flow.

## Summary

Adversaries may execute their own malicious payloads by hijacking the binaries used by services. Adversaries may use flaws in the permissions of Windows services to replace the binary that is executed upon service start. These service processes may automatically execute specific binaries as part of 

## Description

Adversaries may execute their own malicious payloads by hijacking the binaries used by services. Adversaries may use flaws in the permissions of Windows services to replace the binary that is executed upon service start. These service processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

Adversaries may use this technique to replace legitimate binaries with malicious ones as a means of executing code at a higher permissions level. If the executing process is set to run at a specific time or during a certain event (e.g., system bootup) then this technique can also be used for persistence.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
