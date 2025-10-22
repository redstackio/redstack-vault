---
id: 732aadf8-40e4-4629-98cf-9ccd9340661b
name: File Deletion
type: sub-technique
mitre_id: T1070.004
mitre_url: null
created_at: '2023-04-06T00:31:27.027956+00:00'
updated_at: '2023-04-06T00:31:27.027956+00:00'
parent_technique: '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Linux Command History Evasion]]'
- '[[Obfuscating AWS CloudTrail and GuardDuty Logs]]'
- '[[SQLite Injection - Remote Command Execution using Load_extension]]'
---

# File Deletion

**MITRE ID**: T1070.004

**Parent Technique**: [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

This is a sub-technique of T1070 - Indicator Removal on Host.

## Summary

Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex: [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) may leave traces to indicate to what was done within 

## Description

Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex: [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) may leave traces to indicate to what was done within a network and how. Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.

There are tools available from the host operating system to perform cleanup, but adversaries may use other tools as well.(Citation: Microsoft SDelete July 2016) Examples of built-in [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) functions include <code>del</code> on Windows and <code>rm</code> or <code>unlink</code> on Linux and macOS.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 3 procedures using this sub-technique:

- [[Linux Command History Evasion]]
- [[Obfuscating AWS CloudTrail and GuardDuty Logs]]
- [[SQLite Injection - Remote Command Execution using Load_extension]]
