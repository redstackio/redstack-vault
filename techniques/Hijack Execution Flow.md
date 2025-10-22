---
id: b84971a2-f4bb-4fea-b181-2584348c8d57
name: Hijack Execution Flow
type: technique
mitre_id: T1574
mitre_url: null
created_at: '2023-04-06T00:31:26.725502+00:00'
updated_at: '2023-05-24T16:04:41.655542+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Apache Karaf XXE Out-of-Band Data Exfiltration]]'
- '[[AWS API Gateway Stage Enumeration]]'
- '[[Blind XPATH Injection]]'
- '[[Git Hook Persistence]]'
- '[[Linux - Privilege Escalation via Shared Library Dependencies]]'
- '[[Linux - Privilege Escalation via Shared Library RPATH Hijacking]]'
---

# Hijack Execution Flow

**MITRE ID**: T1574

## Description

Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions on execution.

There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs/resources, such as file directories and in the case of Windows the Registry, could also be poisoned to include malicious payloads.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (6)

- [[Apache Karaf XXE Out-of-Band Data Exfiltration]]
- [[AWS API Gateway Stage Enumeration]]
- [[Blind XPATH Injection]]
- [[Git Hook Persistence]]
- [[Linux - Privilege Escalation via Shared Library Dependencies]]
- [[Linux - Privilege Escalation via Shared Library RPATH Hijacking]]
