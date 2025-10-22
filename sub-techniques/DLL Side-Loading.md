---
id: dee4c341-233d-4b47-978c-97681c024687
name: DLL Side-Loading
type: sub-technique
mitre_id: T1574.002
mitre_url: null
created_at: '2023-04-06T00:31:27.106224+00:00'
updated_at: '2023-04-06T00:31:27.106224+00:00'
parent_technique: '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Apache Karaf XXE Out-of-Band Data Exfiltration]]'
- '[[AWS API Gateway Stage Enumeration]]'
- '[[Blind XPATH Injection]]'
---

# DLL Side-Loading

**MITRE ID**: T1574.002

**Parent Technique**: [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]

This is a sub-technique of T1574 - Hijack Execution Flow.

## Summary

Adversaries may execute their own malicious payloads by side-loading DLLs. Similar to [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001), side-loading involves hijacking which DLL a program loads. But rather than just planting the DLL within the search order of a program the

## Description

Adversaries may execute their own malicious payloads by side-loading DLLs. Similar to [DLL Search Order Hijacking](https://attack.mitre.org/techniques/T1574/001), side-loading involves hijacking which DLL a program loads. But rather than just planting the DLL within the search order of a program then waiting for the victim application to be invoked, adversaries may directly side-load their payloads by planting then invoking a legitimate application that executes their payload(s).

Side-loading takes advantage of the DLL search order used by the loader by positioning both the victim application and malicious payload(s) alongside each other. Adversaries likely use side-loading as a means of masking actions they perform under a legitimate, trusted, and potentially elevated system or software process. Benign executables used to side-load payloads may not be flagged during delivery and/or execution. Adversary payloads may also be encrypted/packed or otherwise obfuscated until loaded into the memory of the trusted process.(Citation: FireEye DLL Side-Loading)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 3 procedures using this sub-technique:

- [[Apache Karaf XXE Out-of-Band Data Exfiltration]]
- [[AWS API Gateway Stage Enumeration]]
- [[Blind XPATH Injection]]
