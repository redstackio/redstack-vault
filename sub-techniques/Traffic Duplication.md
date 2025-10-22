---
id: 767ea3e7-433f-4459-bcf4-23eb19b7cadf
name: Traffic Duplication
type: sub-technique
mitre_id: T1020.001
mitre_url: null
created_at: '2023-04-06T00:31:26.418318+00:00'
updated_at: '2023-04-06T00:31:26.418318+00:00'
parent_technique: '[[Automated Exfiltration|T1020 - Automated Exfiltration]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[.NET Serialization Tools Exploitation]]'
---

# Traffic Duplication

**MITRE ID**: T1020.001

**Parent Technique**: [[Automated Exfiltration|T1020 - Automated Exfiltration]]

This is a sub-technique of T1020 - Automated Exfiltration.

## Summary

Adversaries may leverage traffic mirroring in order to automate data exfiltration over compromised network infrastructure.  Traffic mirroring is a native feature for some network devices and used for network analysis and may be configured to duplicate traffic and forward to one or more destinations 

## Description

Adversaries may leverage traffic mirroring in order to automate data exfiltration over compromised network infrastructure.  Traffic mirroring is a native feature for some network devices and used for network analysis and may be configured to duplicate traffic and forward to one or more destinations for analysis by a network analyzer or other monitoring device. (Citation: Cisco Traffic Mirroring)(Citation: Juniper Traffic Mirroring)

Adversaries may abuse traffic mirroring to mirror or redirect network traffic through other network infrastructure they control. Malicious modifications to network devices to enable traffic redirection may be possible through [ROMMONkit](https://attack.mitre.org/techniques/T1542/004) or [Patch System Image](https://attack.mitre.org/techniques/T1601/001).(Citation: US-CERT-TA18-106A)(Citation: Cisco Blog Legacy Device Attacks) Adversaries may use traffic duplication in conjunction with [Network Sniffing](https://attack.mitre.org/techniques/T1040), [Input Capture](https://attack.mitre.org/techniques/T1056), or [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) depending on the goals and objectives of the adversary.

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[.NET Serialization Tools Exploitation]]
