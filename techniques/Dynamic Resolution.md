---
id: 0e7485ac-9d4d-4c47-b78e-4bec0b32dbb4
name: Dynamic Resolution
type: technique
mitre_id: T1568
mitre_url: null
created_at: '2023-04-06T00:31:26.409446+00:00'
updated_at: '2023-04-06T03:56:40.911686+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[DNS Beacon Payload with Cobalt Strike]]'
- '[[DNS Rebinding Protection Bypass via CNAME]]'
- '[[Git Index File Recovery]]'
- '[[Git Source Code Leakage]]'
- '[[Image-Based .htaccess Upload]]'
---

# Dynamic Resolution

**MITRE ID**: T1568

## Description

Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculations can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

Adversaries may use dynamic resolution for the purpose of [Fallback Channels](https://attack.mitre.org/techniques/T1008). When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing command and control.(Citation: Talos CCleanup 2017)(Citation: FireEye POSHSPY April 2017)(Citation: ESET Sednit 2017 Activity)

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (5)

- [[DNS Beacon Payload with Cobalt Strike]]
- [[DNS Rebinding Protection Bypass via CNAME]]
- [[Git Index File Recovery]]
- [[Git Source Code Leakage]]
- [[Image-Based .htaccess Upload]]
